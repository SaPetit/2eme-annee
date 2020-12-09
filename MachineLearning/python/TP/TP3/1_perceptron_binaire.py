#Imports
from fonctionsTp3 import *
from pylab import rand
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt


""" Les fonctions utilisées sont définies dans le fichier fonctionTp3.py"""

x,y = generateData(20)
scatter2d(x,y)
W = hyperplanSansBiais(np.c_[x,y])
t = np.linspace(-1, 1, 20)
pl.plot(t, -(W[0]/W[1])*t, color = 'green')
pl.show()