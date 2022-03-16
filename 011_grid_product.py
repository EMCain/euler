import functools 
import operator

from shared.grid import Grid

def get_largest_product(grid: Grid, n: int):
    rt = grid.get_n_right(n)
    dd = grid.get_n_diag_down(n)
    du = grid.get_n_diag_up(n)
    do = grid.get_n_down(n)

    max = 0

    for item in [rt, dd, du, do]:
        for num_tuple in item: 
            product = functools.reduce(operator.mul, num_tuple)
            if product > max:
                max = product
    return max


test_grid = Grid("data_files/test_number_grid.txt")
# print(list(test_grid.get_n_right(2)))
# print(list(test_grid.get_n_diag_down(2)))
# print(list(test_grid.get_n_diag_up(2)))
# print(list(test_grid.get_n_down(2)))

print(f"Max product of 2 items for the test grid is {get_largest_product(test_grid, 2)}")

answer_grid = Grid("data_files/011_number_grid.txt")
print(f"Max product of 4 items for the main answer grid is {get_largest_product(answer_grid, 4)}")
