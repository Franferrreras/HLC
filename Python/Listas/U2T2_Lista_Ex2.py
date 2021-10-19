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
