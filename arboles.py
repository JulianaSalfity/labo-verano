#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 10:36:37 2025

@author: Estudiante
"""


from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Cargar el conjunto de datos Titanic
carpeta = Path.cwd()
titanic = pd.read_csv(carpeta / 'titanic_training.csv')

titanic.columns

X = titanic[['Age', 'Pclass']]  # Características
y = titanic['Survived']  # Etiqueta

arbol = DecisionTreeClassifier(max_depth=3)
arbol.fit(X, y)  # Entrenamiento del modelo


predicciones = arbol.predict(X)  # Generamos las predicciones

# Visualizar el árbol de decisión
tree.plot_tree(arbol, feature_names=X.columns, class_names=['No', 'Yes'], filled=True, rounded=True, fontsize=4)
plt.title('Árbol de Decisión Entrenado')

#r = tree. ver escrito





#%%
from sklearn.datasets import load_iris
# Cargar el conjunto de datos Iris
iris = load_iris()
X = iris.data  # Características (features)
y = iris.target  # Etiquetas (labels)

# Crear y entrenar el modelo de árbol de decisión
arbol = DecisionTreeClassifier()
arbol.fit(X, y)  # Entrenamiento del modelo

# Realizar predicciones
predicciones = arbol.predict(X)  # Generamos las predicciones

# Mostrar las primeras 10 predicciones
print(predicciones[:10])

# Visualizar el árbol de decisión
plt.figure(figsize=(15, 10))
tree.plot_tree(arbol, filled=True, feature_names=iris.feature_names, class_names=iris.target_names, rounded=True)
plt.title('Árbol de Decisión Entrenado')
plt.show()

#%%
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn import  metrics


iris = load_iris()
data = iris.frame
X = iris.data  # Características (features)
Y = iris.target 
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X, Y)
Y_pred = model.predict(X)


print('Exacitud modelo',metrics.accuracy_score(Y, Y_pred))

metrics.confusion_matrix(Y, Y_pred)

#%%

from sklearn.model_selection import train_test_split 

X_train, X_test, Y_train, Y_test= train_test_split(X,Y,test_size =0.3)

model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, Y_train)
Y_pred = model.predict(X_test)
print('Exacitud modelo',metrics.accuracy_score(Y_test, Y_pred))

metrics.confusion_matrix(Y_test, Y_pred)

