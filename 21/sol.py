#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    monkeys = {}
    for line in f.readlines():
        name, op = line.strip().split(': ')
        monkeys[name] = op
    f.close()
    return monkeys


def value(name, monkeys):
    op = monkeys[name]
    if op.isnumeric():
        return op
    else:
        m1, x, m2 = op.split(' ')
        v1 = value(m1, monkeys)
        v2 = value(m2, monkeys)
        return int(eval(f'{v1}{x}{v2}'))


def value2(name, monkeys):
    if name == 'humn':
        return 'x'
    op = monkeys[name]
    if op.isnumeric():
        return f'{op}'
    else:
        m1, x, m2 = op.split(' ')
        v1 = value2(m1, monkeys)
        v2 = value2(m2, monkeys)
        if name == 'root':
            return f'{v1} = {v2}'
        if v1.isnumeric() and v2.isnumeric():
            res = int(eval(f'{v1}{x}{v2}'))
            return f'{res}'
        else:
            if not v1.isnumeric():
                v1 = f'({v1})'
            if not v2.isnumeric():
                v2 = f'({v2})'
            return f'{v1}{x}{v2}'


def sol1(filename):
    monkeys = get_input(filename)
    return value('root', monkeys)


def sol2(filename):
    monkeys = get_input(filename)
    expr = value2('root', monkeys)
    l, _, r = expr.split(' ')
    while l != 'x':
        if l[0] == '(':
            end_index = l.rindex(')')
            op = l[end_index + 1]
            n = l[end_index + 2:]
            new_l = l[1:end_index]
            if op == '+':
                new_r = eval(f'{r}-{n}')
            elif op == '-':
                new_r = eval(f'{r}+{n}')
            elif op == '*':
                new_r = eval(f'{r}/{n}')
            elif op == '/':
                new_r = eval(f'{r}*{n}')
            l, r = new_l, new_r
        else:
            start_index = l.index('(')
            op = l[start_index - 1]
            n = l[:start_index - 1]
            new_l = l[start_index + 1: -1]
            if op == '+':
                new_r = eval(f'{r}-{n}')
            elif op == '-':
                new_r = eval(f'{n}-{r}')
            elif op == '*':
                new_r = eval(f'{r}/{n}')
            elif op == '/':
                new_r = eval(f'{n}*{r}')
            l, r = new_l, new_r
    return int(r)


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
