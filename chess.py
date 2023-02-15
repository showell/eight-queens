# Tested with Python 3.10.7

def sw_ne_diagonal(x, y):
    return x - y

def nw_se_diagonal(x, y):
    return x + y

def print_board(square):
    for y in reversed(range(8)):
        for x in range(8):
            print(square(x, y), end='')
        print()

class Board:
    def __init__(self):
        self.queens = []

    def add_queen(self, x, y):
        self.queens.append((x, y))

    def status(self, x, y):
        if (x, y) in self.queens:
            return "Q "
        else:
            return "_ "


board = Board()
board.add_queen(5, 3)
board.add_queen(7, 0)
print_board(board.status)
