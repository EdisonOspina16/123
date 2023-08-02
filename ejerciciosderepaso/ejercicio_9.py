# Crear un programa que genere una matriz de números y la imprima en pantalla.

import random

filas = 3
columnas = 4

matriz = []

for i in range(filas):
  fila = []
  for j in range(columnas):
    numero = random.randint(0, 9)
    fila.append(numero)
  matriz.append(fila)

for fila in matriz:
  print(fila)

