import re


with open('input.txt', 'r') as fh:
    instructions = [
        re.match('(?P<inst>[a-z]+) (?P<src>[a-d]|-?[0-9]+) ?(?P<tgt>[a-d]|-?[0-9]+)?', line).groupdict()
        for line in fh
    ]


def solve(registers, instructions):
    def _value(key):
        try:
            return registers[key]
        except KeyError:
            return int(key)

    i = 0
    while 0 <= i < len(instructions):
        inst = instructions[i]
        if inst['inst'] == 'jnz' and _value(inst['src']):
            i += _value(inst['tgt'])
        else:
            i += 1
            if inst['inst'] == 'cpy':
                registers[inst['tgt']] = _value(inst['src'])
            if inst['inst'] == 'inc':
                registers[inst['src']] += 1
            if inst['inst'] == 'dec':
                registers[inst['src']] -= 1


registers = dict(a=0, b=0, c=0, d=0)
solve(registers, instructions)
print('part 1:', registers['a'])

registers = dict(a=0, b=0, c=1, d=0)
solve(registers, instructions)
print('part 2:', registers['a'])
