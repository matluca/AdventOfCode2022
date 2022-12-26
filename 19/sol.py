#!/usr/bin/env python3

import math


def get_input(filename):
    f = open(filename, 'r')
    n = 0
    blueprints = {}
    for line in f.readlines():
        n += 1
        costs_raw = line.strip().split(': ')[1].split('. ')
        ore = {'ore': int(costs_raw[0].split(' ')[4])}
        clay = {'ore': int(costs_raw[1].split(' ')[4])}
        obsidian = {'ore': int(costs_raw[2].split(' ')[4]), 'clay': int(costs_raw[2].split(' ')[7])}
        geode = {'ore': int(costs_raw[3].split(' ')[4]), 'obsidian': int(costs_raw[3].split(' ')[7])}
        blueprints[n] = {'ore': ore, 'clay': clay, 'obsidian': obsidian, 'geode': geode}
    f.close()
    return blueprints


def ceil(a, b):
    if a % b == 0:
        return int(a/b)
    return int(a/b) + 1


def time_to_robot(blueprint, need, ore_r, clay_r, obsidian_r, ore, clay, obsidian):
    if need == 'ore':
        max_ore = blueprint['ore']['ore'] + blueprint['clay']['ore'] + blueprint['obsidian']['ore'] + blueprint['geode']['ore']
        if ore >= max_ore:
            return 1000
        amount = blueprint['ore']['ore']
        if ore >= amount:
            return 0
        return ceil((amount - ore), ore_r)
    if need == 'clay':
        if clay >= blueprint['obsidian']['clay']:
            return 1000
        amount = blueprint['clay']['ore']
        if ore >= amount:
            return 0
        return ceil((amount - ore), ore_r)
    if need == 'obsidian':
        if obsidian >= blueprint['geode']['obsidian']:
            return 1000
        amount_ore = blueprint['obsidian']['ore']
        if ore >= amount_ore:
            time_ore = 0
        else:
            time_ore = ceil((amount_ore - ore), ore_r)
        amount_clay = blueprint['obsidian']['clay']
        if clay >= amount_clay:
            time_clay = 0
        else:
            if clay_r == 0:
                time_clay = 1000
            else:
                time_clay = ceil((amount_clay - clay), clay_r)
        return max(time_ore, time_clay)
    if need == 'geode':
        amount_ore = blueprint['geode']['ore']
        if ore >= amount_ore:
            time_ore = 0
        else:
            time_ore = ceil((amount_ore - ore), ore_r)
        amount_obsidian = blueprint['geode']['obsidian']
        if obsidian >= amount_obsidian:
            time_obsidian = 0
        else:
            if obsidian_r == 0:
                time_obsidian = 1000
            else:
                time_obsidian = ceil((amount_obsidian - obsidian), obsidian_r)
        return max(time_ore, time_obsidian)


def best_score(blueprint, time, ore_r, clay_r, obsidian_r, geode_r, ore, clay, obsidian, geode, visited):
    options = []
    t = time_to_robot(blueprint, 'ore', ore_r, clay_r, obsidian_r, ore, clay, obsidian)
    if t < time and (time-t-1, ore_r+1, clay_r, obsidian_r, geode_r, ore-blueprint['ore']['ore']+ore_r*(t+1), clay+clay_r*(t+1), obsidian+obsidian_r*(t+1), geode+geode_r*(t+1)) not in visited:
        s = best_score(blueprint, time-t-1, ore_r+1, clay_r, obsidian_r, geode_r, ore-blueprint['ore']['ore']+ore_r*(t+1), clay+clay_r*(t+1), obsidian+obsidian_r*(t+1), geode+geode_r*(t+1), visited)
        options.append(s)
    t = time_to_robot(blueprint, 'clay', ore_r, clay_r, obsidian_r, ore, clay, obsidian)
    if t < time and (time-t-1, ore_r, clay_r+1, obsidian_r, geode_r, ore-blueprint['clay']['ore']+ore_r*(t+1), clay+clay_r*(t+1), obsidian+obsidian_r*(t+1), geode+geode_r*(t+1)) not in visited:
        s = best_score(blueprint, time-t-1, ore_r, clay_r+1, obsidian_r, geode_r, ore-blueprint['clay']['ore']+ore_r*(t+1), clay+clay_r*(t+1), obsidian+obsidian_r*(t+1), geode+geode_r*(t+1), visited)
        options.append(s)
    t = time_to_robot(blueprint, 'obsidian', ore_r, clay_r, obsidian_r, ore, clay, obsidian)
    if t < time and (time-t-1, ore_r, clay_r, obsidian_r+1, geode_r, ore-blueprint['obsidian']['ore']+ore_r*(t+1), clay-blueprint['obsidian']['clay']+clay_r*(t+1), obsidian+obsidian_r*(t+1), geode+geode_r*(t+1)) not in visited:
        s = best_score(blueprint, time-t-1, ore_r, clay_r, obsidian_r+1, geode_r, ore-blueprint['obsidian']['ore']+ore_r*(t+1), clay-blueprint['obsidian']['clay']+clay_r*(t+1), obsidian+obsidian_r*(t+1), geode+geode_r*(t+1), visited)
        options.append(s)
    t = time_to_robot(blueprint, 'geode', ore_r, clay_r, obsidian_r, ore, clay, obsidian)
    if t < time and (time-t-1, ore_r, clay_r, obsidian_r, geode_r+1, ore-blueprint['geode']['ore']+ore_r*(t+1), clay+clay_r*(t+1), obsidian-blueprint['geode']['obsidian']+obsidian_r*(t+1), geode+geode_r*(t+1)) not in visited:
        s = best_score(blueprint, time-t-1, ore_r, clay_r, obsidian_r, geode_r+1, ore-blueprint['geode']['ore']+ore_r*(t+1), clay+clay_r*(t+1), obsidian-blueprint['geode']['obsidian']+obsidian_r*(t+1), geode+geode_r*(t+1), visited)
        options.append(s)
    do_nothing_score = geode+geode_r*time
    options.append(do_nothing_score)
    visited.add((time, ore_r, clay_r, obsidian_r, geode_r, ore, clay, obsidian, geode))
    return max(options)


def sol1(filename):
    blueprints = get_input(filename)
    tot = 0
    for b in range(1, len(blueprints)+1):
        visited = set([])
        score = best_score(blueprints[b], 24, 1, 0, 0, 0, 0, 0, 0, 0, visited)
        tot += score * b
    return tot


def sol2(filename):
    blueprints = get_input(filename)
    tot = 1
    for b in range(1, 4):
        visited = set([])
        score = best_score(blueprints[b], 32, 1, 0, 0, 0, 0, 0, 0, 0, visited)
        tot *= score
    return tot


if __name__ == '__main__':
    print('--- Part 1 ---')
    print(f'Test: {sol1("test.txt")}')
    print(f'Solution: {sol1("input.txt")}')
    print('--- Part 2 ---')
    print(f'Solution: {sol2("input.txt")}')
