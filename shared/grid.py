class Grid:
    rows = []
    number_of_columns = 0

    def __init__(self, filepath): 
        print("Hi")
        with open(filepath, "r") as f:
            for row in f.readlines():
                row_data = row.strip().split(" ")
                if len(row_data) > self.number_of_columns:
                    # This doesn't really account for rows of varying length
                    # if we ever have to deal with them, it would be good to add some Null values to the end of shorter rows.
                    self.number_of_columns = len(row_data)
                self.rows.append([int(num) for num in row_data])

    
    def diag_set(self, row: int, col: int, n: int, down: bool):
        for i in range(0, n):
            try:
                c = col + i
                if down: 
                    r = row + i 
                else: 
                    r = row - i
                yield self.rows[r][c]
            except IndexError:
                raise ValueError(f"Row {c}, Col {c} out of range (overall grid size {len(self.number_of_columns)} x {len(self.rows)})")


    def get_n_right(self, n: int):
        if n < 1:
            raise ValueError("n must be at least 1")
        offset = n - 1
        for row in self.rows:
            for i in range(0, len(row) - offset):
                yield tuple(row[i:i+n])

    def get_n_diag_down(self, n: int):
        if n < 1:
            raise ValueError("n must be at least 1")
        offset = n - 1
        for r in range(0, len(self.rows) - offset):
            row = self.rows[r]
            for c in range(0, len(row) - offset):
                yield tuple(self.diag_set(r, c, n, True))

    def get_n_diag_up(self, n: int):
        if n < 1:
            raise ValueError("n must be at least 1")
        offset = n - 1
        for r in range(offset, len(self.rows)):
            row = self.rows[r]
            for c in range(0, len(row) - offset):
                yield tuple(self.diag_set(r, c, n, False))

    def get_n_down(self, n: int): 
        if n < 1:
            raise ValueError("n must be at least 1")
        offset = n - 1 
        for r1 in range(0, len(self.rows) - offset):
            for c in range(0, self.number_of_columns):
                output = []
                for r2 in range(0, n):
                    output.append(self.rows[r1 + r2][c])
                yield tuple(output)


    # next: implement similar methods for down, diagonal up, diagonal down 