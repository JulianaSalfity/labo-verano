# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 13:08:57 2025

@author: Adrian
"""

import pandas as pd
import duckdb as dd
import matplotlib.pyplot as plt
import numpy as np
import seaborn 

data_ping = seaborn.load_dataset('penguins')

data_ping.columns
data_ping.shape

species = dd.sql("""
                 SELECT DISTINCT species
                 FROM data_ping""").df()
island = dd.sql("""
                 SELECT DISTINCT island
                 FROM data_ping""").df()
                     
island_list = island['island'].tolist()
species_list = species['species'].tolist()
fig, ax = plt.subplots()

data_ping['species'].value_counts().plot(kind = 'pie',
                                      ax= ax,
                                      colors = ['chocolate','salmon','yellow'],
                                      startangle = 90,
                                      shadow= True,
                                      autopct='%1.1f%%',
                                      )
ax.set_ylabel('')
#hay más Adelie

for isla in island_list:
    df_isla = data_ping[data_ping['island'] == isla] 
    fig, ax = plt.subplots()
    df_isla['species'].value_counts().plot(kind = 'pie',
                                          ax= ax,
                                          colors = ['chocolate','salmon','yellow'],
                                          startangle = 90,
                                          shadow= True,
                                          autopct='%1.1f%%'
                                          )
    ax.set_title(f'Isla {isla}')
    
    # Quitar la etiqueta del eje Y para mejor presentación
    ax.set_ylabel('')

# Definir límites comunes para el eje X (mín y máx de bill_depth_mm)
x_min = data_ping['bill_depth_mm'].min()
x_max = data_ping['bill_depth_mm'].max()



# Generar histogramas con los mismos ejes
for specie in species_list:
    df_especie = data_ping[data_ping['species'] == specie]
    
    # Crear figura y ejes
    fig, ax = plt.subplots(figsize=(6, 4))
    
    # Crear histograma
    ax.hist(df_especie['bill_depth_mm'].dropna(), bins=20, color='skyblue', edgecolor='black')
    
    # Configurar título
    ax.set_title(f'Especie: {specie} Bill  depth')
    
    # Establecer los mismos rangos de eje X e Y
    ax.set_xlim(x_min, x_max)  # Mismo rango en X
    ax.set_ylim(0, 22)  # Mismo rango en Y
    



# Generar histogramas con los mismos ejes
for specie in species_list:
    df_especie = data_ping[data_ping['species'] == specie]
    
    # Crear figura y ejes
    fig, ax = plt.subplots(figsize=(6, 4))
    
    # Crear histograma
    ax.hist(df_especie['bill_length_mm'].dropna(), bins=20, color='skyblue', edgecolor='black')
    
    # Configurar título
    ax.set_title(f'Especie: {specie} Bill length')
    
    # Establecer los mismos rangos de eje X e Y
    ax.set_xlim(x_min, x_max)  # Mismo rango en X
    ax.set_ylim(0, 20)  # Mismo rango en Y
    
x_min = data_ping['flipper_length_mm'].min()
x_max = data_ping['flipper_length_mm'].max()



# Generar histogramas con los mismos ejes
for specie in species_list:
    df_especie = data_ping[data_ping['species'] == specie]
    
    # Crear figura y ejes
    fig, ax = plt.subplots(figsize=(6, 4))
    
    # Crear histograma
    ax.hist(df_especie['flipper_length_mm'].dropna(), bins=20, color='skyblue', edgecolor='black')
    
    # Configurar título
    ax.set_title(f'Especie: {specie} Flippers length')
    
    # Establecer los mismos rangos de eje X e Y
    ax.set_xlim(x_min, x_max)  # Mismo rango en X
    ax.set_ylim(0, 20)  # Mismo rango en Y
    
#Adelie tiene todo de mayor tamaño

x_min = data_ping['bill_length_mm'].min()
x_max = data_ping['bill_length_mm'].max()
colores = dict(zip(['Female', 'Male'],['red','blue']))
fig, ax = plt.subplots()
for sexo in ['Female', 'Male']:
    data = data_ping[data_ping['sex']== sexo]
    for specie in species_list:
        df_especie = data[data['species'] == specie]
        
        # Crear figura y ejes
        fig, ax = plt.subplots()
        
        # Crear histograma
        ax.hist(df_especie['bill_length_mm'].dropna(), bins=20, color = colores[sexo], edgecolor='black')
        
        # Configurar título
        ax.set_title(f'Especie: {specie} Bill length')
        
        # Establecer los mismos rangos de eje X e Y
        ax.set_xlim(x_min, x_max)  # Mismo rango en X
        ax.set_ylim(0, 20)  # Mismo rango en Y
        
        
fig, ax = plt.subplots()
ax.set_title('Pico y alas según sexo')
for sexo in ['Female', 'Male']:
    ax.scatter(data = data_ping[data_ping['sex']== sexo], x = 'bill_length_mm', y ='flipper_length_mm', color = colores[sexo] )
ax.set_xlabel('pico', fontsize ='medium')
ax.set_ylabel('alas', fontsize ='medium')
