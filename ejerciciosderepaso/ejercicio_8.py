# Crear una función que invierta el orden de los elementos en una lista dada.

def invertir_lista(lista):
  lista_invertida = []
  for i in range(len(lista) - 1, -1, -1):
    lista_invertida.append(lista[i])
  return lista_invertida

lista = [1, 2, 3, 4, 5]
print(invertir_lista(lista)) # [5, 4, 3, 2, 1]
