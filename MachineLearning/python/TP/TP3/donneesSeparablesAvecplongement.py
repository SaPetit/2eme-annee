#Imports
from fonctionsTp3 import *
from pylab import rand
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt


""" Les fonctions utilisées sont définies dans le fichier fonctionTp3.py"""

x,y = generateData3(200)

scatter2d(x,y)
pl.show()


"""Plongement des données
initialisation"""
i=0
X = x[i][0]
Y = x[i][1]
donees = np.array([[1,X,Y,X*X,X*Y,Y*Y,y[i]]])
i = 1

while i<np.shape(x)[0]:
    donees = np.concatenate((donees,np.array([[1,X,Y,X*X,X*Y,Y*Y,y[i]]])))
    i=i+1
    pass

print(donees)

"""pas besoin de rajouter le biais car le plongement utilisé ajoute déjà une colonne de 1 dans les données"""
W = hyperplanSansBiais(donees)
print(W)