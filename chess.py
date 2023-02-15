# Tested with Python 3.10.7
from collections import defaultdict

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
        self.sw_ne_attacks = defaultdict(int)

    def add_queen(self, x, y):
        self.queens.append((x, y))
        self.sw_ne_attacks[sw_ne_diagonal(x, y)] += 1

    def status(self, x, y):
        if (x, y) in self.queens:
            return "Q "
        else:
            num_attacks = self.sw_ne_attacks[sw_ne_diagonal(x, y)]
            return f"{num_attacks} "


board = Board()
board.add_queen(5, 3)
board.add_queen(7, 0)
print_board(board.status)
