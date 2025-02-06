contrasena = input("Introduce la contraseña: ")
validacion = False

while not(validacion):
    if len(contrasena) < 8:
        print("La contraseña debe contener un mínimo de 8 caracteres")
        contrasena = input("Introduce la contraseña: ")
    elif contrasena.isalpha() or contrasena.isdigit():
        print("La contraseña debe combinar letras y números")
        contrasena = input("Introduce la contraseña: ")
    elif contrasena.islower() or contrasena.isupper():
        print("La contraseña debe combinar mayúsculas y minúsculas")
        contrasena = input("Introduce la contraseña: ")
    else:
        print("La contraseña es válida")
        validacion = True
        