password = input("Introduce la contraseña: ")
is_not_valid = True

while is_not_valid:
    if len(password) < 8:
        print("La contraseña es demasiado corta.")
        password = input("Introduce la contraseña de nuevo: ")
    elif password.isalpha():
        print("La contraseña debe contener números.")
        password = input("Introduce la contraseña de nuevo: ")
    else:
        is_not_valid = False
else:
    print("La contraseña es válida.")