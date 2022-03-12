from math import sqrt

# count i backwards from n, nested loops
# i: iterate backwards over j <= i, return first palindrome found, add it to a set 
# get the max of the set for the answer
# there's probably a better way to cut off i to make this faster

def is_palindrome(num: int):
    to_str = str(num)
    for index in range(0, int(len(to_str)/2) + 1): 
        if to_str[index] != to_str[-1-index]:
            return False 
    return True

print(f"1001: {is_palindrome(1001)}")
print(f"1234: {is_palindrome(1234)}")
print(f"12321: {is_palindrome(12321)}")
print(f"3920408: {is_palindrome(3920408)}")
print(f"973379: {is_palindrome(973379)}")

def find_highest_palindrome_multiple(high_factor: int):
    for j in range(high_factor, 0, -1):
        product = j * high_factor
        if is_palindrome(product):
            return product

def solution(ceiling: int):
    palindromes = set()
    for i in range(ceiling, int(sqrt(ceiling)), -1):
        product = find_highest_palindrome_multiple(i)
        if product is not None:
            palindromes.add(product)

    return max(palindromes)

print(solution(100))
print(solution(1000))
