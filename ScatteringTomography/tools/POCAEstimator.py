###################################################################################
####### HSF - VECC workshop at Kolkata Dec. 2024                            #######
####### Hands-on exercise on scattering muography                           #######
####### Author: Pablo Martinez Ruiz del Arbol (IFCA)                        #######
###################################################################################                                    
import pandas as pd
import numpy as np
import matplotlib as plt
from scipy.stats import gaussian_kde as kde

class POCAEstimator:

    def __init__(self, dataset, binInfo, axs):
 
        self.dataset = dataset
        self.binInfo = binInfo
        self.axs = axs
         
    def loop(self):
        
        #Coordinates of the poca Point
        ax = []
        ay = []
        az = []
        
        # loop through the rows using iterrows()
        for index, row in self.dataset.iterrows(): 
            #if index > 100:
            #    break
            r1 = np.asarray([row['x1'], row['y1'], row['z1']])
            r2 = np.asarray([row['x2'], row['y2'], row['z2']])
            v1 = np.asarray([row['vx1'], row['vy1'], row['vz1']])
            v2 = np.asarray([row['vx2'], row['vy2'], row['vz2']])
            dtx = row['dthetax']
            dty = row['dthetay']
            
            valid = False
            ###Apply here a simple angular selection
            if abs(dtx) > self.binInfo['threshold1'] or abs(dty) > self.binInfo['threshold2']:
                valid, v = self.getPoint(r1, r2, v1, v2)
                if not valid:
                    continue
                if v[0] < self.binInfo['limitX'][0] or v[0] > self.binInfo['limitX'][1]:
                    continue
                if v[1] < self.binInfo['limitY'][0] or v[1] > self.binInfo['limitY'][1]:
                    continue
                if v[2] < self.binInfo['limitZ'][0] or v[2] > self.binInfo['limitZ'][1]:
                    continue
                ax.append(v[0])
                ay.append(v[1])
                az.append(v[2])
            else:
                continue
      
        x = np.asarray(ax)
        y = np.asarray(ay)
        z = np.asarray(az)

        self.axs[0][0].hist2d(x, y, bins=(self.binInfo['xynbinx'], self.binInfo['xynbiny']), cmap=plt.cm.jet)
        self.axs[0][1].hist2d(x, z, bins=(self.binInfo['xznbinx'], self.binInfo['xznbinz']), cmap=plt.cm.jet)
        self.axs[0][2].hist2d(y, z, bins=(self.binInfo['yznbiny'], self.binInfo['yznbinz']), cmap=plt.cm.jet)
        

        k = kde(np.asarray([x, y]))
        xi, yi = np.mgrid[x.min():x.max():4.0*self.binInfo['xynbinx']*1j, y.min():y.max():4.0*self.binInfo['xynbiny']*1j]
        zi = k(np.vstack([xi.flatten(), yi.flatten()]))
        self.axs[1][0].pcolormesh(xi, yi, zi.reshape(xi.shape), shading='gouraud', cmap=plt.cm.jet)


   
    def getPoint(self, r1, r2, v1, v2):

        #Calculation of the closest point of approach
        cross_st = np.cross(v1, v2)
        cross_stnorm = np.linalg.norm(cross_st)
        vts = np.dot(v1, v2)
        if cross_stnorm < 1.0e-6 or vts < 1.0e-6:
            return False, [0, 0, 0]
        cross_sst = np.cross(v1, cross_st)
        DeltaR = r1 - r2        
        xpoca2 = r2 - v2 * np.dot(DeltaR, cross_sst)/cross_stnorm**2
        xpoca1 = r1 + v1 * np.dot((xpoca2-r1), v1)/vts
        v = 0.5 * (xpoca1 + xpoca2)
        return True, v
 
   