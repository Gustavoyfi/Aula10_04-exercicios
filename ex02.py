#imprimer elementos de um vetor qualquer:
#criando um vetor:
vetor = ["azul", "branco", "verde", "vermelho"]
for cor in vetor:
    print(cor)
#fazendo de outra forma(caso precise de indice)
for i in range(0,len(vetor)):
    print(f"Elemento {i+1}: Valor: {vetor[i]}")