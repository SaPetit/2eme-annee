from matplotlib.pyplot import plot
import numpy as np
import pylab as pl
from sklearn import linear_model, datasets
import matplotlib.pyplot as mp
import sklearn
from FonctionTP_sklearn import *


print("///////////////TP-2Partie 2\n\n")
print("////Donées factices\n")


#Chargement des données
data = np.loadtxt('http://stephane.ayache.perso.luminy.univ-amu.fr/zoom/cours/Cours/AAuto/dataRegLin2D.txt')
X = data[:,0:2]
X_0 = data[:,0:1]
X_1 = data[:,1:2]
Y = data[:,-1]

#Creation de du régresseur
print("Entrainement des modèles")
modeleX_0 = linear_model.LinearRegression()
modeleX_0.fit(X_0,Y)

modeleX_1 = linear_model.LinearRegression()
modeleX_1.fit(X_1,Y)

modeleX = linear_model.LinearRegression()
modeleX.fit(X,Y)
vecteurPonderation = np.concatenate([modeleX.coef_, [modeleX.intercept_]])

#Prediction suivant le modele
print("Prediction suivant le modele")
X_predit = prediction(modeleX,X)
X_0_predit = prediction(modeleX_0,X_0)
X_1_predit = prediction(modeleX_1,X_1)


print("\nVecteur de ponderation :\n", vecteurPonderation)
print("\nErreur de regression lineaire skl selon la premiere coordonnée :")
#graphRegLin(X_0,Y, a=-3,b=3, Tout = True)
print(erreurSkl(Y,X_0_predit))
print("\nErreur de regression lineaire skl selon la seconde coordonnée :")
#graphRegLin(X_1,Y, a=-3,b=3, Tout = True)
print(erreurSkl(Y,X_1_predit))
print("\nErreur de regression lineaire skl selon les 2 coordonnées :")
#graphRegLin(X,Y, Tout = True)
print(erreurSkl(Y,X_predit))


""" boston et diabetes """

#Import des données diabetes
print("\nImport des données diabetes")
donnees_diabetes, etiquettes_reelles_diabetes = sklearn.datasets.load_diabetes(return_X_y=True)

#Import des données boston
print("Import des données boston")
donnees_boston, etiquettes_reelles_boston = sklearn.datasets.load_boston(return_X_y=True)

#Creation de du régresseur diabetes
print("Entrainement du modèle diabetes")
modele_diabetes = linear_model.LinearRegression()
modele_diabetes.fit(donnees_diabetes,etiquettes_reelles_diabetes)

#Creation de du régresseur boston
print("Entrainement du modèle boston")
modele_boston = linear_model.LinearRegression()
modele_boston.fit(donnees_boston,etiquettes_reelles_boston)

#Prediction suivant les modeles
print("Prediction suivant les modeles")
predit_diabetes = prediction(modele_diabetes,donnees_diabetes)
predit_boston = prediction(modele_boston,donnees_boston)

#Prediction suivant les modeles
print("Prediction suivant les modeles\n\n")
predit_diabetes = prediction(modele_diabetes,donnees_diabetes)
predit_boston = prediction(modele_boston,donnees_boston)

erreur_globale_boston = erreurSkl(etiquettes_reelles_boston,predit_boston)
erreur_globale_diabetes = erreurSkl(etiquettes_reelles_diabetes,predit_diabetes)

print("////Analyse de boston\n")

for colonne in range(0,donnees_boston.shape[1]):
    mod = linear_model.LinearRegression()
    data = donnees_boston[:,colonne:colonne+1]
    mod.fit(data, etiquettes_reelles_boston)
    pred = mod.predict(data)
    erreur = erreurSkl(etiquettes_reelles_boston,pred)

    print("Suivant le parametre ", colonne, " l'erreur vaut ", erreur)
    pass

print("\nSuivant tous les parametres l'erreur pour boston vaut ", erreur_globale_boston, ".\n\n")


print("////Analyse de diabetes\n")

for colonne in range(0,donnees_diabetes.shape[1]):
    mod = linear_model.LinearRegression()
    data = donnees_diabetes[:,colonne:colonne+1]
    mod.fit(data, etiquettes_reelles_diabetes)
    pred = mod.predict(data)
    erreur = erreurSkl(etiquettes_reelles_diabetes,pred)

    print("Suivant le parametre ", colonne, " l'erreur vaut ", erreur)
    pass

print("\nSuivant tous les parametres l'erreur pour diabetes vaut ", erreur_globale_diabetes, ".\n")

print("//////////Avec Regularisation : Ridge et Lasso.\n\n")

ridge_boston_1 = linear_model.Ridge(alpha = 1.0)
