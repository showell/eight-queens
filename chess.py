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
        self.nw_se_attacks = defaultdict(int)
        self.file_attacks = defaultdict(int)
        self.rank_attacks = defaultdict(int)

    def add_queen(self, x, y):
        self.queens.append((x, y))
        self.sw_ne_attacks[sw_ne_diagonal(x, y)] += 1
        self.nw_se_attacks[nw_se_diagonal(x, y)] += 1
        self.file_attacks[x] += 1
        self.rank_attacks[y] += 1

    def can_add_queen(self, x, y):
        return (x, y) not in self.queens and not self.is_attacked(x, y)

    def next_queen_spot(self):
        # We know that any solution has a queen on each rank of the board
        y = len(self.queens)

        # TODO: stop hard coding 8
        for x in range(8):
            if self.can_add_queen(x, y):
                return (x, y)

        return None

    def status(self, x, y):
        if (x, y) in self.queens:
            return "Q "
        else:
            return "x " if self.is_attacked(x, y) else "- "

    def num_attacks_on(self, x, y):
        # similar to is_attacked, but useful for debugging actual counts
        # (we may end up deleting this later)
        return (
            self.sw_ne_attacks[sw_ne_diagonal(x, y)] +
            self.nw_se_attacks[nw_se_diagonal(x, y)] +
            self.file_attacks[x] +
            self.rank_attacks[y]
        )

    def is_attacked(self, x, y):
        return (
            self.sw_ne_attacks[sw_ne_diagonal(x, y)] or
            self.nw_se_attacks[nw_se_diagonal(x, y)] or
            self.file_attacks[x] or 
            self.rank_attacks[y]
        )


board = Board()
board.add_queen(0, 0)
queen_loc2 = board.next_queen_spot()
print(f"Added queen to {queen_loc2}")
board.add_queen(*queen_loc2)
print_board(board.status)
