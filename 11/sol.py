#!/usr/bin/env python3

class Monkey:
    def __init__(self, operation, operation_value, test, true, false):
        self.items = []
        self.operation = operation
        self.operation_value = operation_value
        self.test = test
        self.true = true
        self.false = false
        self.number_inspections = 0

    def add_item(self, item):
        self.items.append(item)

    def apply_operation(self, value):
        self.number_inspections += 1
        if self.operation_value == 'old':
            second_value = value
        else:
            second_value = int(self.operation_value)
        if self.operation == '+':
            return value + second_value
        return value * second_value


def get_input(filename):
    f = open(filename, 'r')
    monkeys = []
    data = f.read().split('\n\n')
    for m in data:
        lines = m.split('\n')
        operation = lines[2].strip().split(' ')[-2]
        operation_value = lines[2].strip().split(' ')[-1]
        test = int(lines[3].strip().split(' ')[-1])
        true = int(lines[4].strip().split(' ')[-1])
        false = int(lines[5].strip().split(' ')[-1])
        monkey = Monkey(operation, operation_value, test, true, false)
        items = lines[1].strip().split(': ')[1].split(', ')
        for item in items:
            monkey.add_item(int(item))
        monkeys.append(monkey)
    f.close()
    return monkeys


def print_status(monkeys):
    for m in range(len(monkeys)):
        monkey = monkeys[m]
        print('Monkey', m, end=': ')
        for item in monkey.items:
            print(item, end=',')
        print()


def sol(monkeys, reduction, n_rounds):
    n_monkeys = len(monkeys)
    for r in range(n_rounds):
        for m in range(n_monkeys):
            items = monkeys[m].items
            monkeys[m].items = []
            for item in items:
                new_value = monkeys[m].apply_operation(item)
                new_value = reduction(new_value)
                test = (new_value % monkeys[m].test) == 0
                if test:
                    new_monkey_index = monkeys[m].true
                else:
                    new_monkey_index = monkeys[m].false
                monkeys[new_monkey_index].add_item(new_value)
    n_inspections = []
    for monkey in monkeys:
        n_inspections.append(monkey.number_inspections)
    n_inspections.sort(reverse=True)
    return n_inspections[0] * n_inspections[1]


def sol1(filename):
    monkeys = get_input(filename)

    def reduction1(value):
        return int(value/3)

    return sol(monkeys, reduction1, 20)


def sol2(filename):
    monkeys = get_input(filename)
    lcm = 1
    for m in monkeys:
        lcm *= m.test

    def reduction2(value):
        return value % lcm

    return sol(monkeys, reduction2, 10000)


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
