##Importing the needed modules
import sys
import os
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.datasets import load_iris,load_digits
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv(url, names=names)

iris=load_iris()
X,y= iris.data,iris.target
classifier=KNeighborsClassifier()

train_X,test_X,train_y,test_y= \
    train_test_split(X,y,train_size=0.5,random_state=12)
print ("Labels for training and testing")
print (test_y)
print (train_y)


#print (iris.data.shape)
#print (iris.feature_names)
#print (iris.target_names)
print (type(iris))
#sys.exit()

