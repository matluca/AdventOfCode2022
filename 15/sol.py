#!/usr/bin/env python3

def get_input(filename):
    f = open(filename, 'r')
    lines = []
    for line in f.readlines():
        sx_raw, sy_raw = line.strip().split(':')[0].split(',')
        sx = int(sx_raw.split('=')[1])
        sy = int(sy_raw.split('=')[1])
        bx_raw, by_raw = line.strip().split(':')[1].split(',')
        bx = int(bx_raw.split('=')[1])
        by = int(by_raw.split('=')[1])
        lines.append(((sy, sx), (by, bx)))
    f.close()
    return lines


def man_dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1-x2) + abs(y1-y2)


def simplify(s1, segments):
    new_segments = []
    for s2 in segments:
        if s1[1] < s2[0] or s2[1] < s1[0]:
            new_segments.append(s2)
            continue
        if s2[0] < s1[0]:
            new_segments.append((s2[0], s1[0]-1))
        if s2[1] > s1[1]:
            new_segments.append((s1[1]+1, s2[1]))
    new_segments.append(s1)
    return new_segments


def segments_row(filename, row):
    lines = get_input(filename)
    segments = []
    beacons = set()
    for line in lines:
        s, b = line
        beacons.add(b)
        d = man_dist(s, b)
        vert_distance = abs(s[0] - row)
        if vert_distance > d:
            continue
        segments.append((s[1]-d+vert_distance, s[1]+d-vert_distance))
    simplified_segments = []
    for s in segments:
        simplified_segments = simplify(s, simplified_segments)
    return beacons, simplified_segments


def sol1(filename, row):
    beacons, segments = segments_row(filename, row)
    tot = 0
    for s in segments:
        tot += s[1] - s[0] + 1
    for b in beacons:
        if b[0] == row:
            tot -= 1
    return tot


def sol2(filename, size):
    for row in range(size, -1, -1):
        beacons, segments = segments_row(filename, row)
        interesting_segments = []
        for s in segments:
            if s[0] > size or s[1] < 0:
                continue
            interesting_segments.append(s)
        interesting_segments.sort(key=lambda x: x[0])
        for i in range(len(interesting_segments)-1):
            if interesting_segments[i][1] != interesting_segments[i+1][0] - 1:
                return 4000000 * (interesting_segments[i][1] + 1) + row


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt", 10)}')
    print(f'Solution: {sol1("input.txt", 2000000)}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt", 20)}')
    print(f'Solution: {sol2("input.txt", 4000000)}')
