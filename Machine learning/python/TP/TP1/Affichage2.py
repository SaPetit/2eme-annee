
##Exercice 1.2
#Chargement du jeude de données.
from sklearn.datasets import load_iris
irisData=load_iris()

import pylab as pl # permet de remplacer le nom "pylab" par "pl"
X=irisData.data
Y=irisData.target
x = 0
y = 1

pl.scatter(X[Y==0][:, x],X[Y==0][:,y],
color="red",label=irisData.target_names[0])
pl.scatter(X[Y==1][:, x],X[Y==1][:, y],
color="green",label=irisData.target_names[1])
pl.scatter(X[Y==2][:, x],X[Y==2][:, y],
color="blue",label=irisData.target_names[2])
pl.legend()

pl.show()



#Deuxième méthode d'affichage de données
