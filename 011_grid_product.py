from shared.grid import Grid

test_grid = Grid("data_files/test_number_grid.txt")
print(list(test_grid.get_n_right(3)))
print(list(test_grid.get_n_diag_down(3)))
print(list(test_grid.get_n_diag_up(3)))