#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    numbers = []
    for line in f.readlines():
        numbers.append(int(line.strip()))
    f.close()
    return numbers


def swap(numbers_with_pos, e):
    index = numbers_with_pos.index(e)
    val, _ = numbers_with_pos.pop(index)
    new_index = (index + val) % len(numbers_with_pos)
    numbers_with_pos.insert(new_index, e)


def sol1(filename):
    numbers = get_input(filename)
    length = len(numbers)
    numbers_with_pos = [(n, i) for i, n in enumerate(numbers)]
    for i, n in enumerate(numbers):
        swap(numbers_with_pos, (n, i))
    final_list = [x[0] for x in numbers_with_pos]
    return final_list[(final_list.index(0) + 1000) % length] + final_list[(final_list.index(0) + 2000) % length] + final_list[(final_list.index(0) + 3000) % length]


def sol2(filename):
    raw_numbers = get_input(filename)
    numbers = []
    for n in raw_numbers:
        numbers.append(n * 811589153)
    length = len(numbers)
    numbers_with_pos = [(n, i) for i, n in enumerate(numbers)]
    for _ in range(10):
        for i, n in enumerate(numbers):
            swap(numbers_with_pos, (n, i))
    final_list = [x[0] for x in numbers_with_pos]
    return final_list[(final_list.index(0) + 1000) % length] + final_list[(final_list.index(0) + 2000) % length] + final_list[(final_list.index(0) + 3000) % length]


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
