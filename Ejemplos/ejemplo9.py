numero1 = int(input("Ingresa un número: "))
numero2 = int(input("Ingresa otro número: "))
numero3 = int(input("Ingresa otro número: "))

# if numero1 > numero2 and numero1 > numero3:
#     print("El mayor es:", numero1)
# elif numero2 > numero3:
#     print("El mayor es:", numero2)
# else:
#     print("El mayor es:", numero3)
    
def mayor_de_tres(numero1, numero2, numero3):
    if numero1 > numero2 and numero1 > numero3:
        return numero1
    elif numero2 > numero3:
        return numero2
    else:
        return numero3

def orden_descendente(numero1, numero2, numero3):
    if numero1 > numero2 and numero1 > numero3:
        if numero2 > numero3:
            return numero1, numero2, numero3
        else:
            return numero1, numero3, numero2
    elif numero2 > numero3:
        if numero1 > numero3:
            return numero2, numero1, numero3
        else:
            return numero2, numero3, numero1
    else:
        if numero1 > numero2:
            return numero3, numero1, numero2
        else:
            return numero3, numero2, numero1
            
def informacion_personal(nombre, edad = "edad desconocida"):
    print(f"Tu nombre es {nombre} y tienes {edad} años")
    
# informacion_personal("Santos")

mayor = orden_descendente(numero1, numero2, numero3)
print(mayor)