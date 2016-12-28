def solve(n, steal_fn):
    elves = list(range(1, n + 1))
    while len(elves) > 1:
        elves = steal_fn(elves)

    return elves[0]


def steal_from_neighbor(elves):
    n = len(elves)
    # skip every other elf.  if it's an odd number, we'll handle the wrap below
    elves = elves[:n - 1:2]
    # rotate array for our next round if there are an odd number
    if n % 2:
        return elves[1:] + elves[:1]
    else:
        return elves


def steal_from_opposite(elves):
    # This is tricky, and my original solution was painfully slow.
    # Peter Norvig is smart.
    # http://nbviewer.jupyter.org/url/norvig.com/ipython/Advent%20of%20Code.ipynb#Day-19-An-Elephant-Named-Joseph
    n = len(elves)
    i = 0
    while i < max(1, n // 2):
        # the offset required to get to the opposite elf changes as we elimate
        # Here 'i' is used to indicate how many elves have been eliminated so far
        opposite = (n // 2) + i
        elves[i + opposite] = 0
        i += 1
        n -= 1

    # rotate array for the next round
    rotated = elves[i:] + elves[:i]
    return list(filter(None, rotated))

n = 3005290
print('part 1:', solve(n, steal_from_neighbor))
print('part 2:', solve(n, steal_from_opposite))
