loop = int(input())
for i in range(loop):
    a = int(input())
    b = a % 1000
    c = int((a - b) / 1000)
    sum = 0
    if b >= 399:
        c += 1
    elif b < 300:
        pass
    else:
        sum += int((b - 299) * ((b + 300) + c * 2000)/2)
    #Summation of 300-399 is 34950
    sum += 34950*c+(50000*(c-1)*c)
    print(sum)