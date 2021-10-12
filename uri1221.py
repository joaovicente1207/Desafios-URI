N = int(input())
idx = 0

while(idx < N):
    X = int(input())
    met = int(X/2)
    div = 2
    rest = 0
    flag = False
    while (div < met):
        rest = X%div
        met = X/div
        if (rest == 0):
            print("Not Prime")
            flag = True
            break
        else:
            div+=1
    if not flag:
        print("Prime")


    idx+=1