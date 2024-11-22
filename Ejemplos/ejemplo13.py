menu = """
    1. Consultar una palabra
    2. Agregar nueva palabra
    3. Actualizar palabra
    4. Eliminar palabra
    5. Salir
"""
print(menu)
opcion = input("Qué operación quieres realizar? ")
while opcion != "5":
    try:
        if opcion == "1":
            palabra = input("Introduce la palabra: ")
            with open("diccionario.txt", "r") as diccionario:
                contenido = diccionario.read()
                contenido = contenido.split("\n")
                diccionario2 = {}
                for busqueda in contenido:
                    lista = busqueda.split(":")
                    diccionario2[lista[0]] = lista[1]
                print(f"{palabra}: {diccionario2[palabra]}")
                print(menu)
                opcion = input("Qué operación quieres realizar? ")
        if opcion == "2":
            palabra = input("Introduce la palabra: ")
            significado = input("Introduce el significado: ")
            with open("diccionario.txt", "a", encoding="utf-8") as diccionario:
                diccionario.write(f"{palabra}: {significado}\n")
                print(menu)
                opcion = input("Qué operación quieres realizar? ")
    except FileNotFoundError:
        open("diccionario.txt", "x")
