with open('input.txt') as fh:
    moves = fh.read().strip().split(', ')


class State:
    __directions__ = ['N', 'E', 'S', 'W']

    def __init__(self, direction, x, y):
        self.direction = direction
        self.x = x
        self.y = y

    def turn(self, turn):
        idx = State.__directions__.index(self.direction)
        idx += 1 if turn == 'R' else -1
        direction = State.__directions__[idx % len(State.__directions__)]
        return State(direction, self.x, self.y)

    def step(self, dist=1):
        if self.direction == 'N':
            return State(self.direction, self.x + dist, self.y)
        if self.direction == 'S':
            return State(self.direction, self.x - dist, self.y)
        if self.direction == 'E':
            return State(self.direction, self.x, self.y + dist)
        if self.direction == 'W':
            return State(self.direction, self.x, self.y - dist)

    def distance(self, x=0, y=0):
        return abs(self.x - x) + abs(self.y - y)

    @property
    def location(self):
        return (self.x, self.y)

    def __repr__(self):
        return 'x: {}, y: {}, direction: {}'.format(self.x, self.y, self.direction)


s = State(direction='N', x=0, y=0)
for move in moves:
    s = s.turn(move[0])
    s = s.step(int(move[1:]))

print('part 1:', s.distance())


s = State(direction='N', x=0, y=0)
visited = {s}
for move in moves:
    s = s.turn(move[0])
    for _ in range(int(move[1:])):
        s = s.step()
        if s.location in visited:
            print('part 2:', s.distance())
            quit()
        visited.add(s.location)
