lista = [1,2,3,4,5,6,7,8,9,10]
k = 5
n = 10
acomulado = 0
total = 0
for idx in range(1,n):
    if lista[idx+1] > lista[idx]:
        if acomulado < 5:
            acomulado+=1
        if acomulado == 5:
            

