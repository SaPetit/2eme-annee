#Algorithme Régression linéaire par moindres carrés

from matplotlib.pyplot import subplot
from matplotlib import cm
from sklearn import linear_model
import numpy as np
from numpy.core.multiarray import result_type
import pylab as pl
import matplotlib.pyplot as mp
import math

## Inplementation de l'algoritme permettant de recuperer la régression à partir d'une liste de données (x_i,y_i)

def planEnFonctionVecteurPonderation(sub_plot,W, zOrder = 0):
    """
    Desine le plan normal à W dans la sous figure sub_plot.
    """
    if W.shape[0] == 3:
        a,b,d = W[0], W[1], W[-1]

        x_ = np.linspace(-2,2,10)
        y_ = np.linspace(-2,2,10)

        X_,Y_ = np.meshgrid(x_,y_)
        Z_ = d + a*X_ + b*Y_

        sub_plot.plot_surface(X_, Y_, Z_, cmap=cm.plasma, zorder = zOrder)
        pass
    elif W.shape[0] == 2:
        a,b,d = W[0], W[-1]

        x_ = np.linspace(-1,1,10)
        y_ = np.linspace(-1,1,10)

        X_,Y_ = np.meshgrid(x_,y_)
        Z_ =  a*X_ + b*Y_

        sub_plot.plot_surface(X_, Y_, Z_)
    else:
        print("Le vecteur de ponderation ne comporte pas le bon nombre de paramètrd")
    pass

def rss(vecteurPonderation, X, Y):
    """
    Calcul la somme des moindres carrée (Residual sum of squares).
    ensemble de données X de valeurs Y
    """
    nombreDeValeurs = X.shape[0]
    resultat = 0
    for indice in range(0,nombreDeValeurs):
        valeurPredite = vecteurPonderation[-1] #Biais
        valeurReelle = Y[indice]
        for coef in range(0,vecteurPonderation.shape[0]-1):
            valeurPredite += vecteurPonderation[coef]*X[indice][coef]
        resultat += (valeurPredite - valeurReelle)**2
    return resultat

def mse(vecteurPonderation, X, Y):
    """
    Calcul la moyenne des moindres carrée (mean-square error).
    ensemble de données X de valeurs Y
    """
    resultat = rss(vecteurPonderation, X, Y)/ X.shape[0]
    return resultat

def rmse(vecteurPonderation, X, Y):
    resultat = math.sqrt(mse(vecteurPonderation, X, Y))
    return resultat

def regLin(x,y):
    """
    Regression Linéaire avec biais.
    ensemble de données x de valeurs y
    """
    x = np.c_[x,np.ones(x.shape[0])] #ajout d'une colonne de 1.
    xt = np.transpose(x)
    xtx = np.dot(xt,x)
    inv = np.linalg.inv(xtx)
    xty = np.dot(xt,y)
    return np.dot(inv,xty)

def graphRegLin2d(x,y,a=-5,b=5, imprimer = False, afficherDroite = False, afficherNuageDePoints = False, afficherErreur = False, Tout = False):
    """
    Representation graphique de la régression linéaire avec biais.
    ensemble de données x de valeurs y
    a et b : abscisses min et max du segment représentant l'approximation affine.
    Les parametres booleens imprimer, afficherDroite, afficherErreur, afficherNuageDePoints permette de choisir ce que l'on affiche.
    """
    reg = regLin(x,y)

    if afficherNuageDePoints: pl.scatter(x[:, 0], y)
    if afficherDroite : pl.plot([a, b],[reg[1] + a*reg[0], reg[1] + b*reg[0]],'r--', lw=2)
    if afficherErreur : print(mse(reg,x,y)) 
    if imprimer: pl.show()

def graphRegLin3d(x,y,a=-5,b=5, imprimer = False, afficherDroite = False, afficherNuageDePoints = False, afficherErreur = False):
    """
    Representation graphique de la régression linéaire 3d avec biais.
    ensemble de données x de valeurs y
    Les parametres booleens imprimer, afficherDroite, afficherErreur, afficherNuageDePoints permette de choisir ce que l'on affiche.
    """
    fig = pl.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    regressionLineaire = regLin(x,y)
    if afficherNuageDePoints: ax.scatter(x[:,0], x[:,1], y, s=50 )
    if afficherDroite :planEnFonctionVecteurPonderation(ax, regressionLineaire, zOrder = 2)
    if afficherErreur : print(mse(regressionLineaire,x,y)) 
    if imprimer: pl.show()

def graphRegLin(x,y, a=-5,b=-5,imprimer = False, afficherDroite = False, afficherNuageDePoints = False, afficherErreur = False, Tout = False):
    if Tout: imprimer, afficherDroite, afficherErreur, afficherNuageDePoints = True, True, True, True
    if x.shape[1] == 1:graphRegLin2d(x,y,a=a,b=b, imprimer = imprimer, afficherDroite = afficherDroite, afficherNuageDePoints = afficherNuageDePoints, afficherErreur = afficherErreur)
    if x.shape[1] == 2:graphRegLin3d(x,y, imprimer = imprimer, afficherDroite = afficherDroite, afficherNuageDePoints = afficherNuageDePoints, afficherErreur = afficherNuageDePoints)






