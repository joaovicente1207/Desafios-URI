def SumAscii(name):
    total = 0
    for letter in name:
        total = total + ord(letter)
    return total

def SumVector(vector):
    total = 0
    sum_vector = []
    for i in vector:
        total = total + i
        sum_vector.append(total)
    return sum_vector

while(True):
    N = int(input())
    if N==0:
        break
    else:
        names = []
        power = []
        for i in range(N):
            name = input()
            names.append(name)
            power.append(SumAscii(name))

        inverse_power = power[::-1] #list reverse

        power_direct = SumVector(power)
        power_reverse = SumVector(inverse_power)

        [12, 7, 8, 4]
        [12, 19, 27, 31]
        


        


        



              

            

        


