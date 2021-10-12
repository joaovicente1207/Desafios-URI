while(True):
    A,B = input().split(" ")
    A = int(A) 
    B = int(B)
    if(A == B == 0): break
    deck_a = list(map(int, input().split()))
    deck_b = list(map(int, input().split()))

    cartas = [0]*500000


    n = 0
    m = 0


    for i in range(A):
        if cartas[deck_a[i]] == 0:
            cartas[deck_a[i]] = 1
            n+=1
    
    for i in range(B):
        if cartas[deck_b[i]] == 0:
            cartas[deck_b[i]] = 2
            m+=1
        else:
            if cartas[deck_b[i]] != 3:
                if cartas[deck_b[i]] != 2:
                    n-=1
                    cartas[deck_b[i]] = 3
 


    if n > m:
        print(m)
    else:
        print(n)
                

    


    
