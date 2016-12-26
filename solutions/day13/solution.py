import math
import heapq
from collections import namedtuple

favorite_number = 1350
Position = namedtuple('Position', 'x,y')


def is_open(x, y):
    if x < 0 or y < 0:
        return False

    val = x * x + 3 * x + 2 * x * y + y + y * y + favorite_number
    ones = 0
    while val:
        ones += val % 2
        val >>= 1

    return (ones % 2) == 0


def h_func(position):
    dx = position.x - goal.x
    dy = position.y - goal.y
    return math.sqrt(dx * dx + dy * dy)


def move_func(p):
    for child in (Position(x=p.x - 1, y=p.y),
                  Position(x=p.x + 1, y=p.y),
                  Position(x=p.x, y=p.y - 1),
                  Position(x=p.x, y=p.y + 1)):
        if is_open(child.x, child.y):
            yield child


def astar(goal, start):
    position_to_shortest_path = {start: 0}
    frontier = [(h_func(start), start)]

    while frontier:
        cost, pos = heapq.heappop(frontier)
        if pos == goal:
            return position_to_shortest_path[pos]

        new_cost = position_to_shortest_path[pos] + 1
        for child in move_func(pos):
            if new_cost < position_to_shortest_path.get(child, 10 ** 999):
                position_to_shortest_path[child] = new_cost
                heapq.heappush(frontier, (new_cost + h_func(child), child))


goal = Position(x=31, y=39)
start = Position(x=1, y=1)
print('part 1:', astar(goal, start))


frontier = [(0, start)]
visited = set()
visited.add(start)
while frontier:
    steps, pos = frontier.pop()
    new_cost = steps + 1
    if new_cost <= 50:
        for child in move_func(pos):
            if child not in visited:
                visited.add(child)
                frontier.append((new_cost, child))

print('part 2:', len(visited))
