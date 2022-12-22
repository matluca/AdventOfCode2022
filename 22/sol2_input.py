#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    data = f.read()
    f.close()
    grid_raw, mov_raw = data.split('\n\n')
    movs = []
    i = 0
    while i < len(mov_raw):
        if mov_raw[i] in ['L', 'R']:
            movs.append(mov_raw[i])
            i += 1
        else:
            next_l, next_r = len(mov_raw), len(mov_raw)
            if 'L' in mov_raw[i:]:
                next_l = mov_raw[i:].index('L') + i
            if 'R' in mov_raw[i:]:
                next_r = mov_raw[i:].index('R') + i
            next_dir = min(next_l, next_r)
            movs.append(mov_raw[i:next_dir])
            i = next_dir
    return grid_raw.split('\n'), movs


def move_right(pos, tile, size):
    x, y = pos
    if y + 1 < size:
        return (x, y+1), tile, 0
    if tile == 1:
        return (x, 0), 2, 0
    if tile == 5:
        return (x, 0), 4, 0
    if tile == 2:
        return (size-1-x, size-1), 4, 2
    if tile == 4:
        return (size-1-x, size-1), 2, 2
    if tile == 3:
        return (size-1, x), 2, 3
    if tile == 6:
        return (size-1, x), 4, 3


def move_down(pos, tile, size):
    x, y = pos
    if x + 1 < size:
        return (x+1, y), tile, 1
    if tile == 1:
        return (0, y), 3, 1
    if tile == 3:
        return (0, y), 4, 1
    if tile == 5:
        return (0, y), 6, 1
    if tile == 2:
        return (y, size-1), 3, 2
    if tile == 4:
        return (y, size-1), 6, 2
    if tile == 6:
        return (0, y), 2, 1


def move_left(pos, tile, size):
    x, y = pos
    if y > 0:
        return (x, y-1), tile, 2
    if tile == 1:
        return (size-1-x, 0), 5, 0
    if tile == 5:
        return (size-1-x, 0), 1, 0
    if tile == 2:
        return (x, size-1), 1, 2
    if tile == 3:
        return (0, x), 5, 1
    if tile == 4:
        return (x, size-1), 5, 2
    if tile == 6:
        return (0, x), 1, 1


def move_up(pos, tile, size):
    x, y = pos
    if x > 0:
        return (x-1, y), tile, 3
    if tile == 3:
        return (size-1, y), 1, 3
    if tile == 4:
        return (size-1, y), 3, 3
    if tile == 6:
        return (size-1, y), 6, 3
    if tile == 1:
        return (y, 0), 6, 0
    if tile == 2:
        return (size-1, y), 6, 3
    if tile == 5:
        return (y, 0), 3, 0


def get_coords_input(pos, tile, size):
    x, y = pos
    if tile == 1:
        return x, y+size
    if tile == 2:
        return x, y+2*size
    if tile == 3:
        return x+size, y+size
    if tile == 4:
        return x+2*size, y+size
    if tile == 5:
        return x+2*size, y
    if tile == 6:
        return x+3*size, y


def sol2(filename, size):
    original, movs = get_input(filename)
    grids = {
        1: [[original[x][y] for y in range(size, 2 * size)] for x in range(size)],
        2: [[original[x][y] for y in range(2*size, 3*size)] for x in range(size)],
        3: [[original[x][y] for y in range(size, 2 * size)] for x in range(size, 2 * size)],
        4: [[original[x][y] for y in range(size, 2 * size)] for x in range(2 * size, 3 * size)],
        5: [[original[x][y] for y in range(size)] for x in range(2*size, 3*size)],
        6: [[original[x][y] for y in range(size)] for x in range(3*size, 4*size)]
    }
    pos, tile, d = (0, 0), 1, 0
    for mov in movs:
        if not mov.isnumeric():
            if mov == 'R':
                d = (d + 1) % 4
            elif mov == 'L':
                d = (d - 1) % 4
        else:
            steps = int(mov)
            for s in range(steps):
                if d == 0:
                    new_pos, new_tile, new_d = move_right(pos, tile, size)
                elif d == 1:
                    new_pos, new_tile, new_d = move_down(pos, tile, size)
                elif d == 2:
                    new_pos, new_tile, new_d = move_left(pos, tile, size)
                elif d == 3:
                    new_pos, new_tile, new_d = move_up(pos, tile, size)
                if grids[new_tile][new_pos[0]][new_pos[1]] == '#':
                    break
                pos, tile, d = new_pos, new_tile, new_d
    final = get_coords_input(pos, tile, size)
    return 1000*(final[0] + 1) + 4*(final[1] + 1) + d


if __name__ == '__main__':
    print('--- Part 2 ---')
    print(f'Solution: {sol2("input.txt", 50)}')
