from xmlrpc.client import Boolean, boolean


class Grid:
    rows = []
    def __init__(self, filepath): 
        print("Hi")
        with open(filepath, "r") as f:
            for row in f.readlines():
                row_data = row.strip().split(" ")
                self.rows.append([int(num) for num in row_data])

    
    def diag_set(self, row: int, col: int, n: int, down: Boolean):
        for i in range(0, n):
            c = col + i
            if down: 
                r = row + i 
            else: 
                r = row - i
            yield self.rows[r][c]


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


    # next: implement similar methods for down, diagonal up, diagonal down 