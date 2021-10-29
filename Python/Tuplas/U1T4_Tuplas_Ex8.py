# Ejercicio 8

# Ordenar una tupla de tuplas por segundo elemento

# tupla = (('a', 23),('b', 37),('c', 11), ('d',29))

# Resultado:

# (('c', 11), ('a', 23), ('d', 29), ('b', 37))


tupla = (('a', 23),('b', 37),('c', 11), ('d',29))


lista1 = list(tupla)

lista1 = [('a', 23),('b', 37),('c', 11), ('d',29)]
lista1.sort(key=lambda x: x[1])

tupla2 = tuple(lista1)

print(tupla2)