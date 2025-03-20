def suma(numero1, numero2):
    """
    Esta es una función para sumar
    
    parametro 1: int
    parametro 2: int
    retur int
    """
    suma = numero1 + numero2
    return suma
try:
    numero1 = int(input("Introduce un número: "))
    numero2 = int(input("Introduce un número: "))
except Exception as e:
    print("Sólo se permiten números", e)  
else:
    print(suma(numero1, numero2))
finally:
    print("Siempre me ejecuto")