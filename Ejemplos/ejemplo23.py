menu = """
Bienvenido al sistema, seleccione una opción:
    1. Registrarse
    2. Iniciar sesión
    3. Salir
"""

opcion = "0"

usuario = ""
contrasena = ""

while opcion != "3":
    print(menu)
    opcion = input("Opción: ")
    
    if opcion == "1":
        print("Registro de usuario")
        usuario = input("Introduce tu usuario: ")
        contrasena = input("Introduce tu contraseña: ")
    elif opcion == "2":
        print("Inicio de sesión")
        usuario_introducido = input("Introduce tu usuario: ")
        contrasena_introducida = input("Introduce tu contraseña: ")
        if usuario_introducido == usuario and contrasena_introducida == contrasena:
            print("Bienvenido")
            break
        else:
            print("Usuario o contraseña incorrectos")