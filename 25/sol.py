#!/usr/bin/env python3

def get_input(filename):
    raw = []
    f = open(filename, 'r')
    for line in f.readlines():
        raw.append(line.strip())
    f.close()
    return raw


def from_snafu(raw):
    n = 0
    for i in range(len(raw)):
        d = raw[len(raw)-1-i]
        if d == '-':
            d = '-1'
        elif d == '=':
            d = '-2'
        n += pow(5, i) * int(d)
    return n


def to_snafu(n):
    reverse = []
    rest = 0
    while n != 0:
        digit = n % 5 + rest
        if digit > 2:
            digit = digit - 5
            rest = 1
        else:
            rest = 0
        reverse.append(digit)
        n = int(n/5)
    s = ''
    for i in range(len(reverse)):
        d = reverse[len(reverse)-1-i]
        if d == -1:
            s += '-'
        elif d == -2:
            s += '='
        else:
            s += f'{d}'
    return s


def sol1(filename):
    raw = get_input(filename)
    tot = 0
    for r in raw:
        tot += from_snafu(r)
    return to_snafu(tot)


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
