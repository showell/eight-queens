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

print("OK")
