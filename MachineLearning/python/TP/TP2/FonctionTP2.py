#Algorithme Régression linéaire par moindres carrés

import numpy as np
import pylab as pl
import matplotlib.pyplot as mp

## Inplementation de l'algoritme permettant de recuperer la régression à partir d'une liste de données (x_i,y_i)
import numpy as np

data = np.loadtxt('http://stephane.ayache.perso.luminy.univ-amu.fr/zoom/cours/Cours/AAuto/dataRegLin2D.txt')

def regLin(x,y):
    x = np.c_[x,np.ones(x.shape[0])]
    xt = np.transpose(x)
    xtx = np.dot(xt,x)
    inv = np.linalg.inv(xtx)
    xty = np.dot(xt,y)
    return np.dot(inv,xty)


def graphRegLin2d(x,y,a,b, print = True, afficherErreurDroiteErreur = True, afficherErreurDroiteNuageDePoints = True, afficherErreurDroiteErreurDroite = True):
    reg = regLin(x,y)

    if afficherErreurDroiteNuageDePoints: pl.scatter(x[:, 0], y)
    if afficherErreurDroiteErreurDroite: pl.plot([a, b],[reg[1] + a*reg[0], reg[1] + b*reg[0]],'r--', lw=2)
    if print: pl.show()

def graphRegLin3d(x,y,a,b, print = True, erreur = True, nuageDePoints = True, droite = True):
    return print("L'affichage d'un nuage de points en 3d doit etre implementée")

def graphRegLin(x,y,a,b, print = True, erreur = True, nuageDePoints = True, droite = True):
    if x.shape[1] == 1:graphRegLin2d(x,y,a,b, print = True, erreur = True, nuageDePoints = True, droite = True)
    if x.shape[1] == 2:graphRegLin3d(x,y,a,b, print = True, erreur = True, nuageDePoints = True, droite = True)



