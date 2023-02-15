# Tested with Python 3.10.7

def sw_ne_diagonal(x, y):
    return x - y

def sw_ne_diagonal_str(x, y):
    diag = sw_ne_diagonal(x, y)
    return f"{diag: 4d}"

def nw_se_diagonal(x, y):
    return x + y

def nw_se_diagonal_str(x, y):
    diag = nw_se_diagonal(x, y)
    return f"{diag: 4d}"

def vanilla_square(x, y):
        letter = 'ABCDEFGH'[x]
        return f' {letter}{y+1}({x}, {y})'

def print_board(square):
    for y in reversed(range(8)):
        for x in range(8):
            print(square(x, y), end='')
        print()

print_board(nw_se_diagonal_str)
