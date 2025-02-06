nombre = input("¿Cómo te llamas? ")
pareja = input("traes a tu pareja? ")

if pareja == "si":
    print("Bienvenidos a la fiesta", nombre, "y pareja")
elif pareja == "mas o menos":
    print("Quédate a la espera")
else:
    print("Lo siento", nombre, "no puedes entrar")