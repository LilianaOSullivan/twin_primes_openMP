def sieve_of_eratosthenes(N):
    sieve = [True for every number in range 0 .. N]
    i = 2
    for i=2; i*i <= N; ++i:
        if sieve[i] == True:
            for j=i*2; j<N ;j+=i:
                sieve[j] = False
    return sieve

def twin_prime_count(sieve):
    count = 0
    for i=3; i<n ;i+=2:
        if sieve[i] == True and sieve[i+2] == True:
            count+=1
    return count

