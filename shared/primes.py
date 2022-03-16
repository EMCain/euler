def first_n_primes(n: int):
    sum, sieve, primes = 0, [True] * (n ** 2), []
    p = 2
    while len(primes) < n:
        if sieve[p]:
            sum += p
            primes.append(p)
            for i in range(p*p, n ** 2, p):
                sieve[i] = False
        p += 1
    return { 'sum': sum, 'primes': primes }

def primes_under_n(n: int):
    # adapted from https://stackoverflow.com/a/18232279
    sum, sieve, primes = 0, [True] * n, []
    for p in range(2, n):
        if sieve[p]:
            sum += p
            primes.append(p)
            for i in range(p*p, n, p):
                sieve[i] = False
    return { 'sum': sum, 'primes': primes }

    