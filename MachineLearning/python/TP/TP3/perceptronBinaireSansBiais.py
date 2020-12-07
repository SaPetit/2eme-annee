#Import de bibliothèques
# from re import S
import numpy as np
import sklearn as sk
import pylab as pl

####################################################Perceptron binaire (sans biais)####################################################

#Entrée : une liste de données d'apprentissage de données à d paramètres étiquettées de façon binaire.
# S = (x_i, y_i) avec x_i ∈ IR^d et y_i ∈ {1, -1}. en python les éléments de S sont de cette forme :[[x_i][y_i]]
#Sortie : Le vecteur de pondération w. vecteur normal de l'hyperplan du perceptron.

#### Implementation.
#0. Initialiser les variables.
d = 10 #dimention des données.
L = 7  #Nombre de données
erreurs = True
# 1. Initialiser le vecteur w = 0 dans IR^d
S = np.zeros(L*(d+1)).reshape(L,d+1)
W = np.zeros(d).reshape(d,1)

X = S[:,0:d-1]
Y = S[-1]
# 2. Répéter
while erreurs == True:
    erreurs = False
    # 3. Pour chaque exemple (xi,yi) ∈ S faire :
    for k in range(0,d):
        # 4. Si yi〈w,xi〉≤0 alors  exemple mal classé
        if  np.vdot(W[k],X[k]) <= 0:
        # 5. Ajuster le plan w:w←w+yixi
            W[k] += X[k]*Y[k]
            erreurs = True
        pass # 6.Fin si
        k += 1 
        pass# 7.Fin pour
    pass # 8.Jusqu'à ce que tous les exemples soient bien classé.
#Renvoyer w
print(W)
