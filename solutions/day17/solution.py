import heapq
from hashlib import md5
from collections import namedtuple

input = 'qljzarfv'
map_size = 4
Position = namedtuple('Position', 'x,y')


def move_func(state):
    path, pos = state
    hash = md5((input + path).encode()).hexdigest()
    for door, h in zip(['U', 'D', 'L', 'R'], hash):
        if h in 'bcdef':
            child_path = path + door
            endpos = trace_path(child_path)
            if 0 <= endpos.x < map_size and 0 <= endpos.y < map_size:
                yield (child_path, endpos)


def h_func(state):
    path, pos = state
    dx = pos.x - goal.x
    dy = pos.y - goal.y
    return abs(dx) + abs(dy)


def trace_path(path):
    _, pos = start
    for step in path:
        if step == 'U':
            pos = Position(pos.x, pos.y - 1)
        elif step == 'D':
            pos = Position(pos.x, pos.y + 1)
        elif step == 'L':
            pos = Position(pos.x - 1, pos.y)
        elif step == 'R':
            pos = Position(pos.x + 1, pos.y)
        else:
            raise RuntimeError("Whoops")

    return pos


def astar(goal, start):
    frontier = [(h_func(start), start)]
    state_to_lowest_cost = {start: 0}

    while frontier:
        cost, state = heapq.heappop(frontier)
        path, pos = state
        if pos == goal:
            return path

        new_cost = cost + 1
        for child in move_func(state):
            if new_cost < state_to_lowest_cost.get(child, 10 ** 999):
                state_to_lowest_cost[child] = new_cost
                heapq.heappush(frontier, (new_cost + h_func(child), child))


def dfs(goal, start):
    frontier = [start]
    max_cost = 0
    while frontier:
        state = frontier.pop()
        path, pos = state
        if pos == goal:
            max_cost = max(max_cost, len(path))
        else:
            for child in move_func(state):
                frontier.append(child)

    return max_cost


start = ('', Position(0, 0))
goal = Position(map_size - 1, map_size - 1)
print('part 1:', astar(goal, start))
print('part 2:', dfs(goal, start))
