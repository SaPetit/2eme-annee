from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('http://stephane.ayache.perso.luminy.univ-amu.fr/zoom/cours/Cours/AAuto/dataRegLin2D.txt')

fig = plt.figure()
fig = 


x =data[:,0]
y =data[:,1]
z =data[:,2]



ax.scatter(x, y, z, c='r', marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
