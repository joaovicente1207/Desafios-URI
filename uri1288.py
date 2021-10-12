N = int(input())
i = 0

def Mochila(PesoMax, pesos, poderes, n):
  
    if n == 0 or PesoMax == 0 :
        return 0
  
    if (pesos[n-1] > PesoMax):
        return Mochila(PesoMax, pesos, poderes, n-1)
    else:
        return max(poderes[n-1] + Mochila(PesoMax-pesos[n-1], pesos, poderes, n-1),
                   Mochila(PesoMax, pesos, poderes, n-1))

while (i < N):
    M = int(input())
    lista_poder = []
    lista_peso = []
    
    for idx in range(M):
        X,Y = input().split(" ")
        lista_poder.append(int(X))
        lista_peso.append(int(Y))
    
    cargaMax = int(input())
    resistencia = int(input())

    ret = Mochila(cargaMax,lista_peso,lista_poder,M)

    if ret>=resistencia:
        print("Missao completada com sucesso")
    else:
        print("Falha na missao")

    i+=1