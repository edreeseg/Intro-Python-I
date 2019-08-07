def sieve_of_eratosthenes(limit):
    p = 2
    l = [False, False] + [True for n in range(2, limit+1)]
    print(l)
    isFinished = False
    while(isFinished == False):
        isFinished = True
        i = p**2
        while(i <= limit):
            isFinished = False
            l[i] = False
            i += p
        for i, n in enumerate(l, p + 1):
            if (n == True):
                p = i
                break
    print(l)
sieve_of_eratosthenes(20)