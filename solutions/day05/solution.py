from hashlib import md5


key = 'ojvtpuvg'


def test(d, num_zeros=5):
    hash = md5((key + str(d)).encode()).hexdigest()
    if hash.startswith('0' * num_zeros):
        return hash


def part1(length=8):
    password = ''
    d = 0
    while len(password) < length:
        hash = test(d)
        if hash:
            password += hash[5]
        d += 1

    return password


print('part 1:', part1())


def part2(length=8):
    password = [None] * 8
    d = 0
    while not all(password):
        hash = test(d)
        if hash:
            try:
                position = int(hash[5])
                if position < length and not password[position]:
                    password[position] = hash[6]
            except ValueError:
                pass

        d += 1

    return ''.join(password)


print('part 2:', part2())
