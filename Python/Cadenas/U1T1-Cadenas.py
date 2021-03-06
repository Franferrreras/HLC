________________________________________________________________________________________________



#__________________________________________________________________________________________________

        
#________________________________________________________________________________________________________________
# Ejercicio 6:
# Dadas dos cadenas, s1 y s2, cree una cadena mixta usando las siguientes reglas


# Nota : cree una tercera cadena hecha del primer carácter de s1, luego el último carácter de s2, Siguiente, el segundo carácter de s1 y el segundo último carácter de s2, y así sucesivamente. Los caracteres sobrantes van al final del resultado.

# Dado:

# s1 = "Abc"
# s2 = "Xyz"

# Resultado esperado:

# AzbycX

s1 = "Abc"
s2 = "Xyzpq"
s3 = s2[::-1]
s4 = s1+s3
saux = s1[::-1]
saux2 = saux+s2
s5 = ""

#s4 = "ABCXYZBP"
if ( len(s1) < len(s2)):
    resto = len(s2)-len(s1)
    for i in range(len(s4)):
        if (i < len(s1)):
            s5+=s1[i]
            s5+=s3[i]
        else:
            if(len(s4)-resto <= i <= len(s4)):
                s5+=s4[i]
elif(len(s1) > len(s2)):
    resto = len(s1)-len(s2)
    for i in range(len(s4)):
        if (i < len(s2)):
            s5+=s1[i]
            s5+=s3[i]
    else:
        if(len(saux2)-resto <= i <= len(saux2)):
            s5+=saux2[i]
else:
    for i in range(len(s1)):
        s5+=s1[i]
        s5+=s2[-(i+1)]
print(s5)
#Versión Pedro incompleta
# for i in range(len(s1)):
#     s3+=s1[i]
#     s3+=s2[-(i+1)]
    
# print(s3)

#_________________________________________________________________________________________________________________
# Ejercicio 7:
# Prueba de equilibrio de caracteres de cadena


# Asumiremos que una cadena s1 y s2 está equilibrada si todos los caracteres de s1 están en s2. la posición de los caracteres no importa.

# Dado:
# Caso 1:

# s1 = "hD"
# s2 = "ChemaDuran"

# Resultado:

# True

# Caso 2 :

# s1 = "hDf"
# s2 = "ChemaDuran"

# Resultado:

# Falso


#_________________________________________________________________________________________________________________
# Ejercicio 8:
# Busque todas las apariciones de "que" en una cadena dada, independientemente que esté o no en mayúsculas.


# Dado :

# str1 = "Lo que yo te diga. Que la vida es así"

# Resultado:

# El recuento de 'que' es: 2


# Ejercicio 9:
# Dada una cadena, devuelve la suma y el promedio de los dígitos que aparecen en la cadena, ignorando todos los demás caracteres.


# Dado :

# str1 = "Galicia = 78 Andalucia = 83 Canarias = 68 Cataluña = 65"

# Resultado:

# la suma es 294
# el promedio es 73.5

# Ejercicio 10:
# Dada una cadena de entrada, cuente las apariciones de todos los caracteres dentro de una cadena

# Dado :

# str1 = "Apple"

# Resultado:

# {'A': 1, 'p': 2, 'l': 1, 'e': 1}

# Ejercicio 11:
# Invertir una cuerda determinada

# Dado :

# str1 = "ChemaDuran"

# Resultado:

# naruDamehC

# Ejercicio 12:
# Encuentre la última posición de una subcadena "Chema" en una cadena determinada


# Dado :

# str1 = "Chema es un profesor del IES Alixar que sabe Python. Chema trabaja mucho."

# Resultado:

# La última ocurrencia de Chema comienza en el índice: 53

# Ejercicio 13:
# Divida una cadena dada con guiones en varias subcadenas y muestre cada subcadena.


# Dado :

# str1 = Chema-es-un-profesor

# Resultado:

# Chema
# es
# un
# profesor

# Ejercicio 14:
# Eliminar cadenas vacías de una lista de cadenas

# Dado :
# str_list = ["Chema", "Alejandro", "", "Juan Diego", None, "Diana", ""]

# Resultado esperado :

# # lista original
# ['Chema', 'Alejandro', '', 'Juan Diego', None, 'Diana', '']
# # Después de quitar cadenas vacías
# ['Chema', 'Alejandro', 'Juan Diego', 'Diana']

# Ejercicio 15:
# Eliminar símbolos / puntuación especiales de una cadena determinada


# Dado :

# str1 = "/*Chema es @profesor & maker"

# Resultado esperado :

# "Chema es profesor maker"

# Ejercicio 16:
# Eliminación de todos los caracteres que no sean enteros de una cadena
# Dado :

# str1 = 'Tengo 39 años y 10 meses'

# Resultado esperado :

# 3910

# Ejercicio 17:
# Encuentra palabras con alfabetos y números
# Dado :

# str1 = "Chema39 es profesor10 y maker"

# Resultado:

# Chema39 profesor10

# Ejercicio 18:
# Reemplace cada puntuación con # en la siguiente cadena

# Dado :

# str1 = '/*Chema es @profesor & maker!!'

# Resultado:

# ##Chema es #profesor # maker##


