N = int(input())
aux = 0

while(aux < N):
    P,C = input().split(" ")
    C = int(C)
    P = list(P)
    it = 0
    while(it < C):
        esq_desligou = False
        if P[0] == 'X':
            P[0] = 'O'
        else:
            P[0] = 'X'
            esq_desligou = True

        for k in range(1,len(P)):
            if esq_desligou:
                if P[k] == 'O':
                    P[k] = 'X'
                else:
                    P[k] = 'O'
                    esq_desligou = False

        it+=1
    P = ''.join(P)
    print(P)
    aux+=1