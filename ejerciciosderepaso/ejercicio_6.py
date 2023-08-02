# Crear un programa que calcule la suma de los números en una lista dada.

def suma_lista(lista):
    suma = 0
    for numero in lista:
        suma = suma + numero
    return suma

lista = [1, 2, 3, 4, 5]
suma = suma_lista(lista)

