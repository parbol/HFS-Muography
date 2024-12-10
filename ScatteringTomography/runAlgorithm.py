###################################################################################
####### HSF - VECC workshop at Kolkata Dec. 2024                            #######
####### Hands-on exercise on scattering muography                           #######
####### Author: Pablo Martinez Ruiz del Arbol (IFCA)                        #######
###################################################################################                                    
import sys, optparse
import pandas as pd
import matplotlib as plt
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
    binInfo['threahold1'] = 0
    binInfo['threahold2'] = 0
    binInfo['xynbinx'] = 160
    binInfo['xynbiny'] = 160
    binInfo['xznbinx'] = 40
    binInfo['xznbinz'] = 20
    binInfo['yznbiny'] = 40
    binInfo['yznbinz'] = 20
 
    fig, ax = plt.subplots(3)

    pEstimator = POCAEstimator(dataset, binInfo, ax)
    pEstimator.loop()
    
    plt.save(opts.output)
    


