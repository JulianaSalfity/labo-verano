# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

with open ('datame.txt', 'rt') as file:
	data = file.read()
    
    
nuevo_archivo = 'inicio de texto\n' + data
nuevo_archivo = nuevo_archivo + 'cierre de texto'

datame = open('nuevo.txt', 'w')
datame.write(nuevo_archivo)
datame.close()
with open ('nuevo.txt', 'r') as file:
	data1 = file.read()
    
print(data1)

lista_materias = []
with open ('cronograma_sugerido.csv', 'rt') as file:
   encabezado = next(file)
   for line in file:
    	datos_linea = line.split(',')
    	lista_materias.append(datos_linea[1])
    
encabezado1 = encabezado.split(',')

print(encabezado1[1])
print(lista_materias)

def cuantas_materias (n):
	count = 0
	#n = input("n° de cuatrimestre")
	with open ('cronograma_sugerido.csv', 'rt') as file:
    	encabezado = next(file)
    	for line in file:
        	datos_linea = line.split(',')
        	if n == int(datos_linea[0]):
            	count +=1
    	return count
    
print(cuantas_materias(8))

def materias_cuatrimestre
    
import random
def generala_tirar():
	i = 0
	resultado = []
	while i < 5:
    	dado = random.randint(1,6)
    	resultado.append(dado)
    	i +=1  	 
	return resultado

print(generala_tirar())

with open ('datame.txt', 'rt') as file:
	for line in file:
    	palabras_linea = line.split(' ')
    	if 'estudiantes' in palabras_linea:
        	print(line)
       	 
import numpy as np
def pisar_elmento(M,e):
	dimension = M.shape
	columnas_dim = dimension[0]
	filas_dim = dimension[1]
	columnas = 0
	filas = 0
	for elems in M[columnas]:
    	if elems == e:
        	M[columnas,filas] = -1
    	if columnas == columnas_dim - 1:
        	columas = 0
    	else:    
        	columnas += 1
    	if filas == filas_dim - 1:
        	filas = 0
    	else:    
        	filas += 1
	return M

print(pisar_elmento(M = np.array([[0, 1, 2, 3], [4, 5, 6, 7]]), e = 2))
import numpy as np
def pisar_elmento1(M,e):
    nueva_M = M.copy()  
    nueva_M[nueva_M == e] = -1  
    return nueva_M

print(pisar_elmento1(M = np.array([[0, 1, 2, 3], [4, 5, 6, 7]]), e = 2))

import pandas as pd
fname = 'cronograma_sugerido.csv'
df = pd.read_csv(fname)

