#Diccionario español
menu = """
    Diccionario español
    1. Agregar palabra
    2. Buscar palabra
    3. Salir
"""
opcion = "0"

diccionario = dict()

while opcion != "3":
    print(menu)
    opcion = input("Opción: ")
    
    if opcion == "1":
        palabra = input("Ingresa la palabra: ").lower()
        significado = input("Ingresa el significado: ")
        diccionario[palabra] = significado
    elif opcion == "2":
        palabra = input("Ingresa la palabra: ").lower()
        print(diccionario[palabra])