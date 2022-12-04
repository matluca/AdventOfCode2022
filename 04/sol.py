#!/usr/bin/env python3

def sol1(filename):
    f = open(filename, 'r')
    tot = 0
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        one, two = line.split(',')
        a_s, b_s = one.split('-')
        c_s, d_s = two.split('-')
        a, b, c, d = int(a_s), int(b_s), int(c_s), int(d_s)
        if ((a >= c) and (b <= d)) or ((a <= c) and (b >= d)):
            tot += 1
    f.close()
    return tot


def sol2(filename):
    f = open(filename, 'r')
    tot = 0
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        one, two = line.split(',')
        a_s, b_s = one.split('-')
        c_s, d_s = two.split('-')
        a, b, c, d = int(a_s), int(b_s), int(c_s), int(d_s)
        if (b >= c) and (a <= d):
            tot += 1
    f.close()
    return tot


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
