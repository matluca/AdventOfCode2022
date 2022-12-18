#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    points = []
    for line in f.readlines():
        xs, ys, zs = line.strip().split(',')
        x, y, z = int(xs), int(ys), int(zs)
        points.append((x, y, z))
    f.close()
    return points


def are_neighbours(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2]) == 1


def ext_surface(points):
    tot = len(points) * 6
    for i in range(len(points)):
        for j in range(len(points)):
            if are_neighbours(points[i], points[j]):
                tot -= 1
    return tot


def sol1(filename):
    points = get_input(filename)
    return ext_surface(points)


def neighbours(p):
    return [
        (p[0], p[1], p[2] + 1),
        (p[0], p[1], p[2] - 1),
        (p[0], p[1] + 1, p[2]),
        (p[0], p[1] - 1, p[2]),
        (p[0] + 1, p[1], p[2]),
        (p[0] - 1, p[1], p[2]),
    ]


def inbounds(p, max_size):
    return -1 <= p[0] <= max_size and -1 <= p[1] <= max_size and -1 <= p[2] <= max_size


def add_void(points, void, max_size):
    new_void = set()
    for v in void:
        for n in neighbours(v):
            if n not in void and n not in points and inbounds(n, max_size):
                new_void.add(n)
    if len(new_void) == 0:
        return void, True
    return void.union(new_void), False


def sol2(filename):
    points = get_input(filename)
    max_x = max([p[0] for p in points]) + 1
    max_y = max([p[1] for p in points]) + 1
    max_z = max([p[2] for p in points]) + 1
    max_size = max([max_x, max_y, max_z])
    void = set()
    for i in range(-1, max_size):
        for j in range(-1, max_size + 1):
            void.update(set([(-1, i, j), (i, -1, j), (i, j, -1), (max_size, i, j), (i, max_size, j), (i, j, max_size)]))
    end = False
    while not end:
        void, end = add_void(points, void, max_size)
    return ext_surface(list(void)) - 6 * (max_size + 2) * (max_size + 2)


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
