a = 16**18 * 4**10 - 46 - 16
k = 0
while a>0:
    if a%4==3:
        k+=1
    a=a//4
print(k)