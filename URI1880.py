T = int(input())

decimais = []
for i in range(T):
    decimais.append(int(input()))


def converte(decimal,base):
    numero_base = []
    atual = decimal
    i = 0
    while(atual >= base):
        i+=1
        numero_base.append(atual%base)
        atual = int(atual/base)
    numero_base.append(atual)
    return numero_base,i


def palindromo(numero,i):
    certo = True
    aux = 0
    while aux < i/2:
        if numero[aux] != numero[i-aux]:
            certo = False
        aux+=1
    return certo


for num in decimais:
    i = 2
    tam = 0
    nenhum = True
    lista_de_base = []
    while i <=16:
        a,b = converte(num,i)
        if palindromo(a,b):
            nenhum = False
            lista_de_base.append(i)
            tam +=1
        i+=1
    if nenhum:
        print("-1")
    else:
        for k in range(tam):
            if k+1 != tam:
                print(f'{lista_de_base[k]} ', end="")
            else:
                print(f'{lista_de_base[k]}')


