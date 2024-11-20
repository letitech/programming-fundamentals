while True:
    try:
        respuesta = input("Quieres agregar una palabras diccionario? ")
        respuesta = respuesta.lower()
        if respuesta == "si":
            palabra = input("Introduce la palabra: ")
            significado = input("Introduce el significado: ")
            with open("diccionario", "a") as diccionario:
                diccionario.write(f"{palabra}: {significado}\n")
        else:
            break
    except FileNotFoundError:
        open("diccionario.txt", "x")
