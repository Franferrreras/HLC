#Ejercicio1: Dada una cadena de longitud impar mayor que 7, devuelve una nueva cadena formada por los tres caracteres del medio de una cadena determinada.


cadena = input("Introduzca una cadena")

print(cadena[int(len(cadena)/2)-1:int((len(cadena)/2)+2)])
