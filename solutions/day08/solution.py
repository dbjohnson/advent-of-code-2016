import re


h = 6
w = 50

display = [
    [0] * w
    for row in range(h)
]


with open('input.txt', 'r') as fh:
    instructions = [line.strip() for line in fh]


def process(instruction, display, debug=False):
    if instruction.startswith('rect'):
        x, y = map(int, re.match(r'.*?([0-9]+)x([0-9]+)', instruction).groups())
        for row in range(y):
            display[row][:x] = [1] * x

    elif instruction.startswith('rotate column'):
        col, shift = map(int, re.match(r'.*?([0-9]+) by ([0-9]+)', instruction).groups())
        vals = [display[row][col] for row in range(h)]
        for row in range(h):
            display[row][col] = vals[(row - shift) % h]

    elif instruction.startswith('rotate row'):
        row, shift = map(int, re.match(r'.*?([0-9]+) by ([0-9]+)', instruction).groups())
        vals = [display[row][col] for col in range(w)]
        for col in range(w):
            display[row][col] = vals[(col - shift) % w]

    return display


def show(display):
    rendered = '\n'.join(map(lambda x: ''.join(map(str, x)), display))
    rendered = rendered.replace('0', ' ').replace('1', '#')
    print(rendered)


for instruction in instructions:
    display = process(instruction, display)


print('part 1:', sum(map(sum, display)))
print('part 2:')
show(display)
