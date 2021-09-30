#Ejercicio1: Dada una cadena de longitud impar mayor que 7, devuelve una nueva cadena formada por los tres caracteres del medio de una cadena determinada.


cadena = input("Introduzca una cadena")

for i in range(len(cadena)/2 , (len(cadena)/2)+2):
        print(cadena[i])