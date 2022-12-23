#!/usr/bin/env python3

class Valve:
    def __init__(self, flow_rate, neighbours):
        self.flow_rate = flow_rate
        self.neighbours = neighbours


class SimplifiedValve:
    def __init__(self, flow_rate, neighbours):
        self.flow_rate = flow_rate
        self.neighbours = neighbours


def get_input(filename):
    f = open(filename, 'r')
    valves = {}
    for line in f.readlines():
        v, n = line.strip().split('; ')
        name = v.split(' ')[1]
        flow_rate = int(v.split(' ')[4].split('=')[1])
        neighbours_list = n.split(' ')[4:]
        neighbours = []
        for n in neighbours_list:
            neighbours.append(n.split(',')[0])
        valves[name] = Valve(flow_rate, neighbours)
    f.close()
    return valves


def get_distances(valves):
    valve_names = valves.keys()
    distances = {}
    for n in valve_names:
        distances[n + n] = 0
    while len(distances) != len(valve_names) * len(valve_names):
        for n1 in valve_names:
            for n in valves[n1].neighbours:
                distances[n1 + n] = 1
                distances[n + n1] = 1
            keys = [k for k in distances.keys()]
            for key in keys:
                if key[:2] == n1:
                    n2 = key[2:]
                    for n in valves[n2].neighbours:
                        if n1 + n not in distances.keys():
                            distances[n1 + n] = distances[key] + 1
                            distances[n + n1] = distances[key] + 1
    return distances


def simplified_valves(valves):
    distances = get_distances(valves)
    names = valves.keys()
    new_valves = {}
    for n1 in names:
        neighbours = {}
        for n2 in names:
            neighbours[n2] = distances[n1 + n2]
        new_valves[n1] = SimplifiedValve(valves[n1].flow_rate, neighbours)
    return new_valves


def best_score(pos, open_valves, time_remaining):
    if time_remaining <= 0:
        return 0
    if len(open_valves) == 1:
        valve = list(open_valves.values())[0]
        dist = valve.neighbours[pos]
        if dist > time_remaining + 1:
            return 0
        return valve.flow_rate * (time_remaining - dist - 1)
    best = 0
    for valve in open_valves.keys():
        remaining_valves = {}
        for v in open_valves.keys():
            if v != valve:
                remaining_valves[v] = open_valves[v]
        dist = open_valves[valve].neighbours[pos]
        score = best_score(valve, remaining_valves, time_remaining - dist - 1) + open_valves[valve].flow_rate * (time_remaining - dist - 1)
        if score > best:
            best = score
    return best


def sol1(filename):
    valves = get_input(filename)
    new_valves = simplified_valves(valves)
    valves = {}
    for n, v in new_valves.items():
        if v.flow_rate != 0:
            valves[n] = v
    return best_score('AA', valves, 30)


def sol2(filename):
    valves = get_input(filename)
    new_valves = simplified_valves(valves)
    valves = {}
    for n, v in new_valves.items():
        if v.flow_rate != 0:
            valves[n] = v
    valve_names = list(valves.keys())
    best = 0
    for n in range(pow(2, len(valves)-1)):
        valves_1 = {}
        valves_2 = {}
        for i in range(len(valves)):
            valve_name = valve_names[i]
            digits = []
            new_n = n
            for _ in range(len(valves)):
                digits.append(new_n % 2)
                new_n = int(new_n / 2)
            if digits[i]:
                valves_1[valve_name] = valves[valve_name]
            else:
                valves_2[valve_name] = valves[valve_name]
        score = best_score('AA', valves_1, 26) + best_score('AA', valves_2, 26)
        if score > best:
            best = score
    return best


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Test: {sol2("test.txt")}')
    print(f'Solution: {sol2("input.txt")}')
