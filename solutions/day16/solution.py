flip = str.maketrans('01', '10')


def dragon(s):
    return s + '0' + ''.join(reversed(s)).translate(flip)


def checksum(s):
    c = ''.join('1' if s[i] == s[i + 1] else '0' for i in range(0, len(s) - 1, 2))
    return c if len(c) % 2 else checksum(c)


def fill(disk, length):
    while len(disk) < length:
        disk = dragon(disk)
    return disk[:length]


input = '01110110101001000'
print('part 1:', checksum(fill(input, 272)))
print('part 2:', checksum(fill(input, 35651584)))
