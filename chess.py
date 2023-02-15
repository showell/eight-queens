# Tested with Python 3.10.7
from collections import defaultdict

def print_board(square, *, n):
    s = "\nY\n"
    for y in reversed(range(n)):
        s += f"{y} "
        for x in range(n):
            s += square(x, y)
        s += "\n"

    s += "  "
    for x in range(n):
        s += f"{x} "

    s += "X\n"
    print(s)

class QueenAttackNet:
    # We keep track of which diagonals and ranks are being attacked by
    # queens. Note that we DO NOT check for attacks along
    # files, since we rely on our caller NEVER to place two
    # queens on the same file.

    def __init__(self):
        self.sw_ne_attacks = defaultdict(int)
        self.nw_se_attacks = defaultdict(int)
        self.rank_attacks = defaultdict(int)

    def add_queen(self, x, y):
        self.sw_ne_attacks[x - y] += 1
        self.nw_se_attacks[x + y] += 1
        self.rank_attacks[y] += 1

    def remove_queen(self, x, y):
        self.sw_ne_attacks[x - y] -= 1
        self.nw_se_attacks[x + y] -= 1
        self.rank_attacks[y] -= 1

    def is_attacked(self, x, y):
        return (
            self.sw_ne_attacks[x - y] or
            self.nw_se_attacks[x + y] or
            self.rank_attacks[y]
        )


class Board:
    def __init__(self, *, n):
        self.queens = []
        self.n = n
        self.attack_net = QueenAttackNet()

    def add_queen_to_next_file(self, y):
        x = len(self.queens)
        self.queens.append(y)
        self.attack_net.add_queen(x, y)

    def remove_last_queen(self):
        y = self.queens.pop()
        x = len(self.queens)
        self.attack_net.remove_queen(x, y)

    def possible_queen_spots(self):
        # We know that any solution has a queen on each file of the board
        x = len(self.queens)

        if x >= self.n:
            return []

        return [y for y in range(self.n) if not self.is_attacked(x, y)]

    def status(self, x, y):
        if x < len(self.queens) and self.queens[x] == y:
            return "Q "
        else:
            return "x " if self.is_attacked(x, y) else "- "

    def is_attacked(self, x, y):
        return self.attack_net.is_attacked(x, y)

    def num_queens(self):
        return len(self.queens)

    def is_done(self):
        return len(self.queens) == self.n

    def coords(self):
        return [(x, y) for x, y in enumerate(self.queens)]

def solve(*, is_done, node_value, child_nodes, add_node, remove_node):
    def run():
        if is_done():
            yield node_value()

        for child_node in child_nodes():
            add_node(child_node)
            for solution in run():
                yield solution

            remove_node()

    for solution in run():
        yield solution

def add_queens_to_board(board):
    for solution in solve(
            is_done=board.is_done,
            node_value=board.coords,
            child_nodes=board.possible_queen_spots,
            add_node=board.add_queen_to_next_file,
            remove_node=board.remove_last_queen):
        yield solution

N = 8
board = Board(n=N)
solutions = list(add_queens_to_board(board))
assert len(solutions) == 92
for solution in solutions:
    print(solution)

print("board is actually empty after our entire traversal!")
print_board(board.status, n=N)
