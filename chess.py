# Tested with Python 3.10.7

def vanilla_square(x, y):
        letter = 'ABCDEFGH'[x]
        return f' {letter}{y+1}({x}, {y})'

def print_board(square):
    for y in reversed(range(8)):
        for x in range(8):
            print(square(x, y), end='')
        print()

print_board(vanilla_square)
