# Escribir un programa que determine si un número dado es par o impar

def par (num):
    return num % 2 == 0
def main ():
    try:
        numero = int(input("ingrese un numero entero: "))
        if par(numero):
            print (numero, "es un numero par")
        else:
            print(numero,"es un numero impar ")
    except ValueError:
        print("No has ingresado un numero entero")
