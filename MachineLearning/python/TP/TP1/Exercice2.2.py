
##Exercice 2.1
#Chargement du jeude de données.
from sklearn.datasets import load_iris
irisData=load_iris()

from sklearn import neighbors

X=irisData.data
Y=irisData.target

from sklearn.model_selection  import train_test_split

# ou from sklearn.model_selection import train_test_split
import random # pour pouvoir utiliser un g´en´erateur de nombres aléatoires
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3,random_state=random.seed())
help(train_test_split)
len(X_train)
len(X_test)
