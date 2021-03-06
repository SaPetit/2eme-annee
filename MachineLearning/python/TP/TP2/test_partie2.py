from matplotlib.pyplot import plot
import numpy as np
import pylab as pl
from sklearn import linear_model, datasets
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV, train_test_split
import matplotlib.pyplot as mp

__ARRONDIE__ = 2 #Variable globale qui determine à combien les valeur affichées sont arrondies, on n'arrondie pas les valeurs dans les calculs.

def prediction(model, ensemble):
    """
    Renvoie un ensemble de valeurs prédites pour l'ensemble donné par le model donné.
    """
    result = model.predict(ensemble)
    return result

def erreurSkl(valeursReelles , valeursPredites):
    """
    Renvoie l'erreur mse du model étant donnés un ensemble de valeurs prédites et un ensemble de valeur réelles.

    """
    result = mean_squared_error(valeursReelles , valeursPredites)
    return result

def vecteurPond(modele):
    """
    Renvoie le vecteur de ponderation d'un modèle.
    """
    result = np.concatenate([modele.coef_, [modele.intercept_]])
    return result

def arrondie(a):
    result = np.round(a, decimals=__ARRONDIE__)
    return result


def ridgeLasso(donnees, etiquettes, plage_debut, plage_fin, nb_de_valeurs):
    alphas = np.logspace(plage_debut, plage_fin, nb_de_valeurs)
    for Model in [linear_model.Ridge, linear_model.Lasso]:
        gscv = GridSearchCV(Model(), dict(alpha=alphas), cv=5).fit(donnees, etiquettes)

        best_model = Model(alpha = gscv.best_params_.get("alpha"))
        best_model.fit(donnees, etiquettes)
        pred_best_model = best_model.predict(donnees)
        erreur_best_model = erreurSkl(etiquettes,pred_best_model)
        print(Model.__name__, gscv.best_params_, " score ", erreur_best_model)

def ridgeLassoAvecSplit(donnees_train, etiquettes_train, donnees_test, etiquettes_test, plage_debut, plage_fin, nb_de_valeurs):
    alphas = np.logspace(plage_debut, plage_fin, nb_de_valeurs)
    for Model in [linear_model.Ridge, linear_model.Lasso]:
        gscv = GridSearchCV(Model(), dict(alpha=alphas), cv=5).fit(donnees_train, etiquettes_train)

        best_model = Model(alpha = gscv.best_params_.get("alpha"))
        best_model.fit(donnees_train, etiquettes_train)
        pred_best_model = best_model.predict(donnees_test)
        erreur_best_model = erreurSkl(etiquettes_test,pred_best_model)
        print(Model.__name__, gscv.best_params_, " score ", erreur_best_model)



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
vecteurPonderation = vecteurPond(modeleX)

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
donnees_diabetes, etiquettes_reelles_diabetes = datasets.load_diabetes(return_X_y=True)

#Import des données boston
print("Import des données boston")
donnees_boston, etiquettes_reelles_boston = datasets.load_boston(return_X_y=True)

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
vecteurPonderation_boston_global = vecteurPond(modele_boston)

print("////Analyse de boston\n")

for colonne in range(0,donnees_boston.shape[1]):
    mod = linear_model.LinearRegression()
    data = donnees_boston[:,colonne:colonne+1]
    mod.fit(data, etiquettes_reelles_boston)
    pred = prediction(mod, data)
    erreur = erreurSkl(etiquettes_reelles_boston,pred)

    print("Suivant le parametre ", colonne, " l'erreur vaut ", arrondie(erreur))
    pass

print("\nSuivant tous les parametres l'erreur pour boston vaut ", arrondie(erreur_globale_boston), ".\n\n")

print("////Analyse de diabetes\n")

for colonne in range(0,donnees_diabetes.shape[1]):
    mod = linear_model.LinearRegression()
    data = donnees_diabetes[:,colonne:colonne+1]
    mod.fit(data, etiquettes_reelles_diabetes)
    pred = mod.predict(data)
    erreur = erreurSkl(etiquettes_reelles_diabetes,pred)

    print("Suivant le parametre ", colonne, " l'erreur vaut ", arrondie(erreur))
    pass

print("\nSuivant tous les parametres l'erreur pour diabetes vaut ", arrondie(erreur_globale_diabetes), ".\n")



############   Ridge et Lasso

print("//////////Avec Regularisation : Ridge et Lasso.\n\n")
print("////////Ridge.\n")
print("//boston.\n")


ridge_boston_1 = linear_model.Ridge(alpha = 1.0)
ridge_boston_1.fit(donnees_boston, etiquettes_reelles_boston)
pred_ridge_boston_1 = ridge_boston_1.predict(donnees_boston)
erreur_ridge_boston_1 = erreurSkl(etiquettes_reelles_boston,pred_ridge_boston_1)
vect_ridge_boston_1 = vecteurPond(ridge_boston_1)

print("Pour boston, Ridge avec alpha = 1 l'erreur est de ", arrondie(erreur_ridge_boston_1), ".\n\n\nLe vecteur de ponderation est : \n\n", arrondie(vect_ridge_boston_1))


print("//diabetes.\n")


ridge_diabetes_1 = linear_model.Ridge(alpha = 1.0)
ridge_diabetes_1.fit(donnees_diabetes, etiquettes_reelles_diabetes)
pred_ridge_diabetes_1 = ridge_diabetes_1.predict(donnees_diabetes)
erreur_ridge_diabetes_1 = erreurSkl(etiquettes_reelles_diabetes,pred_ridge_diabetes_1)
vect_ridge_diabetes_1 = vecteurPond(ridge_boston_1)

print("Pour diabetes, Ridge avec alpha = 1 l'erreur est de ", arrondie(erreur_ridge_diabetes_1), ".\n\n\nLe vecteur de ponderation est : \n\n", arrondie(vect_ridge_diabetes_1))





print("\n////////Lasso.\n")
print("//boston.\n")


Lasso_boston_1 = linear_model.Lasso(alpha = 1.0)
Lasso_boston_1.fit(donnees_boston, etiquettes_reelles_boston)
pred_Lasso_boston_1 = Lasso_boston_1.predict(donnees_boston)
erreur_Lasso_boston_1 = erreurSkl(etiquettes_reelles_boston,pred_Lasso_boston_1)
vect_Lasso_boston_1 = vecteurPond(Lasso_boston_1)
print("Pour boston, Lasso avec alpha = 1 l'erreur est de ", arrondie(erreur_Lasso_boston_1), ".\n\n\nLe vecteur de ponderation est : \n\n", arrondie(vect_Lasso_boston_1))


print("//diabetes.\n")


Lasso_diabetes_1 = linear_model.Lasso(alpha = 1.0)
Lasso_diabetes_1.fit(donnees_diabetes, etiquettes_reelles_diabetes)
pred_Lasso_diabetes_1 = Lasso_diabetes_1.predict(donnees_diabetes)
erreur_Lasso_diabetes_1 = erreurSkl(etiquettes_reelles_diabetes,pred_Lasso_diabetes_1)
vect_Lasso_diabetes_1 = vecteurPond(Lasso_diabetes_1)


print("Pour diabetes, Lasso avec alpha = 1 l'erreur est de ", arrondie(erreur_Lasso_diabetes_1), ".\n\n\nLe vecteur de ponderation est : \n\n", arrondie(vect_Lasso_diabetes_1))

print("\nConclision : Avec alpha = 1 Ridge et Lasso sont moins bons qu'une régression linéaire simple.\n" +
"Beacoup de zéros dans le vecteur de ponderation avec Lasso.\n" +
"Nous allons tenter de trouver un meilleur hyperparamètre par validation croisé.\n\n")

print("Regulation ridge et lasso pour boston.\n")

ridgeLasso(donnees_boston, etiquettes_reelles_boston, -5,1,200)

print("\n\n")
print("Regulation ridge et lasso pour diabetes.\n")

ridgeLasso(donnees_diabetes, etiquettes_reelles_diabetes,-5,1,200)

#print("\n\nListe des alphas testés :\n",alphas, "\n\n")

print("\nConclision : Avec une régulation Ridge ou lasso l'erreur est legerement moins bonne mais elles permettent un compromis entre erreur et complexité du modèle\n")

### Séparation entre ensemble d'entrainement et ensemble de test

print("Séparation entre ensemble d'entrainement et ensemble de test\n")


donnees_train_boston, donnees_test_boston, etiquette_train_boston, etiquette_test_boston, = train_test_split(donnees_boston, etiquettes_reelles_boston, test_size=0.33, random_state=42)

donnees_train_diabetes, donnees_test_diabetes, etiquette_train_diabetes, etiquette_test_diabetes, = train_test_split(donnees_diabetes, etiquettes_reelles_diabetes, test_size=0.33, random_state=42)

print("Regulation ridge et lasso pour boston avec split.\n")

ridgeLassoAvecSplit(donnees_train_boston, etiquette_train_boston, donnees_test_boston,etiquette_test_boston, -5,1,200)

print("\n\n")
print("Regulation ridge et lasso pour diabetes avec split.\n")

ridgeLassoAvecSplit(donnees_train_diabetes, etiquette_train_diabetes, donnees_test_diabetes, etiquette_test_diabetes,-5,1,200)