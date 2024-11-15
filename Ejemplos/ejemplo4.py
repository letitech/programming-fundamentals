print("Bienvenido al sistema del cagero automático")
try:
    archivo = open("contrasena.txt", "r+")
    contenido = archivo.read()
    if contenido == "":
        print("Es la primera vez que accedes al sistema, necesitas una contraseña para cualquier acción")
        contrasena = input("Introduce una contraseña: ")
        archivo.write(contrasena)
    else:
        contrasena = input("Introduce tu contraseña: ")
        while contrasena != contenido:
            contrasena = input("La contraseña no es váilida, inténtalo de nuevo: ")
        else:
            print("Contraseña válida, Bienvenido")
except FileNotFoundError:
    print("No se encontró el archivo")
