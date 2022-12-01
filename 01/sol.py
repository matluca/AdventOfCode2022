#!/usr/bin/env python3

def sol1(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    elf_calories = 0
    calories = []
    for line in lines:
        line = line.strip()
        if line == '':
            calories.append(elf_calories)
            elf_calories = 0
        else:
            elf_calories += int(line)
    f.close()
    calories.sort(reverse=True)
    return calories[0], calories[0] + calories[1] + calories[2]


if __name__ == '__main__':
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
