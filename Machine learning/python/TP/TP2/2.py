import numpy as np
data = np.loadtxt('http://stephane.ayache.perso.luminy.univ-amu.fr/zoom/cours/Cours/AAuto/dataRegLin2D.txt')
import pylab as pl # permet de remplacer le nom "pylab" par "pl"
#Algorithme Régression linéaire par moindres carrés

import numpy as np
import pylab as pl
import matplotlib.pyplot as mp

## Inplementation de l'algoritme permettant de recuperer la régression à partir d'une liste de données (x_i,y_i)
import numpy as np

def regLin(x,y):

    x = np.c_[x,np.ones(x.shape[0])]
    xt = np.transpose(x)
    xtx = np.dot(xt,x)
    inv = np.linalg.inv(xtx)
    xty = np.dot(xt,y)
    return np.dot(inv,xty)

regression = regLin(data[:,1:2],data[:,-1])
X= data
Y=data[:,-1]
x = 0
y = 1

pl.scatter(X[:, 0], Y) # Creation du nuage de point.
pl.plot([x1, x2],[y1, y2])

pl.show()


def graphRegLin(x,y):
    def regLin(x,y):

        x = np.c_[x,np.ones(x.shape[0])]
        xt = np.transpose(x)
        xtx = np.dot(xt,x)
        inv = np.linalg.inv(xtx)
        xty = np.dot(xt,y)
        return np.dot(inv,xty) 
    reg = regLin(x,y)
    pl.scatter(x[:, 0], y)
    pl.show()


    def regLin(x,y):

        x = np.c_[x,np.ones(x.shape[0])]
        xt = np.transpose(x)
        xtx = np.dot(xt,x)
        inv = np.linalg.inv(xtx)
        xty = np.dot(xt,y)
        return np.dot(inv,xty) 

