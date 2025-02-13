#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 10:00:13 2025

@author: Estudiante
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
carpeta = "/home/Estudiante/Descargas/"

data_wine = pd.read_csv(carpeta+"wine.csv", sep = ";")

#Genera un gráfico qqe relaciona la acidez y el contenido de ácido cítrico
plt.scatter(data = data_wine, x = 'fixed acidity', y ='citric acid')
plt.scatter(data = data_wine, x = 'fixed acidity', y ='residual sugar')

fig, ax = plt.subplots()

ax.set_title('Acidez vs contenido de ácido cítrico')
ax.scatter(data = data_wine,
           x = 'fixed acidity', y ='citric acid', s = 8, color = 'green')
ax.set_xlabel('Acidez', fontsize ='medium')
ax.set_ylabel('cont_citr', fontsize ='medium')

arboles = pd.read_csv(carpeta+"arbolado-en-espacios-verdes.csv")

print(arboles.columns)
print(arboles.shape)


id_esp = list(arboles["nombre_com"].value_counts().index)[:30]

arboles[arboles["nombre_com"].isin(id_esp)]

#%%

fig, ax = plt.subplots()
ax.set_title('Long vs Lat')
ax.scatter(data = arboles,
           x = 'long', y ='lat', s = 8, color = 'forestgreen')
ax.set_xlabel('long', fontsize ='medium')
ax.set_ylabel('lat', fontsize ='medium')
#%%

fig, ax = plt.subplots()
ax.set_title('altura X diametro')
ax.scatter(data = arboles, y = 'altura_tot', x = 'diametro', s = 8, color = 'plum')
ax.set_xlabel('alt', fontsize ='medium')
ax.set_ylabel('dia', fontsize ='medium')

#%%
fig, ax = plt.subplots()
colores = dict(zip(['Exótico','Nativo/Autóctono', 'No Determinado'],['red', 'blue', 'green']))
for origen in ['Exótico','Nativo/Autóctono', 'No Determinado']:
            ax.scatter(data = arboles[arboles['origen']== origen], 
           x = 'diametro', 
           y = 'altura_tot', 
           c = colores[origen], 
           label = origen,
           alpha= 0.5)

ax.legend()
ax.grid(True)

#%%

fig, ax = plt.subplots()
cheetaRegion


tamanoBurbuja = 5

ax.scatter(data = data_wine, 
           x = 'fixed acidity',
           y = 'citric acid', 
           s = data_wine['residual sugar']*tamanoBurbuja)

ax.set_xlabel('Acidez', fontsize ='medium')
ax.set_ylabel('cont_citr', fontsize ='medium')
ax.set_title('Tres variables')

#%%data_wine,
fig, ax = plt.subplots()
data_wine['type'].value_counts().plot(kind = 'pie',
                                      ax= ax,
                                      autopct = '%1.1f%%',
                                      colors = ['chocolate','salmon'],
                                      startangle = 90,
                                      shadow= True,
                                      explode= (0.1,0)
                                      )

#%%
# Busco relación entre el PH y el ácido cítrico
fig, ax = plt.subplots()
colores = dict(zip(['white','red'],['pink','darkred']))
ax.set_title('pH vs residual sugar según tipo')
for tipo in['white','red']:
            ax.scatter(data = data_wine[data_wine['type']== tipo],
                       x = 'pH', y ='residual sugar', s = 8, color = colores[tipo], label= tipo)
ax.set_xlabel('pH', fontsize ='medium')
ax.set_ylabel('sugar', fontsize ='medium')
ax.legend()


fig.savefig('sugarph')

#%%
carpeta = "/home/Estudiante/Descargas/"
fig, ax = plt.subplots()
cheetahRegion = pd.read_csv(carpeta+"cheetahRegion.csv")
ax.bar(data= cheetaRegion, x = 'Anio', height = 'Ventas')

ax.set_title('Ventas')
ax.set_xlabel('Año', fontsize = 'medium')
ax.set_ylabellabel('ventas', fontsize = 'medium')
ax.set_xlim(0,11)
ax.set_ylim(0,259)

ax.set_xticks(range(1,11,1))
ax.set_yticks([])

#%%
fig, ax = plt.subplots()
cheetahRegion.plot(x = 'Anio',
                   y = ['regionEste', 'regionOeste'],
                   kind = 'bar',
                   label = ['regionEste', 'regionOeste'],
                   ax = ax)
#%%
fig, ax = plt.subplots()
ax.bar(cheetahRegion['Anio'], cheetahRegion['regionEste'], label = 'Region este', color = 'darkblue')
ax.bar(cheetahRegion['Anio'], cheetahRegion['regionOeste'], label = 'Region oeste', color = 'teal')

#%%
fig, ax = plt.subplots()
ax.plot('Anio', 'Ventas', data = cheetahRegion, marker = "o")
ax.set_title('Ventas')
ax.set_xlabel('Año', fontsize = 'medium')
ax.set_ylabellabel('ventas', fontsize = 'medium')
ax.set_xlim(0,12)
ax.set_ylim(0,250)

#%%
fig, ax = plt.subplots()
ax.plot('Anio','regionEste', data= cheetahRegion,
        marker = '.',
        linestyle= '-',
        linewidth = 0.5,
        label = 'Region este',
        )

ax.plot('Anio','regionOeste', data= cheetahRegion,
        marker = '.',
        linestyle= '-',
        linewidth = 0.5,
        label = 'Region oeste',
        )
ax.legend()

#%%
carpeta = "/home/Estudiante/Descargas/"
fig, ax = plt.subplots()
gaseosas = pd.read_csv(carpeta+'gaseosas.csv')

gaseosas['Compras_gaseosas'].value_counts().plot.bar(ax=ax, color = 'chocolate')
ax.tick_params(axis ='x', labelrotation = 0)
ax.set_title('Frecuencia Venta de Gaseosas')
ax.set_xlabel('Marcas gaseosas')
ax.set_yticks([])
ax.bar_laberl(ax.containers[0], fontsize = 8)

#%%

carpeta = "/home/Estudiante/Descargas/"
fig, ax = plt.subplots()
gaseosas = pd.read_csv(carpeta+'gaseosas.csv')

gaseosas['Compras_gaseosas'].value_counts(normalize = True).plot.bar(ax=ax, color = 'chocolate')
ax.tick_params(axis ='x', labelrotation = 0)
ax.set_title('Frecuencia Venta de Gaseosas')
ax.set_xlabel('Marcas gaseosas')
ax.set_yticks([])
ax.bar_laberl(ax.containers[0], fontsize = 8)

#%%
fig, ax = plt.subplots()
carpeta = "/home/Estudiante/Descargas/"
ageAtDeath = pd.read_csv(carpeta+'ageAtDeath.csv')
sns.histplot(data=ageAtDeath['AgeAtDeath'], bins = 20, color = 'salmon')


#%%

fig, ax = plt.subplots()
sns.histplot(data=tips, x = 'tip',hue='sex', bins = 14, palette = 'flare')


#%%

print(tips['tip'].mode())
print(tips['tip'].median())
print(tips['tip'].mean())
print(tips['tip'].std())
print(tips['tip'].describe())

#%%

carpeta = "/home/Estudiante/Descargas/"
fig, ax = plt.subplots()
ventaCasas = pd.read_csv(carpeta+'ventaCasas.csv')

ax.boxplot(ventaCasas['PrecioDeVenta'], showmeans = True)

ax.set_title('precio ventas')
ax.set_xtciks([])
ax.set_ylabel('precio ventas($)')
ax.set_ylim(0,500)

#%%

fig, ax = plt.subplots()
tips.boxplot(by=['sex'], column=['tip'], ax = ax, grid = False, showmeans = True)
    
fig.subtitle('')
ax.set_title('Propinas')
ax.set_xlabel('Sexo')
ax.set_ylabel('Valor propina($)')
    
#%%
fig, ax = plt.subplots()
ax = sns.violinplot(x = 'sex', y = 'tip', data = tips,
                    palette= {'Female': 'orange', 'Male': 'skyblue'})
    

ax.set_title('Propinas')
ax.set_xlabel('Sexo')
ax.set_ylabel('Valor propina($)')
ax.set_ylim(0,12)
ax.set_xticklabels(['fem','masc'])
    