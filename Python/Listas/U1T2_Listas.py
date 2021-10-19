# Ejercicio 3:
# Dada una lista de números. Convierte cada elemento de una lista en su cuadrado

# Dado:

# lista = [1, 2, 3, 4, 5, 6, 7]


# Resultado esperado
# [1, 4, 9, 16, 25, 36, 49]

lista = [1, 2, 3, 4, 5, 6, 7]
lista2 = []

for i in range(len(lista)):
    lista2.append(lista[i]*lista[i])
    
print(lista2)


#________________________________________________________________________________
# Ejercicio 4:
# Concatenar dos listas en el siguiente orden

# Dado:
# lista1 = ["Hola ", "toma "]
# lista2 = ["guapo", "señor"]


# Resultado esperado:

# ['Hola guapo', 'Hola señor', 'toma guapo', 'toma señor']