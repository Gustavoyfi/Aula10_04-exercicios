listap = []
listai = []
for i in range (0,10):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        listap.append(num)
    else:
        listai.append(num)
print(f"Números Pares: {len(listap)}")
print(f"Números Ímpares: {len(listai)}")


