import re
import itertools
import heapq
from collections import defaultdict


class Object:
    def __init__(self, floor, fuel, type):
        self.floor = floor
        self.fuel = fuel
        self.type = type

    def __repr__(self):
        return '{}{}'.format(self.fuel[0].upper(), self.type[0].upper())


class State:
    def __init__(self, objects, elevator):
        self.objects = objects
        self.elevator = elevator
        s = '\n'.join([
            ('x ' if floor == self.elevator else '  ') + '-'.join(sorted(str(o) for o in self.objects if o.floor == floor))
            for floor in reversed(range(4))
        ])
        x = '-' * 20
        self.str = '\n'.join([x, s, x])
        self.hash = hash(self.str)

    @property
    def valid(self):
        for f in range(4):
            microchips = {o.fuel for o in self.objects if o.floor == f and o.type == 'microchip'}
            generators = {o.fuel for o in self.objects if o.floor == f and o.type == 'generator'}
            if generators and microchips.difference(generators):
                return False
        return True

    @property
    def heuristic_to_go(self):
        return sum((3 - o.floor) for o in self.objects) / 2  # each elevator trip can contain two items - thanks Peter Norvig!! http://nbviewer.jupyter.org/url/norvig.com/ipython/Advent%20of%20Code.ipynb#Day-11:-Radioisotope-Thermoelectric-Generators

    @property
    def children(self):
        on_this_floor = [o for o in self.objects if o.floor == self.elevator]
        for next_floor in (self.elevator - 1, self.elevator + 1):
            if 0 <= next_floor <= 3:
                for n_passengers in (1, 2):
                    for passengers in itertools.combinations(on_this_floor, n_passengers):
                        next_objects = [o for o in self.objects if o not in passengers]
                        next_objects += [Object(next_floor, p.fuel, p.type) for p in passengers]
                        s = State(next_objects, next_floor)
                        if s.valid:
                            yield s

    def __hash__(self):
        return self.hash

    def __eq__(self, other):
        return self.str == other.str

    def __lt__(self, other):
        # only here to satisfy heapq - not really necessary
        return self.heuristic_to_go < other.heuristic_to_go

    def __repr__(self):
        return self.str


def solve(start):
    shortest_path_to_state = defaultdict(lambda: 10 ** 999)
    shortest_path_to_state[start] = 0
    frontier = []
    heapq.heappush(frontier, (start.heuristic_to_go, start))

    i = 0
    while frontier:
        est_path_cost, state = heapq.heappop(frontier)

        i += 1
        if i % 10000 == 0:
            print(state)

        if state.heuristic_to_go == 0:
            return shortest_path_to_state[state]

        next_cost = shortest_path_to_state[state] + 1
        for child in state.children:
            if next_cost < shortest_path_to_state[child]:
                heapq.heappush(frontier, (next_cost + child.heuristic_to_go, child))
                shortest_path_to_state[child] = next_cost


objects = []
with open('input.txt', 'r') as fh:
    for floor, description in enumerate(fh):
        objects.extend([Object(floor, fuel, 'microchip') for fuel in re.findall('([a-z]+)-compatible microchip', description)])
        objects.extend([Object(floor, fuel, 'generator') for fuel in re.findall('([a-z]+) generator', description)])

start = State(objects, 0)

print('part 1:', solve(start))

for element in ('elerium', 'dilithium'):
    for kind in ('generator', 'microchip'):
        start.objects.append(Object(0, element, kind))

print('part 2:', solve(start))
