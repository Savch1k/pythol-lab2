def f(n):
    return sorted({x for i in range(2,int(n**0.5)+1) if n % i == 0 for x in (i,n//i)})

for i in range(452021,10**10):
    if len(f(i))>2:
        if min(f(i))>0 and max(f(i))>0:
            m=min(f(i))+max(f(i))
        if m%7==3:
            print(i,m)
            input()