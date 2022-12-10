#!/usr/bin/env python3

def get_input(filename):
    instruction = {}
    f = open(filename, 'r')
    data = f.read()
    lines = data.split('\n')
    cycle = 0
    for line in lines:
        if line.startswith('noop'):
            cycle += 1
            instruction[cycle] = 0
        elif line.startswith('addx'):
            v = int(line.split(' ')[1])
            cycle += 2
            instruction[cycle] = v
    f.close()
    return instruction


def sol1(filename):
    instructions = get_input(filename)
    x = 1
    tot = 0
    for c in range(max(instructions.keys())+2):
        if (c - 20) % 40 == 0:
            tot += c * x
        if c in instructions.keys():
            x += instructions[c]
    return tot


def print_drawing(drawing):
    for row in drawing:
        for c in row:
            print(c, end=' ')
        print()


def sol2(filename):
    instructions = get_input(filename)
    x = 1
    cycles = max(instructions.keys())+2
    drawing = [['.'] * 40 for _ in range(int(cycles/40))]
    for c in range(cycles):
        if c in instructions.keys():
            x += instructions[c]
        if abs((c % 40) - x) < 2:
            drawing[int(c / 40)][c % 40] = '#'
    print_drawing(drawing)


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test:')
    sol2("test.txt")
    print(f'Solution:')
    sol2("input.txt")
