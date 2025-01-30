# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 19:37:31 2025

@author: Adrian
"""

import csv
import pandas as pd

nombre_archivo_veredas = r'C:\Users\Adrian\Downloads\arbolado-publico-lineal-2017-2018.csv' 
df_veredas = pd.read_csv(nombre_archivo_veredas)
print(df.columns)

df_veredas[['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho',
'altura_arbol']]

print(df)

nombre_archivo_parque = r'C:\Users\Adrian\Downloads\arbolado-en-espacios-verdes.csv'
df_parques = pd.read_csv(nombre_archivo_parque)