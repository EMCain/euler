def fibonacci(max):
    first = 1
    second = 1
    while first <= max: 
        yield first
        new = first + second 
        first = second 
        second = new 

print(list(fibonacci(90)))

sum = 0

for item in fibonacci(4000000):
    if item % 2 == 0:
        sum += item 

print(sum)