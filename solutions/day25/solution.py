import re
from itertools import cycle


def instructions():
    with open('input.txt', 'r') as fh:
        for line in fh:
            yield re.match('(?P<inst>[a-z]+) (?P<src>[a-d]|-?[0-9]+) ?(?P<tgt>[a-d]|-?[0-9]+)?', line).groupdict()


def process(registers, instructions):
    def _value(key):
        try:
            return registers[key]
        except KeyError:
            return int(key)

    i = 0
    processed = 0
    while 0 <= i < len(instructions):
        processed += 1
        if processed > 1e6:
            return False

        # blech
        if i < len(instructions) - 6:
            seq = instructions[i: i + 6]
            if [ix['inst'] for ix in seq] == ['cpy', 'inc', 'dec', 'jnz', 'dec', 'jnz'] and \
               [_value(ix['tgt']) for i, ix in enumerate(seq) if i in (3, 5)] == [-2, -5] and \
               all([seq[idx]['src'] == seq[idx - 1]['src'] for idx in (3, 5)]):
                registers[seq[1]['src']] += _value(seq[0]['src']) * _value(seq[4]['src'])
                registers[seq[0]['tgt']] = 0
                registers[seq[4]['src']] = 0
                i += 6

        inst = instructions[i]
        if inst['inst'] == 'jnz' and _value(inst['src']) != 0:
            i += _value(inst['tgt'])
        elif inst['inst'] == 'tgl':
            idx = i + _value(inst['src'])
            i += 1
            if 0 <= idx < len(instructions):
                ix = instructions[idx]
                if ix['tgt'] is None:
                    ix['inst'] = 'dec' if ix['inst'] == 'inc' else 'inc'
                else:
                    ix['inst'] = 'cpy' if ix['inst'] == 'jnz' else 'jnz'
        else:
            i += 1
            if inst['inst'] == 'cpy':
                registers[inst['tgt']] = _value(inst['src'])
            if inst['inst'] == 'inc':
                registers[inst['src']] += 1
            if inst['inst'] == 'dec':
                registers[inst['src']] -= 1
            if inst['inst'] == 'out':
                yield _value(inst['src'])


def solve():
    for i in range(10 ** 999):
        print(i)
        registers = dict(a=i, b=0, c=0, d=0)
        outputs = process(registers, list(instructions()))
        c = cycle((0, 1))
        for x, (expected, actual) in enumerate(zip(c, outputs)):
            if expected != actual:
                break
            if x > 100:
                return i

print('part 1:', solve())
