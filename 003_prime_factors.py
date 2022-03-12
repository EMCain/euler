import math 

def prime_candidates(max):
    """
    numbers that could be primes
    """
    yield 2
    for i in range(3, max, 2):
        yield i


def get_largest_prime_factor(n: int):
    largest_so_far: int = 0
    for i in prime_candidates(int(math.sqrt(n))+1):
        while (n % i == 0):
            largest_so_far = i
            n = n / i
    return largest_so_far

print(get_largest_prime_factor(13195))
print(get_largest_prime_factor(600851475143))
