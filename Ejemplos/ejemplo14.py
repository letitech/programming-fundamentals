lista = []
for i in range(15):
    if i <= 0:
        lista.append(0)
    elif i == 1:
        lista.append(i)
    else:
        lista.append(lista[i - 2] + lista[i - 1])
    
print(lista)