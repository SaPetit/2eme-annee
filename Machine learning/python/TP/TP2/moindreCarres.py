#Algorithme Régression linéaire par moindres carrés

import numpy as np
import pylab as pl
import matplotlib.pyplot as mp

## Inplementation de l'algoritme permettant de recuperer la régression à partir d'une liste de données (x_i,y_i)
import numpy as np

data = np.loadtxt('http://stephane.ayache.perso.luminy.univ-amu.fr/zoom/cours/Cours/AAuto/dataRegLin2D.txt')

def regLin(x,y):
    #ones = np.ones_like(x[0])
    x = np.c_[np.ones(x.shape[0]),x]
    xt = np.transpose(x)
    xtx = np.dot(xt,x)
    inv = np.linalg.inv(xtx)
    xty = np.dot(xt,y)
    return np.dot(inv,xty)

test = regLin(data[:,0:1],data[:,-1])

print(test)
