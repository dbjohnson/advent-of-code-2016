with open('input.txt', 'r') as fh:
    steps = [line.strip() for line in fh]


def decode(steps, keypad, start=5):
    for i, row in enumerate(keypad):
        for j, col in enumerate(row):
            if col == start:
                x, y = j, i

    code = []
    for step in steps:
        for move in step:
            xx, yy = x, y
            if move == 'R':
                xx += 1
            elif move == 'L':
                xx -= 1
            elif move == 'U':
                yy -= 1
            elif move == 'D':
                yy += 1

            if 0 <= xx < len(keypad[0]) and 0 <= yy < len(keypad) and keypad[xx][yy] is not None:
                x, y = xx, yy

        code.append(keypad[y][x])
    return ''.join(map(str, code))


keypad = [
    [None, None, None, None, None],
    [None, 1,    2,    3,    None],
    [None, 4,    5,    6,    None],
    [None, 7,    8,    9,    None],
    [None, None, None, None, None],
]

print('part 1:', decode(steps, keypad))


keypad = [
    [None,  None,  1, None, None],
    [None,  2,     3,    4,    None],
    [5,     6,     7,    8,    9   ],
    [None, 'A',   'B',  'C',   None],
    [None,  None, 'D', None, None],
]

print('part 2:', decode(steps, keypad))
