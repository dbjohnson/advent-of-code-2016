import re
import operator
from functools import reduce


class Bot:
    __refs_by_name__ = {}

    def __init__(self, name):
        Bot.__refs_by_name__[name] = self
        self.name = name
        self.chips = []

    def receive(self, chip):
        assert len(self.chips) < 2, 'Each bot can only hold two chips!'
        self.chips.append(chip)

    def get(self, high_or_low):
        if high_or_low == 'hi':
            chip = max(self.chips)
        else:
            chip = min(self.chips)

        self.chips.remove(chip)
        return chip

    @classmethod
    def by_name(cls, name):
        return Bot.__refs_by_name__.get(name) or Bot(name)


def execute_instruction(s):
    if s.startswith('value'):
        m = re.search('([0-9]+) goes to (bot [0-9]+)', s)
        Bot.by_name(m.group(2)).receive(int(m.group(1)))
        return True
    else:
        m = re.search('(bot [0-9]+) gives low to (output [0-9]+|bot [0-9]+) and high to (output [0-9]+|bot [0-9]+)', s)
        b = Bot.by_name(m.group(1))
        if len(b.chips) < 2:
            return

        if set(b.chips) == {61, 17}:
            print('part 1:', b.name)

        Bot.by_name(m.group(2)).receive(b.get('lo'))
        Bot.by_name(m.group(3)).receive(b.get('hi'))
        return True


with open('input.txt', 'r') as fh:
    instructions = [line.strip() for line in fh]


while instructions:
    executed = []
    for s in instructions:
        if execute_instruction(s):
            executed.append(s)

    for s in executed:
        instructions.remove(s)

prod = reduce(operator.mul, [Bot.by_name('output {}'.format(i)).chips[0] for i in range(3)], 1)
print('part 2:', prod)
