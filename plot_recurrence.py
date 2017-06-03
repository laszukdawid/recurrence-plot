#!/usr/bin/python
# coding: UTF-8
from __future__ import division, print_function
import numpy as np
import pylab as plt
from scipy.spatial.distance import pdist, squareform

def rec_plot(s, eps=0.10, steps=10):
    d = pdist(s[:,None])
    d = np.floor(d/eps)
    d[d>steps] = steps
    Z = squareform(d)
    return Z

def moving_average(s, r=5):
    return np.convolve(s, np.ones((r,))/r, mode='valid')

if __name__ == "__main__":
    # Generate singal
    N = 200
    eps = 0.1
    steps = 10

    # Plot unifrom dist filtered with moving average
    ru = np.random.uniform(low=-1, high=1, size=N)
    ru_filtered = moving_average(ru)

    plt.title("Normal")
    plt.subplot(221)
    plt.plot(ru_filtered)
    plt.title("Unitary")
    plt.subplot(223)
    plt.imshow(rec_plot(ru_filtered, eps=eps, steps=steps))

    # Plot normal dist filtered with moving average
    rn = np.random.normal(size=N)
    rn_filtered = moving_average(rn)

    plt.subplot(222)
    plt.plot(rn_filtered)
    plt.title("Normal")
    plt.subplot(224)
    plt.imshow(rec_plot(rn_filtered, eps=eps, steps=steps))

    plt.show()
