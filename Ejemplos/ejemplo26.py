diccionario = dict()

usuario = ""

while usuario != "1":
    usuario = input("Introduce las palabras en español e ingés: ")
    if usuario != "1":
        usuario = usuario.split(":")
        diccionario[usuario[0]] = usuario[1]
else:
    frase = input("Introduce la frase en español: ")
    for espanol, ingles in diccionario.items():
        frase = frase.replace(espanol, ingles)
    print(frase)    