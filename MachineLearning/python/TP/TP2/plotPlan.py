from FonctionTP2 import regLin
import numpy as np
import matplotlib.pyplot as pl
from mpl_toolkits.mplot3d import Axes3D

a,b,c,d = reg[0], reg[1], 1, reg[-1]

x = np.linspace(-1,1,10)
y = np.linspace(-1,1,10)

X,Y = np.meshgrid(x,y)
Z = (d + a*X + b*Y) / c

ax = pl.gca(projection='3d')

surf = ax.plot_surface(X, Y, Z)

pl.show()