import itertools

with open('input.txt', 'r') as fh:
    triangles = [
        list(map(int, line.strip().split()))
        for line in fh
    ]


def valid(triangle):
    total = sum(triangle)
    for sides in itertools.combinations(triangle, 2):
        s = sum(sides)
        if s <= total - s:
            return False
    return True


print('part 1:', len(list(filter(valid, triangles))))


transposed = [
    t[i]
    for i in range(3)
    for t in triangles
]

tri2 = [
    transposed[i * 3:(i + 1) * 3]
    for i in range(len(transposed) // 3)
]

print('part 2:', len(list(filter(valid, tri2))))
