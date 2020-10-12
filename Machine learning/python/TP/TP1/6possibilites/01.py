
##Exercice 1.2
#Chargement du jeude de données.
from sklearn.datasets import load_iris
irisData=load_iris()

import pylab as pl # permet de remplacer le nom "pylab" par "pl"
X=irisData.data
Y=irisData.target
x = 0
y = 1

pl.scatter(X[:, x], X[:, y],c=Y) # Creation du nuage de point.
pl.xlabel(irisData.feature_names[x]) #Etiquettage des axes du repère.
pl.ylabel(irisData.feature_names[y])
pl.show()

