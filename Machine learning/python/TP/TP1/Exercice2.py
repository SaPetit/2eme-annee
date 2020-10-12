
##Exercice 2.1
#Chargement du jeude de données.
from sklearn.datasets import load_iris
irisData=load_iris()

from sklearn import neighbors
nb_voisins = 15
X=irisData.data
Y=irisData.target

classifieur = neighbors.KNeighborsClassifier(nb_voisins) #création du classifieur en fonction de son ou ses méthaparametres.

classifieur.fit(X, Y)

print(classifieur.predict([[ 5.4, 3.2, 1.6, 0.4]]))                    #Renvoie une etiquette
print(classifieur.predict_proba([[ 5.4, 3.2, 1.6, 0.4]]))              #Renvoie une liste donnant une probabilité d'apparition par étiquette.
print(classifieur.score(X,Y))
Z = classifieur.predict(X) #renvoie la liste des Données pour lesquelles le classifieur prédit la bonne
print(X[Z!=Y])
