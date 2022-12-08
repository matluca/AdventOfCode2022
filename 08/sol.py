#!/usr/bin/env python3

def get_grid(filename):
    f = open(filename, 'r')
    grid = []
    for line in f.readlines():
        grid_line = []
        line = line.strip()
        for c in line:
            grid_line.append(int(c))
        grid.append(grid_line)
    f.close()
    return grid


def is_visible(x, y, grid):
    if x == 0 or x == len(grid)-1 or y == 0 or y == len(grid)-1:
        return True
    right = grid[x][y+1:]
    left = grid[x][:y]
    up = [row[y] for row in grid][:x]
    down = [row[y] for row in grid][x+1:]
    return grid[x][y] > max(right) or grid[x][y] > max(left) or grid[x][y] > max(up) or grid[x][y] > max(down)


def get_scenic_score(x, y, grid):
    if x == 0 or x == len(grid)-1 or y == 0 or y == len(grid)-1:
        return 0
    up, down, left, right = 0, 0, 0, 0
    for i in range(x):
        up += 1
        if grid[x-i-1][y] >= grid[x][y]:
            break
    for i in range(x+1, len(grid)):
        down += 1
        if grid[i][y] >= grid[x][y]:
            break
    for j in range(y):
        left += 1
        if grid[x][y-j-1] >= grid[x][y]:
            break
    for j in range(y+1, len(grid)):
        right += 1
        if grid[x][j] >= grid[x][y]:
            break
    return up * down * left * right


def sol1(filename):
    grid = get_grid(filename)
    tot = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if is_visible(i, j, grid):
                tot += 1
    return tot


def sol2(filename):
    grid = get_grid(filename)
    max_score = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            scenic_score = get_scenic_score(i, j, grid)
            if scenic_score > max_score:
                max_score = scenic_score
    return max_score


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
