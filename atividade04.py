idade = []
while True:
    cont = str(input("Para continuar a inserir idades escreva (S) e para sair escvra (N): "))
    if cont == "S":
        idade2 = int(input("Informe idades: "))
        idade.append(idade2)
    else:
        idade4 = sum(idade)/len(idade)
        print(f"A média das idades é {idade4}")
        break


