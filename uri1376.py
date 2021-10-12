while True:
    N, R, C, K = map(int,input().split(" "))

    # encerra o programa
    if (N == R == C == K == 0):
        break
    
    # inicializa a matriz do reino
    mapaReino = []
    mapaReino2 = []
    for i in range(R):
        mapaReino.append(list(map(int,input().split(" "))))
        mapaReino2.append(mapaReino[i].copy())

    # para cada batalha, percorre todos municipios do reino
    for x in range(K):
        for y in range(R):
            for z in range(C):
                #tratando os casos de bordas
                if y == 0:
                    if z == 0:
                        #direita
                        if (mapaReino[y][z] +1 == mapaReino[y][z+1] or (mapaReino[y][z] == N-1 and mapaReino[y][z+1] == 0)):
                            mapaReino2[y][z+1] = mapaReino[y][z]
                        #baixo
                        if (mapaReino[y][z] +1 == mapaReino[y+1][z] or (mapaReino[y][z] == N-1 and mapaReino[y+1][z] == 0)):
                            mapaReino2[y+1][z] = mapaReino[y][z]
                    elif z == C-1:
                        #baixo
                        if (mapaReino[y][z] +1 == mapaReino[y+1][z] or (mapaReino[y][z] == N-1 and mapaReino[y+1][z] == 0)):
                            mapaReino2[y+1][z] = mapaReino[y][z]
                        #esquerda
                        if (mapaReino[y][z] +1 == mapaReino[y][z-1] or (mapaReino[y][z] == N-1 and mapaReino[y][z-1] == 0)):
                            mapaReino2[y][z-1] = mapaReino[y][z]
                    else:
                        #direita
                        if (mapaReino[y][z] +1 == mapaReino[y][z+1] or (mapaReino[y][z] == N-1 and mapaReino[y][z+1] == 0)):
                            mapaReino2[y][z+1] = mapaReino[y][z]
                        #baixo
                        if (mapaReino[y][z] +1 == mapaReino[y+1][z] or (mapaReino[y][z] == N-1 and mapaReino[y+1][z] == 0)):
                            mapaReino2[y+1][z] = mapaReino[y][z]
                        #esquerda
                        if (mapaReino[y][z] +1 == mapaReino[y][z-1] or (mapaReino[y][z] == N-1 and mapaReino[y][z-1] == 0)):
                            mapaReino2[y][z-1] = mapaReino[y][z]
                elif y == R-1:
                    if z == 0:
                        #cima
                        if (mapaReino[y][z] +1 == mapaReino[y-1][z] or (mapaReino[y][z] == N-1 and mapaReino[y-1][z] == 0)):
                            mapaReino2[y-1][z] = mapaReino[y][z]
                        #direita
                        if (mapaReino[y][z] +1 == mapaReino[y][z+1] or (mapaReino[y][z] == N-1 and mapaReino[y][z+1] == 0)):
                            mapaReino2[y][z+1] = mapaReino[y][z]
                    elif z == C-1:
                        #cima
                        if (mapaReino[y][z] +1 == mapaReino[y-1][z] or (mapaReino[y][z] == N-1 and mapaReino[y-1][z] == 0)):
                            mapaReino2[y-1][z] = mapaReino[y][z]
                        #esquerda
                        if (mapaReino[y][z] +1 == mapaReino[y][z-1] or (mapaReino[y][z] == N-1 and mapaReino[y][z-1] == 0)):
                            mapaReino2[y][z-1] = mapaReino[y][z]
                    else:
                        #cima
                        if (mapaReino[y][z] +1 == mapaReino[y-1][z] or (mapaReino[y][z] == N-1 and mapaReino[y-1][z] == 0)):
                            mapaReino2[y-1][z] = mapaReino[y][z]
                        #direita
                        if (mapaReino[y][z] +1 == mapaReino[y][z+1] or (mapaReino[y][z] == N-1 and mapaReino[y][z+1] == 0)):
                            mapaReino2[y][z+1] = mapaReino[y][z]
                        #esquerda
                        if (mapaReino[y][z] +1 == mapaReino[y][z-1] or (mapaReino[y][z] == N-1 and mapaReino[y][z-1] == 0)):
                            mapaReino2[y][z-1] = mapaReino[y][z]
                else:
                    if z == 0:
                        #cima
                        if (mapaReino[y][z] +1 == mapaReino[y-1][z] or (mapaReino[y][z] == N-1 and mapaReino[y-1][z] == 0)):
                            mapaReino2[y-1][z] = mapaReino[y][z]
                        #direita
                        if (mapaReino[y][z] +1 == mapaReino[y][z+1] or (mapaReino[y][z] == N-1 and mapaReino[y][z+1] == 0)):
                            mapaReino2[y][z+1] = mapaReino[y][z]
                        #baixo
                        if (mapaReino[y][z] +1 == mapaReino[y+1][z] or (mapaReino[y][z] == N-1 and mapaReino[y+1][z] == 0)):
                            mapaReino2[y+1][z] = mapaReino[y][z]
                    elif z == C-1:
                        #cima
                        if (mapaReino[y][z] +1 == mapaReino[y-1][z] or (mapaReino[y][z] == N-1 and mapaReino[y-1][z] == 0)):
                            mapaReino2[y-1][z] = mapaReino[y][z]
                        #baixo
                        if (mapaReino[y][z] +1 == mapaReino[y+1][z] or (mapaReino[y][z] == N-1 and mapaReino[y+1][z] == 0)):
                            mapaReino2[y+1][z] = mapaReino[y][z]
                        #esquerda
                        if (mapaReino[y][z] +1 == mapaReino[y][z-1] or (mapaReino[y][z] == N-1 and mapaReino[y][z-1] == 0)):
                            mapaReino2[y][z-1] = mapaReino[y][z]
                    else:
                        #cima
                        if (mapaReino[y][z] +1 == mapaReino[y-1][z] or (mapaReino[y][z] == N-1 and mapaReino[y-1][z] == 0)):
                            mapaReino2[y-1][z] = mapaReino[y][z]
                        #direita
                        if (mapaReino[y][z] +1 == mapaReino[y][z+1] or (mapaReino[y][z] == N-1 and mapaReino[y][z+1] == 0)):
                            mapaReino2[y][z+1] = mapaReino[y][z]
                        #baixo
                        if (mapaReino[y][z] +1 == mapaReino[y+1][z] or (mapaReino[y][z] == N-1 and mapaReino[y+1][z] == 0)):
                            mapaReino2[y+1][z] = mapaReino[y][z]
                        #esquerda
                        if (mapaReino[y][z] +1 == mapaReino[y][z-1] or (mapaReino[y][z] == N-1 and mapaReino[y][z-1] == 0)):
                            mapaReino2[y][z-1] = mapaReino[y][z]
    
        
        mapaReino = []
        for i in range(R):
            mapaReino.append(mapaReino2[i].copy())
    
    for i in range(R):
            print(*mapaReino2[i], sep=" ");