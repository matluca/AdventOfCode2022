#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    data = f.read()
    f.close()
    grid = []
    grid_raw, mov_raw = data.split('\n\n')
    for line in grid_raw.split('\n'):
        grid_line = {}
        for i in range(len(line)):
            if line[i] != ' ':
                grid_line[i] = line[i]
        grid.append(grid_line)
    i = 0
    movs = []
    while i < len(mov_raw):
        if mov_raw[i] in ['L', 'R']:
            movs.append(mov_raw[i])
            i += 1
        else:
            next_l, next_r = len(mov_raw), len(mov_raw)
            if 'L' in mov_raw[i:]:
                next_l = mov_raw[i:].index('L') + i
            if 'R' in mov_raw[i:]:
                next_r = mov_raw[i:].index('R') + i
            next_dir = min(next_l, next_r)
            movs.append(mov_raw[i:next_dir])
            i = next_dir
    return grid, movs


def move_right(pos, grid, steps):
    i, j = pos
    for s in range(steps):
        next_j = j+1
        if next_j not in grid[i].keys():
            next_j = min(grid[i].keys())
        if grid[i][next_j] == '#':
            break
        j = next_j
    return i, j


def move_left(pos, grid, steps):
    i, j = pos
    for s in range(steps):
        next_j = j-1
        if next_j not in grid[i].keys():
            next_j = max(grid[i].keys())
        if grid[i][next_j] == '#':
            break
        j = next_j
    return i, j


def move_down(pos, grid, steps):
    i, j = pos
    for s in range(steps):
        next_i = i+1
        if next_i == len(grid):
            next_i = 0
        if j not in grid[next_i].keys():
            next_i = 0
            while j not in grid[next_i].keys():
                next_i += 1
        if grid[next_i][j] == '#':
            break
        i = next_i
    return i, j


def move_up(pos, grid, steps):
    i, j = pos
    for s in range(steps):
        next_i = i-1
        if next_i == -1:
            next_i = len(grid) - 1
        if j not in grid[next_i].keys():
            next_i = len(grid) - 1
            while j not in grid[next_i].keys():
                next_i -= 1
        if grid[next_i][j] == '#':
            break
        i = next_i
    return i, j


def sol1(filename):
    grid, movs = get_input(filename)
    pos = (0, min(grid[0].keys()))
    d = 0
    for mov in movs:
        if not mov.isnumeric():
            if mov == 'R':
                d = (d + 1) % 4
            elif mov == 'L':
                d = (d - 1) % 4
        else:
            if d == 0:
                pos = move_right(pos, grid, int(mov))
            elif d == 1:
                pos = move_down(pos, grid, int(mov))
            elif d == 2:
                pos = move_left(pos, grid, int(mov))
            elif d == 3:
                pos = move_up(pos, grid, int(mov))
    return 1000*(pos[0] + 1) + 4*(pos[1] + 1) + d


def sol2(filename):
    _ = get_input(filename)
    return 0


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
