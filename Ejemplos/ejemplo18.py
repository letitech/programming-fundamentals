cadena = "Hola mundo"
letra = "a"
contador = 0
palabras = cadena.split()

for palabra in palabras:
    if letra in palabra:
        contador += 1
        
print(contador)