def first_n_primes(n):
    primes = [2]
    i = 3
    while len(primes) < n:
        is_prime = True
        for existing_prime in primes:
            if i % existing_prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
        i += 2
    
    return primes

print(first_n_primes(6))
print(first_n_primes(10001)[-1])