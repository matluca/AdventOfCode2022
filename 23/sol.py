#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    elves = []
    i = 0
    for line in f.readlines():
        for c in range(len(line.strip())):
            if line[c] == '#':
                elves.append((i, c))
        i += 1
    f.close()
    return set(elves)


def all_neighbours(pos):
    x, y = pos
    return [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]


def neighbours(pos, d):
    x, y = pos
    if d == 0:
        return [(x-1, y-1), (x-1, y), (x-1, y+1)]
    if d == 1:
        return [(x+1, y-1), (x+1, y), (x+1, y+1)]
    if d == 2:
        return [(x-1, y-1), (x, y-1), (x+1, y-1)]
    if d == 3:
        return [(x-1, y+1), (x, y+1), (x+1, y+1)]


def suggested_position(e, elves, d):
    all_n = all_neighbours(e)
    alone = True
    for n in all_n:
        if n in elves:
            alone = False
            break
    if alone:
        return e
    for dd in range(4):
        direction = (d + dd) % 4
        neighb = neighbours(e, direction)
        free = True
        for n in neighb:
            if n in elves:
                free = False
                break
        if free:
            return neighb[1]
    return e


def sol1(filename):
    elves = get_input(filename)
    d = 0
    for _ in range(10):
        suggested = {}
        suggested_count = {}
        for e in elves:
            new_e = suggested_position(e, elves, d)
            suggested[e] = new_e
            if new_e not in suggested_count.keys():
                suggested_count[new_e] = 0
            suggested_count[new_e] += 1
        new_elves = set([])
        for old, new in suggested.items():
            if suggested_count[new] == 1:
                new_elves.add(new)
            else:
                new_elves.add(old)
        elves = new_elves
        d += 1
    min_x, max_x = min([e[0] for e in elves]), max([e[0] for e in elves])
    min_y, max_y = min([e[1] for e in elves]), max([e[1] for e in elves])
    return (max_x - min_x + 1) * (max_y - min_y + 1) - len(elves)


def sol2(filename):
    elves = get_input(filename)
    d = 0
    r = 1
    while True:
        suggested = {}
        suggested_count = {}
        for e in elves:
            new_e = suggested_position(e, elves, d)
            suggested[e] = new_e
            if new_e not in suggested_count.keys():
                suggested_count[new_e] = 0
            suggested_count[new_e] += 1
        new_elves = set([])
        tot_moves = 0
        for old, new in suggested.items():
            if suggested_count[new] == 1:
                new_elves.add(new)
                if old != new:
                    tot_moves += 1
            else:
                new_elves.add(old)
        if tot_moves == 0:
            return r
        elves = new_elves
        d += 1
        r += 1


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
