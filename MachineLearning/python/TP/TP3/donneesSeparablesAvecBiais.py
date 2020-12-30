#Imports
import matplotlib.pyplot as plt
import numpy as np
import pylab as pl
from pylab import rand

from fonctionsTp3 import *

""" Les fonctions utilisées sont définies dans le fichier fonctionTp3.py"""

x,y = generateData2(200)
scatter2d(x,y)

""" On complète les données avec une collone de 1 afin de pouvoir gerer le biais et obtenir un hyperplan (ici une drssoite) affine"""
x = np.c_[x,np.ones(x.shape[0])]

W = hyperplanSansBiais(np.c_[x,y])
print(W)
t = np.linspace(0, 2, 2)
pl.plot(t, -(W[0]/W[1])*t-W[-1]/W[1], color = 'green')
pl.show()
