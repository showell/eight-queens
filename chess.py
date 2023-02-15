# Tested with Python 3.10.7
from collections import defaultdict

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

    def is_attacked(self, x, y):
        return self.attack_net.is_attacked(x, y)

    def is_done(self):
        return len(self.queens) == self.n

    def coords(self):
        return [(x, y) for x, y in enumerate(self.queens)]

def visit(*, child_nodes, visit_child, unvisit_child):
    def visit_subtree():
        yield None

        for child_node in child_nodes():
            visit_child(child_node)
            for checkpoint in visit_subtree():
                yield None

            unvisit_child()
            yield None

    for solution in visit_subtree():
        yield None

def add_queens_to_board(board):
    for checkpoint in visit(
            child_nodes=board.possible_queen_spots,
            visit_child=board.add_queen_to_next_file,
            unvisit_child=board.remove_last_queen):
        if board.is_done():
            yield board.coords()

N = 8
board = Board(n=N)
solutions = list(add_queens_to_board(board))
assert len(solutions) == 92

print("DONE!!!!!")
