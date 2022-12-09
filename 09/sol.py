#!/usr/bin/env python3

def get_moves(filename):
    f = open(filename, 'r')
    moves = []
    for line in f.readlines():
        direction, amount = line.strip().split(' ')
        for i in range(int(amount)):
            moves.append(direction)
    f.close()
    return moves


def move_head(head, m):
    if m == 'U':
        return head[0]-1, head[1]
    if m == 'D':
        return head[0]+1, head[1]
    if m == 'L':
        return head[0], head[1]-1
    if m == 'R':
        return head[0], head[1]+1


def move_tail(head, tail):
    x, y = tail
    a, b = head
    if abs(x-a) > 1 or abs(y-b) > 1:
        if x != a:
            x += abs(a-x) // (a-x)
        if y != b:
            y += abs(b-y) // (b-y)
    return x, y


def sol1(filename):
    moves = get_moves(filename)
    tail_positions = set()
    head, tail = (0, 0), (0, 0)
    tail_positions.add(tail)
    for m in moves:
        head = move_head(head, m)
        tail = move_tail(head, tail)
        tail_positions.add(tail)
    return len(tail_positions)


def sol2(filename):
    moves = get_moves(filename)
    tail_positions = set()
    knots = [(0, 0)] * 10
    tail_positions.add(knots[9])
    for m in moves:
        knots[0] = move_head(knots[0], m)
        for i in range(1, 10):
            knots[i] = move_tail(knots[i-1], knots[i])
        tail_positions.add(knots[9])
    return len(tail_positions)


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Test 2: {sol2("test2.txt")}')
    print(f'Solution: {sol2("input.txt")}')
