password = input("Introduce una contraseña: ")
special = "@#$%^&*./"
count1 = 0
count2 = 0
validation = True
while validation:
    if len(password) < 8:
        print("La contraseña debe tener al menos 8 caracteres")
        password = input("Introduce una contraseña válida: ")
    else:
        if password.islower() == True or password.isupper() == True:
            print("La contraseña debe tener una combinación de mayúsculas y minúsculas")
            password = input("Introduce una contraseña válida: ")
        
        for i in password:
            if i.isnumeric():
                count1 += 1
        for i in special:
            if i in password:
                count2 += 1
        
        if count1 < 1 or count2 < 1:
            print("La contraseña debe tener una combinación de valores numéricos y caracteres especiales")
            password = input("Introduce una contraseña válida: ")
        else:
            validation = False
else:
    print("La contraseña es válida, Bienvenido")               
        
        