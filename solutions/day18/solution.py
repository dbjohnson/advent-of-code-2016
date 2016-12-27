input = '^^^^......^...^..^....^^^.^^^.^.^^^^^^..^...^^...^^^.^^....^..^^^.^.^^...^.^...^^.^^^.^^^^.^^.^..^.^'


def child(parents):
    return '^' if parents in {'^^.', '.^^', '^..', '..^'} else '.'


def next_row(row):
    padded = '.' + row + '.'
    return ''.join([
        child(''.join(triplet))
        for triplet in zip(padded, padded[1:], padded[2:])
    ])


def safe_tile_count(nrows):
    row = input[:]
    count = 0
    for _ in range(nrows):
        count += row.count('.')
        row = next_row(row)
    return count


print('part 1:', safe_tile_count(40))
print('part 2:', safe_tile_count(400000))
