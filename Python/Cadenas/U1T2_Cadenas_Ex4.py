# Ejercicio 4:
# Dada una cadena de entrada con la combinación de mayúsculas y minúsculas,organice los caracteres de tal manera que todas las letras minúsculas deben ir primero.
# Dado :

# str1 = ChEmaDUraN

# Resultado:

# hmaraCEDUN

str1 = "ChEmaDUraN"
srt2 = ""
cd = ""

for x in range(0, len(str1)):
    if (str1[x].islower()):
        srt2+=str1[x]
    else:
        cd+=str1[x]
            
print(srt2 + cd)