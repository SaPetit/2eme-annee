# -*- coding: utf-8 -*-

##Exercice 1.2
#Chargement du jeude de données.
from sklearn.datasets import load_iris
irisData=load_iris()

import pylab as pl # permet de remplacer le nom "pylab" par "pl"
X=irisData.data
Y=irisData.target
x = 0
y = 1

colors=[’red’,’green’,’blue’]
for i in range(3):
    pl.scatter(X[Y==i][:, x],X[Y==i][:,y],color=colors[i],\
        label=irisData.target_names[i])
pl.legend()
pl.xlabel(irisData.feature_names[x])
pl.ylabel(irisData.feature_names[y])
pl.title("Donnees Iris - dimension des s´epales uniquement")
pl.show()



#3eme méthode d'affichage de données
