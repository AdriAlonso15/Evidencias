"""
Created on Thu Jun 23 19:42:55 2022

@author: adriana alonso custodio
"""

import numpy as np

array = np.random.randint(0, 50, size=(15, 12))  
porprom = np.amin(array)

print ("La lista ingresada es la siguiente:")
print (array)
print ()
print("El dato menor del array es:")
print (porprom)
