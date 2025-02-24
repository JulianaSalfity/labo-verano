# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 09:28:32 2025

@author: Adrian
"""

from pathlib import Path
import pandas as pd
import duckdb as dd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import numpy as np

carpeta = Path.cwd() 

arboles = pd.read_csv(carpeta /"arboles.csv")
arboles.columns


plot1 = sns.histplot(data = arboles, x = 'altura_tot', hue = 'nombre_com',bins = 17, palette = 'turbo')
plt.show()
plot2 = sns.histplot(data = arboles, x = 'diametro', hue = 'nombre_com', bins = 17, palette = 'turbo')
plt.show()
plot3 = sns.histplot(data = arboles, x = 'inclinacio', hue = 'nombre_com', bins = 17 ,palette = 'turbo')
plt.show()

sns.scatterplot(data=arboles, x="diametro",y="altura_tot",hue="nombre_com",
                palette='turbo',alpha=0.7, s=80)
     
plt.grid(True,alpha = 0.5) 
plt.show()

#%% Árbol 1

X = arboles[['altura_tot', 'diametro', 'inclinacio']]  # Características
y = arboles['nombre_com']  # Etiqueta

arbol_1 = DecisionTreeClassifier(max_depth=3)
arbol_1.fit(X, y)  # Entrenamiento del modelo


predicciones = arbol_1.predict(X)  # Generamos las predicciones

# Visualizar el árbol de decisión
tree.plot_tree(arbol_1, feature_names=X.columns, class_names=['J','C','E','P'], filled=True, rounded=True, fontsize=4)
plt.title('Árbol de Decisión 1')
plt.show()

X = arboles[['altura_tot', 'inclinacio']]  # Características
y = arboles['nombre_com']  # Etiqueta

arbol_2 = DecisionTreeClassifier(max_depth=3)
arbol_2.fit(X, y)  # Entrenamiento del modelo


predicciones = arbol_2.predict(X)  # Generamos las predicciones

# Visualizar el árbol de decisión
tree.plot_tree(arbol_2, feature_names=X.columns, class_names=['J','C','E','P'], filled=True, rounded=True, fontsize=4)
plt.title('Árbol de Decisión 2')
plt.show()
