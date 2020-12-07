from pylab import rand
import pylab as pl
import numpy as np

def generateData(n):
    """generates a 2D linearly separable dataset with 2n samples.
    returns X an array of 2D samples, and Y the samples label"""
    xb = (rand(n) * 2 - 1) / 2 - 0.5
    yb = (rand(n) * 2 - 1) / 2 + 0.5
    xr = (rand(n) * 2 - 1) / 2 + 0.5
    yr = (rand(n) * 2 - 1) / 2 - 0.5
    inputs = []
    for i in range(n):
        inputs.append([xb[i], yb[i], -1])
        inputs.append([xr[i], yr[i], 1])
    data = np.array(inputs)
    X = data[:, 0:2]
    Y = data[:, -1]
    return X, Y


def generateData2(n):
    """generates a 2D linearly separable dataset with 2n samples.
    returns X an array of 2D samples, and Y the samples label"""
    xb = (rand(n) * 2 - 1) / 2 + 0.5
    yb = (rand(n) * 2 - 1) / 2
    xr = (rand(n) * 2 - 1) / 2 + 1.5
    yr = (rand(n) * 2 - 1) / 2 - 0.5
    inputs = []
    for i in range(n):
        inputs.append([xb[i], yb[i], -1])
        inputs.append([xr[i], yr[i], 1])
    data = np.array(inputs)
    X = data[:, 0:2]
    Y = data[:, -1]
    return X, Y
     

def scatter2d(X,Y):
    """
    Representation graphique de la régression linéaire avec biais.
    ensemble de données x de valeurs y
    a et b : abscisses min et max du segment représentant l'approximation affine.
    Les parametres booleens imprimer, afficherDroite, afficherErreur, afficherNuageDePoints permette de choisir ce que l'on affiche.
    """
    pl.scatter(X[Y==-1][:, 0],X[Y==-1][:,1],color="red")

    pl.scatter(X[Y==1][:, 0],X[Y==1][:, 1],color="blue")



#Import de bibliothèques
# from re import S
import numpy as np
import sklearn as sk
import pylab as pl

def hyperplanSansBiais(donnees_Etiquetees):
    #Entrée : une liste de données d'apprentissage de données à d paramètres étiquettées de façon binaire.
    # S = (x_i, y_i) avec x_i ∈ IR^d et y_i ∈ {1, -1}. en python les éléments de S sont de cette forme :[[x_i][y_i]]
    #Sortie : Le vecteur de pondération w. vecteur normal de l'hyperplan du perceptron.

    #### Implementation.
    #0. Initialiser les variables.
    d = donnees_Etiquetees.shape[1]-1 #dimention des données.
    L = donnees_Etiquetees.shape[0]  #Nombre de données
    erreurs = True
    # 1. Initialiser le vecteur w = 0 dans IR^d
    W = np.zeros(d)


    X = donnees_Etiquetees[:,0:d]
    Y = donnees_Etiquetees[:,-1]
    k=0
    # 2. Répéter
    while erreurs == True:
        erreurs = False
        # 3. Pour chaque exemple (xi,yi) ∈ S faire :
        for k in range(0,L):
            # 4. Si yi〈w,xi〉≤0 alors  exemple mal classé
            #print(W,"\n",X[k],"\n",np.vdot(W,X[k]))
            val =Y[k]*np.vdot(W,X[k])
            if  val <= 0:
            # 5. Ajuster le plan w:w←w+yixi
                W += X[k]*Y[k]
                erreurs = True
            pass # 6.Fin si
            k += 1 
            pass# 7.Fin pour
        pass # 8.Jusqu'à ce que tous les exemples soient bien classé.
    #Renvoyer w
    print(W)
    return W