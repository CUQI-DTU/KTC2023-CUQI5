# read files in Output folder

#%%
import os
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
Nel = 32  # number of electrodes
from skimage.segmentation import chan_vese
from EITLib.segmentation import scoring_function
import KTCScoring

#%%


#%%
for i in range(1,5):
    recon_file = sp.io.loadmat('Output1/' + str(i) +'.mat')


    plt.figure()
    im = plt.imshow(recon_file['reconstruction'])
    plt.title('reconstruction '+str(i))
    plt.colorbar(im)

    # plot the true conductivity
    plt.figure()
    phantom_file = sp.io.loadmat('GroundTruths/true'+str(i)+'.mat')
    im = plt.imshow(phantom_file['truth'])
    plt.title('true conductivity '+str(i))
    plt.colorbar(im)

    # load original reconstruction
    plt.figure()
    orig_recon = np.load('Output1/' + str(i) +'.npz')['deltareco_pixgrid']
    im = plt.imshow(np.log(orig_recon))
    plt.title('log orig recon conductivity '+str(i))
    plt.colorbar(im)

    # load KTC challange recon

    # segment with chan-vese
    plt.figure()
    seg = KTCScoring.cv_NLOpt(orig_recon, log_par=1.5, linear_par=1, exp_par=0)
    im = plt.imshow(seg)
    plt.colorbar(im)
    plt.title('chan-vese segmentation '+str(i))
    
    print(i)
    print(scoring_function(phantom_file['truth'], seg))

    

# %%
