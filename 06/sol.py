#!/usr/bin/env python3

def sol(filename, length):
    f = open(filename, 'r')
    res = []
    for line in f.readlines():
        for i in range(len(line) - length):
            packet = set(line[i:i+length])
            if len(packet) == length:
                res.append(i + length)
                break
    f.close()
    return res


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol("test.txt", 4)}')
    print(f'Solution: {sol("input.txt", 4)}')
    print('--- Part 2 ---')
    print(f'Test: {sol("test.txt", 14)}')
    print(f'Solution: {sol("input.txt", 14)}')
