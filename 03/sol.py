#!/usr/bin/env python3

def sol1(filename):
    f = open(filename, 'r')
    tot = 0
    lines = f.readlines()
    for line in lines:
        l = len(line)
        for i in range(int(l/2)):
            if line[i] in line[int(l/2):]:
                prio = ord(line[i])-ord('a')+1
                if prio < 0:
                    prio = ord(line[i])-ord('A')+27
                tot += prio
                break
    f.close()
    return tot


def sol2(filename):
    f = open(filename, 'r')
    tot = 0
    lines = f.readlines()
    groups = int(len(lines)/3)
    for i in range(groups):
        l1, l2, l3 = lines[3*i], lines[3*i+1], lines[3*i+2]
        for j in l1:
            if (j in l2) and (j in l3):
                prio = ord(j)-ord('a')+1
                if prio < 0:
                    prio = ord(j)-ord('A')+27
                tot += prio
                break
    f.close()
    return tot


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
