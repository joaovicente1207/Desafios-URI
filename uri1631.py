def criaReta(x1,y1,x2,y2):
    m = (y2-y1)/(x2-x1)
    a = -m
    c = m*x1 - y1
    b = 1
    return a,b,c

def distPonto(x1,y1,a,b,c):
    dist = abs(a*x1+b*y1+c)/(a**2 + b**2)**(1/2)
    return dist

while True:
    N = int(input())
    if N == 0:
        break
    
    coord = []
    for i in range(N):
        x,y = input().split(" ")
        coord.append(int(x))
        coord.append(int(y))
    
    
