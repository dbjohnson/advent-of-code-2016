with open('input.txt', 'r') as fh:
    rules = sorted([
        tuple(map(int, line.split('-')))
        for line in fh
    ])


def unblocked(rules):
    i = 0
    for low, high in rules:
        yield from range(i, low)
        i = max(i, high + 1)


print('part 1:', next(unblocked(rules)))
print('part 2:', len(list(unblocked(rules))))
