import re


class Disc:
    def __init__(self, **kwargs):
        self.__dict__ = kwargs

    @staticmethod
    def from_description(description):
        regexp = 'Disc #(?P<number>[0-9]+) has (?P<positions>[0-9]+) positions; at time=0, it is at position (?P<pos_t0>[0-9]+)'
        return Disc(**{
            k: int(v)
            for k, v in re.match(regexp, description).groupdict().items()
        })

    def aligned(self, t):
        return (self.pos_t0 + t) % self.positions == 0


def solve(discs):
    for t in range(10 ** 999):
        if all(d.aligned(t + d.number) for d in discs):
            return t


with open('input.txt', 'r') as fh:
    discs = [
        Disc.from_description(line)
        for line in fh
    ]

print('part 1:', solve(discs))

discs.append(Disc(number=len(discs) + 1, positions=11, pos_t0=0))
print('part 2:', solve(discs))
