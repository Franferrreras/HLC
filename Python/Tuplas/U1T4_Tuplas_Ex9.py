# Ejercicio 9

# Cuenta el número de apariciones del elemento 50 de una tupla

# tupla = (50, 10, 60, 70, 50)

# Resultado:

# 2

tupla = (50, 10, 60, 70, 50)
count = 0
for i in range(len(tupla)):
    if (tupla[i] == 50 ):
        count += 1
        
        
print(count)
    
