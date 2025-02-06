contrasena = input("Introduce la contraseña: ")

if len(contrasena) < 8:
    print("La contraseña debe contener un mínimo de 8 caracteres")
elif contrasena.isalpha() or contrasena.isdigit():
    print("La contraseña debe combinar letras y números")
elif contrasena.islower() or contrasena.isupper():
    print("La contraseña debe combinar mayúsculas y minúsculas")
else:
    print("La contraseña es válida")