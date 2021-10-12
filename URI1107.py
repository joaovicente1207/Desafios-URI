while(True):
    A,C = input().split(" ")
    A = int(A) 
    C = int(C)
    if(A == C == 0): break
    final = list(map(int, input().split(" ")))
    inicial = [A]*C
    ligado = False
    lig_num = 0

    feixe = A - final[0]
    lig_num = feixe
    for i in range(C-1):
        if final[i+1]-final[i] >= 0:
            feixe = A - final[i+1]
        elif final[i+1]-final[i] < 0:
            feixe = A - final[i+1]
            lig_num = lig_num - (final[i+1]-final[i])

    print(lig_num)