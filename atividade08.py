num = int(input("Digite um número: "))
print(f"OS divisores de {num} é: ")
for i in range(1, num + 1):
    if num % i == 0:
        print(f"{i}")