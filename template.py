import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import r2_score, mean_squared_error

# %%===========================================================================
# roundup
# =============================================================================
ru = pd.read_csv("datos_roundup.txt", delim_whitespace=' ')
X = sum(ru['RU'])/len(ru['RU'])
Y =  sum(ru['ID'])/len(ru['ID'])

cuenta1 = 0
for row in ru:
    x = (row['RU'] - X) * (row['ID'] - Y) 
    cuenta1 += x
cuenta2 = 0
for row in ru:
    y = (row['RU'] - X) * (row['ID'] - Y) 
    cuenta2 += y
cuenta = x/y


# %% Aproximar recta
# Y = a + b*X
X = np.linspace(min(ru['RU']), max(ru['RU']))
b,a= np.polyfit(ru['RU'] , ru['ID'] , 1)
Y = a + b*X
plt.scatter(ru['RU'], ru['ID'])
plt.plot(X, Y,  'r')
plt.show()

#%% Obtener recta de cuadrados minimos

plt.scatter(ru['RU'], ru['ID'])
plt.plot(X, Y, 'k')
plt.show()

#%% Calcular score R²
X = ru['RU']
Y =ru['ID']
b,a= np.polyfit(ru['RU'] , ru['ID'] , 1)
Y_pred=a + b*X

r2 = r2_score(Y, Y_pred) #Que tanto se parece a una recta
print("R²: " + str(r2))

MSE = mean_squared_error(Y,Y_pred) #Diferencia entre valor real y valor esperado
print("MSE: " + str(MSE))


# %%===========================================================================
# Anascombe
# =============================================================================
df = sns.load_dataset("anscombe")


# %%===========================================================================
# mpg
# =============================================================================

mpg = pd.read_csv("auto-mpg.xls")

"""
mpg: miles per galon
displacement: Cilindrada
 X = np.linspace(min(col1), max(col1))
    Y =col2
    c,b,a= np.polyfit(col1 , col2 , grado)
    Y_pred = a + b*X + c*X**2
    plt.scatter(col1, col2)
    plt.plot(X, Y_pred,  'r')
    X2 = col1
    Y_pred2 = a + b*X + c*X2**2
    r2 = r2_score(Y, Y_pred2) #Que tanto se parece a una recta
"""


print(mpg.dtypes)

# %% Comparar variables con graficos

def versus(col1, col2):
    plt.scatter(col1, col2)
    plt.show()


versus = versus(mpg['acceleration'], mpg['horsepower'])

#%% Comparar variables y calcular recta de cuadrados minimos

def reg_lineal(col1, col2, grado=3):
    X = np.linspace(min(col1), max(col1))
    d,c,b,a= np.polyfit(col1 , col2 , grado)
    Y = a + b*X + c*X**2 + d*X**3 
    plt.scatter(col1, col2)
    plt.plot(X, Y,  'r')
    plt.show()
    
reg_lineal= reg_lineal(mpg['acceleration'], mpg['horsepower'])

def reg_lineal2(col1, col2, grado=2):
    X = np.linspace(min(col1), max(col1))
    c,b,a= np.polyfit(col1 , col2 , grado)
    Y = a + b*X + c*X**2 
    plt.scatter(col1, col2)
    plt.plot(X, Y,  'r')
    plt.show()


reg_lineal2= reg_lineal2(mpg['acceleration'], mpg['horsepower'])

    
#%% Comparar variables, calcular recta de cuadrados minimos y calcular R²

def reg_lineal_r2(col1, col2, grado=2):
    X = np.linspace(min(col1), max(col1))
    Y =col2
    c,b,a= np.polyfit(col1 , col2 , grado)
    Y_pred = a + b*X + c*X**2
    plt.scatter(col1, col2)
    plt.plot(X, Y_pred,  'r')
    X2 = col1
    Y_pred2 = a + b*X2 + c*X2**2
    r2 = r2_score(Y, Y_pred2) #Que tanto se parece a una recta
    plt.title("R²: " + str(r2))
    plt.show()
    
reg_lineal_r2 = reg_lineal_r2(mpg['acceleration'], mpg['horsepower'])