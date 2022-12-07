#!/usr/bin/env python3

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.files = []
        self.dirs = []
        self.parent = parent

    def add_file(self, file):
        self.files.append(file)

    def add_dir(self, directory):
        self.dirs.append(directory)

    def full_name(self):
        if self.parent is None:
            return self.name
        if self.parent.full_name() == '/':
            return '/' + self.name
        return self.parent.full_name() + '/' + self.name

    def size(self):
        s = 0
        for f in self.files:
            s += f.size
        for d in self.dirs:
            s += d.size()
        return s

    def add_to_dir_sizes(self, sizes):
        sizes.append(self.size())
        for d in self.dirs:
            sizes = d.add_to_dir_sizes(sizes)
        return sizes

    def print_dir(self):
        print('\nPrinting directory ', self.full_name(), ':')
        print('Size: ', self.size())
        dirs = []
        files = []
        for d in self.dirs:
            dirs.append(d.name)
        print('Directories: ', dirs)
        for f in self.files:
            files.append(f.name)
        print('Files: ', files)
        for d in self.dirs:
            d.print_dir()


def get_filesystem_tree(filename):
    f = open(filename, 'r')
    home = Directory('/', None)
    f.readline()  # read first line, cd into /
    current_dir = home
    for line in f.readlines():
        line = line.strip()
        if line == '$ ls':
            continue
        elif line[0] != '$':
            if line.startswith('dir'):
                current_dir.add_dir(Directory(line.split(' ')[1], current_dir))
            else:
                current_dir.add_file(File(line.split(' ')[1], int(line.split(' ')[0])))
        elif line == '$ cd ..':
            current_dir = current_dir.parent
        elif line.startswith('$ cd '):
            dir_name = line.split(' ')[2]
            for d in current_dir.dirs:
                if d.name == dir_name:
                    current_dir = d
                    break
        else:
            print('unknown line type: ', line)
    f.close()
    return home


def sol1(filename):
    home = get_filesystem_tree(filename)
    sizes = home.add_to_dir_sizes([])
    tot = 0
    for s in sizes:
        if s < 100000:
            tot += s
    return tot


def sol2(filename):
    home = get_filesystem_tree(filename)
    free_space = 70000000 - home.size()
    space_to_free = 30000000 - free_space
    sizes = home.add_to_dir_sizes([])
    sizes.sort()
    for s in sizes:
        if s > space_to_free:
            return s


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
