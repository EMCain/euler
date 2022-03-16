from shared.primes import primes_under_n

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

def sum_of_primes_under(n: int):
    return primes_under_n(n)["sum"]

print(sum_of_primes_under(10))
print(sum_of_primes_under(2000000))