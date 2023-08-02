# Escribir un programa que encuentre el número más grande
# y el más pequeño en una lista dada.

def max_min(lista):
  maximo = lista[0]
  minimo = lista[0]
  for i in range(1, len(lista)):
    if lista[i] > maximo:
      maximo = lista[i]
    if lista[i] < minimo:
      minimo = lista[i]
  return (maximo, minimo)

lista = [5, 3, 7, 9, 2, 4, 6, 8]
resultado = max_min(lista)
print("El número más grande es", resultado[0])
print("El número más pequeño es", resultado[1])
