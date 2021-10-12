while(True):
    h1,m1,h2,m2 = input().split(" ")
    h1 = int(h1)
    m1 = int(m1)
    h2 = int(h2)
    m2 = int(m2)

    if(h1 == m1 == h2 == m2 == 0): break

    tempo = (h2-h1)*60 + (m2-m1)
    if tempo<0:
        tempo+=60*24
    print(tempo)