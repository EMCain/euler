sum: int = 0

for i in range(0, 1000):
    if 0 in (i % 3, i % 5):
        sum += i

print(sum)