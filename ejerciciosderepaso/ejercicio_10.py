# . Escribir una función que calcule el factorial de un número dado.

def factorial (num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial (num-1)

numero = int(input("ingrese un numero positivo"))
if numero < 0:
    print ("el numero debe ser positivo.")
else:
    resultado = factorial(numero)
    print("el numero factorial de ",numero, "es ", resultado)

