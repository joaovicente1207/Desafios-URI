N = int(input())
i = 0

while (i < N):
    total = 0
    dicionario = dict()
    vazio = input()
    while(True):
        nome = input()
        if len(nome) == 0:
            break
        if nome not in dicionario:
            dicionario[nome] = 1
        else:
            dicionario[nome] += 1

    print(dicionario)
    i+=1
    