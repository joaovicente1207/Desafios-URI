while(True):
    B,N = input().split(" ")
    B = int(B) 
    N = int(N)
    if(B == N == 0): break

    reserva = list(map(int, input().split(" ")))

    op = []
    for i in range(N):
        lista = list(map(int, input().split(" ")))
        op.append(lista)
    
    negativado = False

    for i in range(N):
        reserva[op[i][0]-1] = reserva[op[i][0]-1] - op[i][2]
        reserva[op[i][1]-1] = reserva[op[i][1]-1] + op[i][2]

    for i in range(B):
        if reserva[i] < 0:
            negativado = True
            break
    
    if negativado == True:
        print("N")
    else:
        print("S")
