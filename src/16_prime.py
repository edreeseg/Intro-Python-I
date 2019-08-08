def sieve_of_eratosthenes(limit):
    p = 2
    l = [False, False] + [True for n in range(2, limit+1)]
    finished = False
    while(not finished):
        finished = True
        i = p**2
        while(i <= limit):
            finished = False
            l[i] = False
            i += p
        for index, value in enumerate(l[p+1:], p+1):
            if (value == True):
                p = index
                break
    return [i for i, prime in enumerate(l) if prime]
print(sieve_of_eratosthenes(100000))