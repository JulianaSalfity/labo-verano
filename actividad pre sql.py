# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 14:28:22 2025

@author: Adrian
"""
empleado_01 = [
    [20222333, 45, 2, 20000],
    [33456234, 40, 0, 25000],
    [45432345, 41, 1, 10000]
]

empleado_02 = [
    [20222333, 45, 2, 20000],
    [33456234, 40, 0, 25000],
    [45432345, 41, 1, 10000],
    [43967304, 37, 0, 12000],
    [42236276, 36, 0, 18000],
]

empleado_03 = [
    [20222333, 20000, 45, 2],
    [33456234, 25000, 40, 0],
    [45432345, 10000, 41, 1],
    [43967304, 12000, 37, 0],
    [42236276, 18000, 36, 0],
]

empleado_04 = [
    [20222333, 33456234, 45432345, 43967304, 42236276],
    [20000, 25000, 10000, 12000, 18000],
    [45, 40, 41, 37, 36],
    [2, 0, 1 ,0, 0],
]


def superanSalarioActividad01(empleados,umbral):
    res = []
    for fila in empleados:
        if fila[3] > umbral:
            res.append(fila)
    return res

def superanSalarioActividad03(empleados,umbral):
    res = []
    for fila in empleados:
        nueva_fila = [fila[0], fila[2], fila[3], fila[1]]
        if nueva_fila[3] > umbral:
            res.append(nueva_fila)
    return res

def superanSalarioActividad04(empleados,umbral):
    res = []
    empleados_fila = []
    cant_atributos = len(empleados[0])
    while cant_atributos > 0:
        empleados_fila.append([])
        cant_atributos -= 1
    i = 0
    print(empleados_fila)
    cant_elementos = len(empleados_fila)-1
    j = 0
    while j < cant_elementos:
        for columna in empleados:
            print(columna)
            print(columna[i])
            while i < len(empleados)-1:
                empleados_fila[j].append(columna[i])
                i += 1
                print(empleados_fila[j])
                i = 0
        j += 1
    print(empleados_fila)
    
#print(superanSalarioActividad01(empleado_01,15000))
#print(superanSalarioActividad01(empleado_02,15000))
#print(superanSalarioActividad03(empleado_03,15000))
print(superanSalarioActividad04(empleado_03,15000))
