#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    pairs = []
    data = f.read()
    for d in data.split('\n\n'):
        d1, d2 = d.split('\n')
        pairs.append((eval(d1), eval(d2)))
    f.close()
    return pairs


def check_right_order(a, b):
    if type(a) is int and type(b) is int:
        if a != b:
            return a < b
        else:
            return None
    if type(a) is int:
        return check_right_order([a], b)
    if type(b) is int:
        return check_right_order(a, [b])
    for i in range(max(len(a), len(b))):
        if i == len(a) and i != len(b):
            return True
        if i == len(b) and i != len(a):
            return False
        res = check_right_order(a[i], b[i])
        if res is not None:
            return res
    return False


def sol1(filename):
    pairs = get_input(filename)
    tot = 0
    for i in range(len(pairs)):
        a, b = pairs[i]
        if check_right_order(a, b):
            tot += i + 1
    return tot


def sol2(filename):
    pairs = get_input(filename)
    divider_one_before, divider_two_before = 0, 0
    for pair in pairs:
        p1, p2 = pair
        for p in [p1, p2]:
            if check_right_order(p, [[2]]):
                divider_one_before += 1
                divider_two_before += 1
                continue
            if check_right_order(p, [[6]]):
                divider_two_before += 1
    return (divider_one_before + 1) * (divider_two_before + 2)


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
