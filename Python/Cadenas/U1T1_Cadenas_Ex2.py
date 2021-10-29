# Ejercicio 2:
# Dadas dos cadenas, s1 y s2, cree una nueva cadena agregando s2 en medio de s1

s1 = input("Introduzca una palabra")
s2 = input("Introduzca otra palabra")

        
print(s1[:int(len(s1)/2)]+s2+s1[int(len(s1)/2):])
        
    

# Dado :

# s1 = "Hola"
# s2 = "Adios"

# Resultado:

# HoAdiosla
