while(True):

    N = int(input())
    if N == 0:
        break
    matriz = [[0]*N]*N

    for idx in range(N):
        print(matriz)
        pessoa = int(input())
        lista_amigos = list(map(int, input().split()))
        for amigo in lista_amigos:
            matriz[pessoa-1][amigo-1] = 1
    
    print(matriz)