from logging import fatal
from operator import truediv
from matplotlib.pyplot import plot
import numpy as np
import pylab as pl
import matplotlib.pyplot as mp

data = np.loadtxt('http://stephane.ayache.perso.luminy.univ-amu.fr/zoom/cours/Cours/AAuto/dataRegLin2D.txt')
## Inplementation de l'algoritme permettant de recuperer la régression à partir d'une liste de données (x_i,y_i)

def regLin(x,y):

    x = np.c_[x,np.ones(x.shape[0])]
    xt = np.transpose(x)
    xtx = np.dot(xt,x)
    inv = np.linalg.inv(xtx)
    xty = np.dot(xt,y)
    return np.dot(inv,xty)

def graphRegLin2d(x,y,a,b, print = True, erreur = True, nuageDePoints = True, droite = True):
    reg = regLin(x,y)

    if nuageDePoints: pl.scatter(x[:, 0], y)
    if droite: pl.plot([a, b],[reg[1] + a*reg[0], reg[1] + b*reg[0]],'r--', lw=2)
    if print: pl.show()

print(regLin(data[:,0:1],data[:,-1]))
graphRegLin(data[:,0:1],data[:,-1],-3,3)

