try:
    archivo = open("C:/Users/CENA/Documents", "w+")
    nombres = ["Santos\n", "Federico\n", "Dina"]
    archivo.write("Hola mundo\n")
    archivo.writelines(nombres)
    print(archivo.read())
except FileNotFoundError:
    print("El archivo no existe")
finally:
    archivo.close()