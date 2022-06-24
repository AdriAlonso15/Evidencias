# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 20:10:15 2022

@author: adriana alonso custodio
"""

Compras = ["Leche","Arroz","Frijoles","Fruta","Jabon","Cereal"]
d = int(input("Que quieres hacer con esta lista? 1)Pila o 2)Cola: "))
if d == 1:
    print("Escogiste la opcion 'Pila' ")
    print(Compras)
    Compras.pop()
    print(Compras)
    Compras.pop()
    print(Compras)
    Compras.pop()
    print(Compras)
    Compras.pop()
    print(Compras)
    Compras.pop()
    print(Compras)
    Compras.pop()
    print(Compras)
elif d==2:
    print("Escogiste la opcion 'Cola' ")
    print(Compras)
    Compras.pop(0)
    print(Compras)
    Compras.pop(0)
    print(Compras)
    Compras.pop(0)
    print(Compras)
    Compras.pop(0)
    print(Compras)
    Compras.pop(0)
    print(Compras)
    Compras.pop(0)
    print(Compras)
else:
    print("Opcion invalida, intentelo de nuevo")