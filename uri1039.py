while True:
    try:
        r1,x1,y1,r2,x2,y2 = input().split(" ")
        r1 = int(r1)
        x1 = int(x1)
        y1 = int(y1)
        r2 = int(r2)
        x2 = int(x2)
        y2 = int(y2)

        dist = ((x2-x1)**2 + (y2-y1)**2)**(1/2)

        if dist + r2 > r1:
            print("MORTO")
        else:
            print("RICO")
    except EOFError:
        break