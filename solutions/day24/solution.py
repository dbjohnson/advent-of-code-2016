import heapq
import re


with open('input.txt', 'r') as fh:
    maze = tuple(
        line.strip()
        for line in fh
    )

locations = {
    m.group(): (m.start(), y)
    for y, line in enumerate(maze)
    for m in re.finditer('[0-9]+', line)
}

start_pos = locations.pop('0')
locations = tuple(locations.values())


def move_func(state):
    pos, locations = state
    x, y = pos
    for xx, yy in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
        if 0 <= xx < len(maze[0]) and 0 <= yy < len(maze) and maze[yy][xx] != '#':
            next_pos = xx, yy
            next_locations = tuple(pos for pos in locations if pos != next_pos)
            yield next_pos, next_locations


def h_func(state):
    pos, locations_to_visit = state
    if locations_to_visit:
        return min(city_block_dist(pos, loc) for loc in locations_to_visit)
    else:
        return 0


def city_block_dist(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return abs(dx) + abs(dy)


def astar(start, move_func, h_func):
    frontier = [(h_func(start), start)]
    state_to_min_cost = {start: 0}
    while frontier:
        est_cost, state = heapq.heappop(frontier)
        if h_func(state) == 0:
            return state_to_min_cost[state]

        child_cost = state_to_min_cost[state] + 1
        for child in move_func(state):
            if child_cost < state_to_min_cost.get(child, 10 ** 999):
                state_to_min_cost[child] = child_cost
                heapq.heappush(frontier, (child_cost + h_func(child), child))


print('part 1:', astar((start_pos, locations), move_func, h_func))


def h_func_part_2(state):
    pos, locations_to_visit = state
    if locations_to_visit:
        return min(city_block_dist(pos, loc) for loc in locations_to_visit)
    else:
        return city_block_dist(pos, start_pos)


print('part 2:', astar((start_pos, locations), move_func, h_func_part_2))
