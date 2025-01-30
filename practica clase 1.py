# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 21:53:31 2025

@author: Adrian
"""

import csv
import pandas as pd

def encabezados(nombre_archivo):
    with open (nombre_archivo) as file:
        encabezado = next(file)
    return encabezado

print(encabezados(r'C:\Users\Adrian\Downloads\arbolado-en-espacios-verdes.csv' ))
def leer_parque (nombre_archivo, parque):
    df = pd.read_csv(nombre_archivo)
    info_parque = []
    cant_filas = df.shape[0]
    j = 1
    for i in range (1, cant_filas):
        if df.iloc[i][10] == parque:
            arbol = dict([(j,df.iloc[i].tolist())])
            info_parque.append(arbol)
            j += 1
    return info_parque

print(leer_parque(r'C:\Users\Adrian\Downloads\arbolado-en-espacios-verdes.csv' ,'GENERAL PAZ'))

def especies(lista_arboles):
    conjunto_especies = []
    for arbol in lista_arboles:
        for clave in arbol:
            especie = arbol[clave][7]
            if especie not in conjunto_especies:
                conjunto_especies.append(especie)
    return conjunto_especies
            

print(especies(leer_parque(r'C:\Users\Adrian\Downloads\arbolado-en-espacios-verdes.csv' ,'GENERAL PAZ')))

def contar_ejemplares(lista_arboles):
    ejemplares = {}
    for arbol in lista_arboles:
        for clave in arbol:
            especie = arbol[clave][7]
            if especie in ejemplares:
                ejemplares[especie] += 1
            else:
                ejemplares[especie] = 1
    return ejemplares

print(contar_ejemplares(leer_parque(r'C:\Users\Adrian\Downloads\arbolado-en-espacios-verdes.csv' ,'GENERAL PAZ')))

def obtener_alturas(lista_arboles, especie):
    alturas = []
    for arbol in lista_arboles:
        for clave in arbol:
            if especie == arbol[clave][7]:
                alturas.append(float(arbol[clave][3]))
    return alturas

print(obtener_alturas(leer_parque(r'C:\Users\Adrian\Downloads\arbolado-en-espacios-verdes.csv' ,'GENERAL PAZ'),'Jacarandá'))

def altura_max(alturas):
    return max(alturas)

def altura_promedio(alturas):
    return sum(alturas)/len(alturas)

print(altura_max(obtener_alturas(leer_parque(r'C:\Users\Adrian\Downloads\arbolado-en-espacios-verdes.csv' ,'GENERAL PAZ'),'Jacarandá')))
print(altura_promedio(obtener_alturas(leer_parque(r'C:\Users\Adrian\Downloads\arbolado-en-espacios-verdes.csv' ,'GENERAL PAZ'),'Jacarandá')))

def obtener_inclinaciones(lista_arboles, especie):
    inclinaciones= []
    for arbol in lista_arboles:
        for clave in arbol:
            if especie == arbol[clave][7]:
                inclinaciones.append(float(arbol[clave][5]))
    return inclinaciones

print(obtener_inclinaciones(leer_parque(r'C:\Users\Adrian\Downloads\arbolado-en-espacios-verdes.csv' ,'GENERAL PAZ'),'Jacarandá'))

def especimen_mas_inclinado(lista_arboles):
    inclinaciones_por_arbol = {}
    arboles = especies(lista_arboles)
    for especie in arboles:
        inclinaciones_por_arbol[especie] = obtener_inclinaciones(lista_arboles, especie)
    print (inclinaciones_por_arbol)
    inclinaciones_maximas = {}
    for especie in inclinaciones_por_arbol:
        inclinaciones_maximas[especie] = altura_max(inclinaciones_por_arbol[especie])
    print (inclinaciones_maximas)
    mas_alto = max(inclinaciones_maximas, key=inclinaciones_maximas.get) 
    res = [mas_alto, inclinaciones_maximas[mas_alto]]
    return res
print(especimen_mas_inclinado(leer_parque(r'C:\Users\Adrian\Downloads\arbolado-en-espacios-verdes.csv' ,'CENTENARIO')))

def especimen_promedio_mas_inclinado(lista_arboles):
    inclinaciones_por_arbol = {}
    arboles = especies(lista_arboles)
    print(arboles)
    for especie in arboles:
        inclinaciones_por_arbol[especie] = obtener_inclinaciones(lista_arboles, especie)
    print(inclinaciones_por_arbol)
    inclinaciones_promedios = {}
    for especie in inclinaciones_por_arbol:
        inclinaciones_promedios[especie] = altura_promedio(inclinaciones_por_arbol[especie])
    print(inclinaciones_promedios)
    mayor_promedio = max(inclinaciones_promedios, key=inclinaciones_promedios.get) 
    res = [mayor_promedio, inclinaciones_promedios[mayor_promedio]]
    return res
print(especimen_promedio_mas_inclinado(leer_parque(r'C:\Users\Adrian\Downloads\arbolado-en-espacios-verdes.csv' ,'EJERCITO DE LOS ANDES')))
    