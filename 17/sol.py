#!/usr/bin/env python3

rocks = [
    [(2, 0), (3, 0), (4, 0), (5, 0)],
    [(3, 0), (2, 1), (3, 1), (4, 1), (3, 2)],
    [(2, 0), (3, 0), (4, 0), (4, 1), (4, 2)],
    [(2, 0), (2, 1), (2, 2), (2, 3)],
    [(2, 0), (3, 0), (2, 1), (3, 1)]
]


def get_input(filename):
    f = open(filename, 'r')
    pushes = list(f.read().strip())
    f.close()
    return pushes


def jet(rock, push, occupied):
    push_dir = 1
    if push == '<':
        push_dir = -1
    new_rock = []
    for p in rock:
        if p[0] + push_dir < 0 or p[0] + push_dir > 6:
            return rock, False
        new_p = (p[0] + push_dir, p[1])
        if new_p in occupied:
            return rock, False
        new_rock.append(new_p)
    return new_rock, False


def down(rock, occupied):
    new_rock = []
    for p in rock:
        new_p = (p[0], p[1] - 1)
        if new_p in occupied:
            return rock, True
        new_rock.append(new_p)
    return new_rock, False


def sol1(filename):
    pushes = get_input(filename)
    max_height = 0
    push = 0
    occupied = set([(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0)])
    for n in range(2022):
        rock_initial = rocks[n % 5]
        rock = []
        for p in rock_initial:
            rock.append((p[0], p[1] + max_height + 4))
        stop = False
        while not stop:
            rock, stop = jet(rock, pushes[push % len(pushes)], occupied)
            if stop:
                for s in rock:
                    occupied.add(s)
                max_height = max([p[1] for p in occupied])
                break
            push += 1
            rock, stop = down(rock, occupied)
            if stop:
                for s in rock:
                    occupied.add(s)
                max_height = max([p[1] for p in occupied])
                break
    return max_height


def list_to_string(l):
    s = ''
    for i in range(6):
        if i in l:
            s += '#'
        else:
            s += '.'
    return s


def sol2(filename):
    pushes = get_input(filename)
    max_height = 0
    push = 0
    occupied = set([(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0)])
    n = 0
    setup = {}
    height = {}
    while True:
        key = ''
        for i in range(10): # keep track of the last 10 lines of the board
            key += list_to_string([p[0] for p in occupied if p[1] == max_height-i])
        if (n % 5, push, key) in setup.keys() and max_height > 100:
            a, height_a = setup[(n % 5, push, key)]
            b, height_b = n, max_height
            n_repeats = int((1000000000000 - b) / (b - a))
            remaining = (1000000000000 - b) % (b - a)
            extra_height = height[a+remaining] - height[a]
            return height_b + n_repeats*(height_b - height_a) + extra_height
        setup[(n % 5, push, key)] = (n, max_height)
        height[n] = max_height
        rock_initial = rocks[n % 5]
        rock = []
        for p in rock_initial:
            rock.append((p[0], p[1] + max_height + 4))
        stop = False
        while not stop:
            rock, stop = jet(rock, pushes[push % len(pushes)], occupied)
            if stop:
                for s in rock:
                    occupied.add(s)
                max_height = max([p[1] for p in occupied])
                break
            push += 1
            if push == len(pushes):
                push = 0
            rock, stop = down(rock, occupied)
            if stop:
                for s in rock:
                    occupied.add(s)
                max_height = max([p[1] for p in occupied])
                break
        n += 1


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')