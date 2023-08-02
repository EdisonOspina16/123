# Crear un programa que genere una lista de números aleatorios
# y los imprima en pantalla.

import random
def generar_Listas_aleatorias(longitud, rango_minimo, rango_maximo):
    lista_aleatoria = [random.randint(rango_minimo, rango_maximo) for _  in range(longitud)]
    return lista_aleatoria

def main():
    longitud_lista = int(input("ingrese la longitud de la lista aleatoria: "))
    rango_minimo = int(input("ingrese el rango minimo de los numeros: "))
    rango_maximo = int(input("ingrese el rango maximo de los numeros: "))

    lista_aleatoria = generar_Listas_aleatorias(longitud_lista, rango_minimo, rango_maximo)

    print("lista aleatoria generada:")
    print(lista_aleatoria)

if __name__== "__main":
    main()
