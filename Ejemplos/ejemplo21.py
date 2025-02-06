contrasena_valida = "admin"

# for intentos in range(3):
#     contrasena = input("Introduce tu contraseña: ")
#     if contrasena == contrasena_valida:
#         print(f"Bienvenido, número de intentos {intentos + 1}")
#         break
#     else:
#         print("Contraseña incorrecta")

contador = 0

while contador < 3:
    contrasena = input("Introduce tu contraseña: ")
    if contrasena == contrasena_valida:
        print(f"Bienvenido, número de intentos {contador + 1}")
        break
    else:
        print("Contraseña incorrecta")
        contador += 1