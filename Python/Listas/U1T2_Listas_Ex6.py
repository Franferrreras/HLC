# Ejercicio 6

# Eliminar cadenas vacías de la lista de cadenas

# Dado:

# lista = ["Chema", "", "Juan Diego", "Diana", "", "Alejandro"]

# Resultado:

# ["Chema", "Juan Diego", "Diana", "Alejandro"]


lista = ["Chema", "", "Juan Diego", "Diana", "", "Alejandro"]
lista2 = []

for i in range(len(lista)): 
    if (lista[i] != ""):
        lista2.append(lista[i])

print(lista2)