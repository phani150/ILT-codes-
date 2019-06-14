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
x,y= iris.data,iris.target
classifier=KNeighborsClassifier()


#print (iris.data.shape)
#print (iris.feature_names)
#print (iris.target_names)
#print (type(iris))
#sys.exit()

