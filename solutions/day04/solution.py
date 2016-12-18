import re
from string import ascii_lowercase as alphabet
from collections import defaultdict

with open('input.txt', 'r') as fh:
    rooms = [l.strip() for l in fh]


def hash(name):
    counts = defaultdict(int)
    for c in name.replace('-', ''):
        counts[c] += 1

    count_to_chars = defaultdict(list)
    for char, count in counts.items():
        count_to_chars[count].append(char)

    hash = []
    for count in sorted(count_to_chars, reverse=True):
        hash += sorted(count_to_chars[count])
        if len(hash) >= 5:
            return ''.join(hash[:5])


def parse(room):
    m = re.match('(([a-z]+-)*)([0-9]+){1}\[([a-z]+)\]', room)
    return {
        'name': m.group(1),
        'sector': int(m.group(3)),
        'hash': m.group(4)
    }


def real(room):
    return hash(room['name']) == room['hash']


rooms = [parse(r) for r in rooms]

print('part 1:', sum(r['sector'] for r in rooms if real(r)))


def decrypt(room):
    def shift(c):
        if c == '-':
            return c

        idx = alphabet.index(c)
        idx += room['sector']
        return alphabet[idx % len(alphabet)]

    return ''.join(list(map(shift, room['name'])))


for r in rooms:
    name = decrypt(r)
    if 'north' in name and 'pole' in name:
        print('part 2:', name, r)
