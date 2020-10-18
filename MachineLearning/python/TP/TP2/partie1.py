from matplotlib.pyplot import plot
import numpy as np
import pylab as pl
import matplotlib.pyplot as mp
from FonctionTP2 import *

data = np.loadtxt('http://stephane.ayache.perso.luminy.univ-amu.fr/zoom/cours/Cours/AAuto/dataRegLin2D.txt')

X = data[:,0:2]
X_0 = data[:,0:1]
X_1 = data[:,1:2]
Y = data[:,-1]

print("\nVecteur de ponderation :\n", regLin(X,Y))
print("\nErreur de regression lineaire selon la premiere coordonnée :")
graphRegLin(X_0,Y, a=-3,b=3, Tout = True)
print("\nErreur de regression lineaire selon la seconde coordonnée :")
graphRegLin(X_1,Y, a=-3,b=3, Tout = True)
print("\nErreur de regression lineaire selon les 2 coordonnées :")
graphRegLin(X,Y, Tout = True)