diccionario = dict()

opcion = input("Quieres agregar una palabra? ")

while opcion != "no":
    palabra = input("Introduce la palabra: ")
    traduccion = input("Introduce la traducción: ")
    diccionario[palabra] = traduccion
    opcion = input("Quieres agregar palabra otra palabra? ")
else:
    frase = input("Ingresa una frase en español: ")
    for i in diccionario.keys():
        if i in frase:
            frase = frase.replace(i, diccionario[i])
    print(frase)            

def funcion():
    pass            
        
    