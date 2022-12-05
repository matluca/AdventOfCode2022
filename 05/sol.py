#!/usr/bin/env python3

def get_setup(start):
    start_grid = []
    start_lines = start.split('\n')
    for i in range(len(start_lines)):
        line = []
        chars = start_lines[i].split(',')
        for j in range(len(chars) - 1):
            line.append(chars[j])
        start_grid.append(line)
    setup = []
    for i in range(len(start_grid[0])):
        setup.append([])
        for j in range(len(start_grid)):
            if start_grid[len(start_grid)-j-1][i] != '':
                setup[i].append(start_grid[len(start_grid)-j-1][i])
    return setup


def sol1(filename):
    f = open(filename, 'r')
    file = f.read()
    f.close()
    start, moves = file.split('\n\n')
    setup = get_setup(start)

    for move in moves.split('\n'):
        instr = move.split(' ')
        n, a, b = int(instr[1]), int(instr[3]), int(instr[5])
        for i in range(n):
            setup[b-1].append(setup[a-1].pop())

    res = ''
    for i in range(len(setup)):
        res = res + setup[i][-1]
    return res


def sol2(filename):
    f = open(filename, 'r')
    file = f.read()
    f.close()
    start, moves = file.split('\n\n')
    setup = get_setup(start)

    for move in moves.split('\n'):
        instr = move.split(' ')
        n, a, b = int(instr[1]), int(instr[3]), int(instr[5])
        setup[b-1].extend(setup[a-1][-n:])
        setup[a-1] = setup[a-1][:-n]

    res = ''
    for i in range(len(setup)):
        res = res + setup[i][-1]
    return res


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
