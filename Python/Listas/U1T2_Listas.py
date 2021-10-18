
#________________________________________________________________________________
# Ejercicio 2:
# Concatenar dos listas por índice

# Dado:
# lista1 = ["M", "nom", "e", "Che"]
# lista2 = ["i", "bre", "s", "ma"]

# Resultado esperado:
# ['Mi nombre es Chema']

lista1 = ["M", "nom", "e", "Che"]
lista2 = ["i", "bre", "s", "ma"]
cadena=""
listnw = [cadena]

if (len(lista1) > len(lista2)):
    rang = len(lista1)
        
elif (len(lista1) < len(lista2) ):
    rang = len(lista2)
    
    
    
else :
    rang = len(lista1)


for i in range(len(rang)):
    listnw[0] += lista1[i]
    listnw[0] += lista2[i]
    listnw[0] += " "

print(listnw)


#________________________________________________________________________________
# Ejercicio 3:
# Dada una lista de números. Convierte cada elemento de una lista en su cuadrado

# Dado:

# lista = [1, 2, 3, 4, 5, 6, 7]


# Resultado esperado
# [1, 4, 9, 16, 25, 36, 49]





#________________________________________________________________________________
# Ejercicio 4:
# Concatenar dos listas en el siguiente orden

# Dado:
# lista1 = ["Hola ", "toma "]
# lista2 = ["guapo", "señor"]


# Resultado esperado:

# ['Hola guapo', 'Hola señor', 'toma guapo', 'toma señor']