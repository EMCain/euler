import math
from time import sleep
# adapting some code from 003_prime_factors

def prime_candidates(max):
    """
    numbers that could be primes
    """
    yield 2
    for i in range(3, max+1, 2):
        yield i

def count_prime_factors(n: int):
    factors = {}
    for i in prime_candidates(n):
        while (n % i == 0):
            if i not in factors: 
                factors[i] = 1
            else: 
                factors[i] += 1
            n = n / i
    return factors

def make_divisible(product, prime, exponent):
    """
    multiply by the prime until it is divisible by prime to the power of exponent
    """
    while product % (math.pow(prime, exponent)) != 0:
        product *= prime
    return product

make_divisible(6, 5, 2)

def get_lowest_common_multiple(num: int):
    product = 1
    # iterate over numbers up to num 
    for i in range(2, num):
        factors = count_prime_factors(i)
        # for each, see if each factor to the power of its value in the prime factors dict goes into the product
        for (prime, exponent) in factors.items(): 
            # if not, multiply by the factor until it does 
            product = make_divisible(product, prime, exponent) 

    return product 

print(get_lowest_common_multiple(10))
print(get_lowest_common_multiple(20))