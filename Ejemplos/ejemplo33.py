menu = """
Bienvenido al sistema de registro de usuarios, elige una opción:

    1. Registrarse
    2. Iniciar sesión
    3. Salir
"""

opcion = "0"

while opcion != "3":
    print(menu)
    opcion = input("Introduce una opción: ")
    
    if opcion == "1":
        print("Registro de usuario")
        usuario = input("Introduce tu usuario: ")
        contrasena = input("Introduce tu contraseña: ")
        with open("usuario.txt", "w") as archivo:
            archivo.write(usuario + "," + contrasena)
    elif opcion == "2":
        print("Iniciar sesión")
        usuario = input("Introduce tu usuario: ")
        contrasena = input("Introduce tu contraseña: ")
        
        with open("usuario.txt", "r") as archivo:
            usuario_archivo, contrasena_archivo = archivo.read().split(",")
            
            if usuario == usuario_archivo and contrasena == contrasena_archivo:
                print("Bienvenido")
                break
            else:
                print("Usuario o contraseña incorrectos")
        
    elif opcion == "3":
        break