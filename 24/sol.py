#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    grid = []
    for line in f.readlines():
        grid.append(list(line.strip()))
    f.close()
    return grid


def get_neighbours(node, grid, end):
    pos, t = node
    x, y = pos
    all_neighbours = [(x, y), (x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    neighbours = []
    for p in all_neighbours:
        if p == end or p == (0, 1):
            neighbours.append((p, t+1))
            continue
        a, b = p
        if a <= 0 or a >= len(grid)-1 or b <= 0 or b >= len(grid[0])-1:
            continue
        if grid[(a-t-2) % (len(grid)-2) + 1][b] == 'v':
            continue
        if grid[(a+t) % (len(grid)-2) + 1][b] == '^':
            continue
        if grid[a][(b-t-2) % (len(grid[0])-2) + 1] == '>' or grid[a][(b+t) % (len(grid[0])-2) + 1] == '<':
            continue
        neighbours.append(((a, b), t+1))
    return neighbours


def exploration(grid, current, paths, visited_nodes, end):
    neighbours = get_neighbours(current, grid, end)
    for n in neighbours:
        if n not in visited_nodes:
            if n not in paths.keys():
                paths[n] = paths[current] + 1
            else:
                paths[n] = min(paths[current] + 1, paths[n])
    visited_nodes.add(current)


def get_next(paths, visited):
    min_d = max(paths.values()) + 1
    next_node = ((-1, -1), -1)
    for node, value in paths.items():
        if node not in visited and value < min_d:
            next_node = node
            min_d = value
    return next_node


def min_path(raw_grid, start, end, start_time):
    grid = {}
    for i in range(len(raw_grid)):
        grid[i] = {}
        for j in range(len(raw_grid[i])):
            grid[i][j] = raw_grid[i][j]
    current = (start, start_time)
    paths = {current: 0}
    visited = set()
    while True:
        exploration(grid, current, paths, visited, (len(grid)-1, len(grid[0])-2))
        current = get_next(paths, visited)
        for key in paths.keys():
            if end == key[0]:
                return paths[key]


def sol1(filename):
    grid = get_input(filename)
    return min_path(grid, (0, 1), (len(grid)-1, len(grid[0])-2), 0)


def sol2(filename):
    grid = get_input(filename)
    trip_1 = min_path(grid, (0, 1), (len(grid)-1, len(grid[0])-2), 0)
    trip_2 = min_path(grid, (len(grid)-1, len(grid[0])-2), (0, 1), trip_1)
    trip_3 = min_path(grid, (0, 1), (len(grid)-1, len(grid[0])-2), trip_1 + trip_2)
    return trip_1 + trip_2 + trip_3


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
