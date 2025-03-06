def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista
                
                
lista = [1,3,7,4,9,32,87,45,23]

print(ordenamiento_burbuja(lista))