def sum_of_squares(num): 
    squares = [pow(x, 2) for x in range(1, num + 1)]
    return sum(squares)

def square_of_sum(num): 
    sum_of_nums = (num + 1) * num / 2
    return pow(sum_of_nums, 2)

def difference(num):
    return int(square_of_sum(num) - sum_of_squares(num))

print(difference(10))
print(difference(100))