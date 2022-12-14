#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    segments = []
    for line in f.readlines():
        points = line.strip().split(' -> ')
        for i in range(len(points)-1):
            a, b = points[i].split(',')
            x, y = points[i+1].split(',')
            segments.append(((int(a), int(b)), (int(x), int(y))))
    f.close()
    occupied = set()
    for segment in segments:
        p1, p2 = segment
        a, b = p1
        x, y = p2
        if a == x:
            for j in range(min(b, y), max(b, y)+1):
                occupied.add((a, j))
        if b == y:
            for i in range(min(a, x), max(a, x)+1):
                occupied.add((i, b))
    return occupied


def new_sand_grain(occupied, y_max):
    pos = (500, 0)
    while True:
        a, b = pos
        if b > y_max:
            return occupied, True
        if (a, b+1) not in occupied:
            pos = (a, b+1)
            continue
        if (a-1, b+1) not in occupied:
            pos = (a-1, b+1)
            continue
        if (a+1, b+1) not in occupied:
            pos = (a+1, b+1)
            continue
        break
    occupied.add(pos)
    return occupied, False


def new_sand_grain_2(occupied, y_max):
    pos = (500, 0)
    while True:
        a, b = pos
        if b == y_max + 1:
            break
        if (a, b+1) not in occupied:
            pos = (a, b+1)
            continue
        if (a-1, b+1) not in occupied:
            pos = (a-1, b+1)
            continue
        if (a+1, b+1) not in occupied:
            pos = (a+1, b+1)
            continue
        break
    occupied.add(pos)
    if pos == (500, 0):
        return occupied, True
    return occupied, False


def sol1(filename):
    occupied = get_input(filename)
    y_max = max([p[1] for p in occupied])
    out_of_bounds = False
    tot = 0
    while not out_of_bounds:
        tot += 1
        occupied, out_of_bounds = new_sand_grain(occupied, y_max)
    return tot - 1


def sol2(filename):
    occupied = get_input(filename)
    y_max = max([p[1] for p in occupied])
    end = False
    tot = 0
    while not end:
        tot += 1
        occupied, end = new_sand_grain_2(occupied, y_max)
    return tot


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
