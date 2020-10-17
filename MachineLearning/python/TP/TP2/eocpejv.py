from matplotlib.pyplot import plot
import numpy as np
import pylab as pl
import matplotlib.pyplot as mp
from sklearn.linear_model import LinearRegression
from FonctionTP2 import *

data = np.loadtxt('http://stephane.ayache.perso.luminy.univ-amu.fr/zoom/cours/Cours/AAuto/dataRegLin2D.txt')

X = data[:,0:2]
Y = data[:,-1]

reg = LinearRegression().fit(X, Y)


print("\n\n\n")
#print(X)
print(regLin(X,Y))
print("\n\n\n")
graphRegLin(X,Y)