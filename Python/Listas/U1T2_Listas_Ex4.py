# Ejercicio 4:
# Concatenar dos listas en el siguiente orden

# Dado:
# lista1 = ["Hola ", "toma "]
# lista2 = ["guapo", "señor"]


# Resultado esperado:

# ['Hola guapo', 'Hola señor', 'toma guapo', 'toma señor']

lista1 = ["Hola ", "toma "]
lista2 = ["guapo", "señor"]
lista3 = []

for i in range(len(lista1)):
    for j in range(len(lista2)):
        lista3.append(lista1[i]+lista2[j])
        

print(lista3)