lista = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6]
nummaior = []
for i in lista:
    nummaior.append(lista.count(i))
rep = lista[nummaior.index(max(nummaior))]
print(f"Mais repetido foi o: {rep}")