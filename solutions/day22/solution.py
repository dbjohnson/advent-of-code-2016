import re
import itertools
import heapq
from collections import namedtuple


Node = namedtuple('Node', 'x,y,used,available,size')


with open('input.txt', 'r') as fh:
    nodes = [Node(
        x=int(re.search('x([0-9]+)', line).groups()[0]),
        y=int(re.search('y([0-9]+)', line).groups()[0]),
        used=int(re.findall('([0-9]+)T', line)[1]),
        available=int(re.findall('([0-9]+)T', line)[2]),
        size=int(re.findall('([0-9]+)T', line)[0])
    )
        for line in fh
        if line.startswith('/dev')
    ]


def viable_pairs(nodes):
    for a, b in itertools.permutations(nodes, 2):
        if 0 < a.used <= b.available:
            yield a, b


print('part 1:', sum(1 for v in viable_pairs(nodes)))


def h_func(state):
    data_pos, empty_pos = state
    return city_block_dist(data_pos, goal)


def city_block_dist(a, b):
    dx = a.x - b.x
    dy = a.y - b.y
    return abs(dx) + abs(dy)


def move_func(state):
    data_pos, empty = state
    for node in neighbors[empty]:
        if node.used <= empty.size:
            # swap node with empty
            empty_next = node
            data_pos_next = empty if node == data_pos else data_pos
            yield data_pos_next, empty_next


def astar(goal, start):
    frontier = [(h_func(start), start)]
    state_to_lowest_cost = {start: 0}

    while frontier:
        cost, state = heapq.heappop(frontier)
        data_pos, empty_pos = state
        if city_block_dist(data_pos, goal) == 0:
            return cost

        new_cost = state_to_lowest_cost[state] + 1
        for child in move_func(state):
            if new_cost < state_to_lowest_cost.get(child, 10 ** 999):
                state_to_lowest_cost[child] = new_cost
                heapq.heappush(frontier, (new_cost + h_func(child), child))


neighbors = {
    node: [n for n in nodes if city_block_dist(n, node) == 1]
    for node in nodes
}

goal = next(n for n in nodes if n.x == 0 and n.y == 0)
start = max(nodes, key=lambda n: -1 if n.y else n.x)
empty = next(n for n in nodes if n.used == 0)
print('part 2:', astar(goal, (start, empty)))
