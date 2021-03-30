def sieve(n:int):
    a = [True] * (n+1) 
    i = 2
    while i*i <= n:
        if a[i]:
            for j in range(i*2,n+1,i):
                a[j] = False
        i+=1
    count:int = 0
    for i in range(3,n-1,2):
        if a[i] and a[i+2]:
            count+=1
    print(count)

sieve(1_000_000_000_000)