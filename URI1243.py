def analisar(palavra,ultimo):
    aceita = True
    for letra in palavra:
        ordem = ord(letra)
        if (ordem >= 65 and ordem <= 90) or (ordem >= 97 and ordem <= 122):
            pass
        else:
            aceita = False
            return False

    return aceita

while True: 
    try:
        palavras = list(map(str, input().split(" ")))
        qtd = 0
        media = 0
        it = 0
        tam = len(palavras)
        while it < tam:
            if it == tam - 1:
                aceita = analisar(palavras[it],True)

            else:
                aceita = analisar(palavras[it],False)
            if aceita:
                qtd+=1
                media = media + len(palavras[it])
            it+=1

        if qtd == 0:
            media = 0
        else:
            media = int(media/qtd)

        if media <=3:
            print(250)
        elif media > 3 and media <=5:
            print(500)
        else:
            print(1000)

    except EOFError:
        break