# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 08:33:53 2013

@author: jz026613
"""
from __future__ import division
import numpy as np
import pylab as plt
import os
from plot_recurrence import rec_plot

example = 'chainsaw' # 'chainsaw', 'disconnect'
os.chdir(os.path.join('examples', example))

IMF = np.load(example+'.npy')
S = np.sum(IMF, axis=0)
t = np.arange(0, S.size).astype(np.float32)

# Params
eps = 0.005
steps = 20
if example == 'disconnect':
    n_start, N = 2000, 5000
else:
    n_start, N = 15000, 3000

norm = lambda X: (X-X.mean())/np.max(np.abs(X-X.mean()))

# From now on everythin is in images dir
os.chdir('images')

# Plot recurrence plot
print("Original signal - recurrence plot")

fig = plt.figure()
rec = rec_plot(norm(S)[n_start:n_start+N], eps=eps, steps=steps)
plt.imshow(rec, extent=[n_start,n_start+N,n_start+N,n_start])
plt.savefig(example+'_orgRec',dpi=200)
plt.close()

# Plot each imf figure
for imfNum in range(IMF.shape[0]):

    F = IMF[imfNum]
    fNorm = norm(F)

    # Plot recurrence plot
    print("IMF %i - recurrence plot" %imfNum)
    fig = plt.figure()
    rp = rec_plot(fNorm[n_start:n_start+N], eps=eps, steps=steps)
    plt.imshow(rp,extent=[n_start,n_start+N,n_start+N,n_start])
    plt.savefig(example+'_imfR_'+str(imfNum),dpi=200)

    plt.close()

