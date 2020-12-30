from fonctionsTp3 import *
from pylab import rand
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt


def generateData(n):
    """generates a 2D linearly separable dataset with 2n samples.
    returns X an array of 2D samples, and Y the samples label"""
    xb = (rand(n) * 2 - 1) / 2 - 0.5
    yb = (rand(n) * 2 - 1) / 2 + 0.5
    xr = (rand(n) * 2 - 1) / 2 + 0.5
    yr = (rand(n) * 2 - 1) / 2 - 0.5
    inputs = []
    for i in range(n):
        inputs.append([xb[i], yb[i], -1])
        inputs.append([xr[i], yr[i], 1])
    data = np.array(inputs)
    X = data[:, 0:2]
    Y = data[:, -1]
    return X, Y



x,y = generateData2(333)
scatter2d(x,y)
print(np.c_[x,y])
# W = hyperplanSansBiais(np.c_[x,y])
# print(W[0]*W[1])
# print(W[0]/W[1])
# t = np.linspace(-1, 1, 20)
# pl.plot(t, -(W[0]/W[1])*t, color = 'green')
pl.show()


# x,y = generateData2(500)
# print(x,y)
# print("\n\n")
# scatter2d(x,y)
# t = np.linspace(-1, 1, 20)
# pl.show()