# Ejercicio 5:
# Cuente todas las minúsculas, mayúsculas, dígitos y símbolos especiales de una cadena determinada


# Dado :

# str1 = "C@#he26ma^&Du5ran"

# Resultado esperado :

# Recuentos totales de caracteres, dígitos y símbolos 

# Caracteres = 10 
# Dígitos = 3 
# Símbolo = 4

srt1 = "C@#he26ma^&Du5ran"
cdig = 0
cndig = 0
csmb = 0
for x in range(len(srt1)):
    if (srt1[x].isdigit()):
        cdig+=1
    elif (srt1[x].islower() or srt1[x].isupper()):
        cndig+=1
    else:
        csmb+=1
        
print(" Caracteres: ", cndig, "\n","Dígitos: ", cdig,"\n","Símbolos: ",csmb )
        