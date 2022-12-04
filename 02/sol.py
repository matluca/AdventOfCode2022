#!/usr/bin/env python3

scores_seed_1 = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

scores_result_1 = {
    'A': {'X': 3, 'Y': 6, 'Z': 0},
    'B': {'X': 0, 'Y': 3, 'Z': 6},
    'C': {'X': 6, 'Y': 0, 'Z': 3},
}

scores_result_2 = {
    'X': 0,
    'Y': 3,
    'Z': 6
}

scores_seed_2 = {
    'A': {'X': 3, 'Y': 1, 'Z': 2},
    'B': {'X': 1, 'Y': 2, 'Z': 3},
    'C': {'X': 2, 'Y': 3, 'Z': 1},
}


def sol1(filename):
    f = open(filename, 'r')
    tot = 0
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        op, you = line.split(' ')
        tot += scores_result_1[op][you] + scores_seed_1[you]
    f.close()
    return tot


def sol2(filename):
    f = open(filename, 'r')
    tot = 0
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        op, you = line.split(' ')
        tot += scores_result_2[you] + scores_seed_2[op][you]
    f.close()
    return tot


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
