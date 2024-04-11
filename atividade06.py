listaf = []
listad = []
for i in range (0,10):
    num = int(input("Digite um número: "))
    if num >=10 and num<= 20:
        listad.append(num)
    else:
        listaf.append(num)
print(f"Números dentro: {len(listad)}")
print(f"Números fora: {len(listaf)}")