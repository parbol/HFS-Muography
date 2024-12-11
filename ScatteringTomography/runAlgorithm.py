###################################################################################
####### HSF - VECC workshop at Kolkata Dec. 2024                            #######
####### Hands-on exercise on scattering muography                           #######
####### Author: Pablo Martinez Ruiz del Arbol (IFCA)                        #######
###################################################################################                                    
import sys, optparse
import pandas as pd
import matplotlib.pyplot as plt
from tools.POCAEstimator import POCAEstimator


if __name__=='__main__':

    parser = optparse.OptionParser(usage='usage: %prog [options] path', version='%prog 1.0')
    parser.add_option('-i', '--input', action='store', type='string', dest='inputFile', default='input.h5', help='Input hdf5 File')
    parser.add_option('-o', '--output', action='store', type='string', dest='outputFile', default='.', help='Output file')
    (opts, args) = parser.parse_args()
    
    try:
        dataset= pd.read_hdf(opts.inputFile)
    except:
        print('Cannot open input file')
        sys.exit()

  
    #Data structure for selection and plotting
    binInfo = dict()
    binInfo['threshold1'] = 0.1
    binInfo['threshold2'] = 0.1
    binInfo['xynbinx'] = 160
    binInfo['xynbiny'] = 160
    binInfo['xznbinx'] = 160
    binInfo['xznbinz'] = 160
    binInfo['yznbiny'] = 160
    binInfo['yznbinz'] = 160
    binInfo['limitX'] = [-30, 30]
    binInfo['limitY'] = [-30, 30]
    binInfo['limitZ'] = [-5, 5]

 
    fig, ax = plt.subplots(2, 3, figsize=(16, 10))
    ax[0][0].set_title('Frontal view XY')
    ax[0][1].set_title('Side view XZ')
    ax[0][2].set_title('Side view YZ')
    ax[0][0].set_xlabel('X [cm]')
    ax[0][0].set_ylabel('Y [cm]')
    ax[0][1].set_xlabel('X [cm]')
    ax[0][1].set_ylabel('Z [cm]')
    ax[0][2].set_xlabel('Y [cm]')
    ax[0][2].set_ylabel('Z [cm]')


    pEstimator = POCAEstimator(dataset, binInfo, ax)
    pEstimator.loop()
    
    plt.savefig(opts.outputFile)
    


