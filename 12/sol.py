#!/usr/bin/env python3

# This solution basically uses Dijkstra's algorithm for finding the shortest path between nodes in a graph
# https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

def get_input(filename):
    f = open(filename, 'r')
    grid = []
    for line in f.readlines():
        grid.append(list(line.strip()))
    f.close()
    start, end = (0, 0), (0, 0)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                start = (i, j)
                grid[i][j] = 'a'
            if grid[i][j] == 'E':
                end = (i, j)
                grid[i][j] = 'z'
    return grid, start, end


def get_neighbours(cell, size_x, size_y):
    a, b = cell
    neighbours = [(a - 1, b), (a, b - 1), (a + 1, b), (a, b + 1)]
    real_neighbours = []
    for n in neighbours:
        x, y = n
        if 0 <= x < size_x and 0 <= y < size_y:
            real_neighbours.append(n)
    return real_neighbours


def exploration(grid, current_cell, paths, visited_nodes):
    neighbours = get_neighbours(current_cell, len(grid), len(grid[0]))
    for n in neighbours:
        x, y = current_cell
        a, b = n
        if ord(grid[a][b]) >= ord(grid[x][y]) - 1 and n not in visited_nodes:
            if n not in paths.keys():
                paths[n] = paths[current_cell] + 1
            else:
                paths[n] = min(paths[current_cell] + 1, paths[n])
    visited_nodes.add(current_cell)


def get_next_cell(paths, visited_nodes):
    min_d = max(paths.values()) + 1
    next_cell = (-1, -1)
    for node, value in paths.items():
        if node not in visited_nodes and value < min_d:
            next_cell = node
            min_d = value
    return next_cell


def sol1(filename):
    grid, start, end = get_input(filename)
    current_cell = end
    paths = {end: 0}
    visited_nodes = set()
    while True:
        exploration(grid, current_cell, paths, visited_nodes)
        current_cell = get_next_cell(paths, visited_nodes)
        if start in paths.keys():
            return paths[start]


def sol2(filename):
    grid, start, end = get_input(filename)
    current_cell = end
    paths = {end: 0}
    visited_nodes = set()
    while True:
        exploration(grid, current_cell, paths, visited_nodes)
        current_cell = get_next_cell(paths, visited_nodes)
        for k in paths.keys():
            x, y = k
            if grid[x][y] == 'a':
                return paths[k]


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
