#!/usr/bin/env python3

import copy

levels = {}

DEBUG = False

with open('input', 'r') as f:
    for depth,rng in [l.strip().split(': ') for l in f.readlines()]:
        levels[int(depth)] = {'scanner_range': int(rng),
                              'scanner_pos': 0,
                              'scanner_dir': -1}

# Huge mess of code to get outputs to compare to puzzle page
def print_level(levels, cur_depth):
    if not DEBUG:
        return

    num_levels = max(levels.keys()) + 1
    for level in range(num_levels):
        if level < 10:
            print(' {} '.format(level), end='')
        else:
            print(' {}'.format(level), end='')

        print(' ', end='')
    print()

    max_range = max([levels[l]['scanner_range'] for l in levels])

    for r in range(max_range):
        for level in range(num_levels):
            if cur_depth == level and r == 0:
                format_string = '({})'
            else:
                format_string = '[{}]'

            if level not in levels:
                if cur_depth == level and r == 0:
                    print('(.)', end='')
                else:
                    print('...', end='')
            elif levels[level]['scanner_range'] > r:
                if levels[level]['scanner_pos'] == r:
                    print(format_string.format('S'), end='')
                else:
                    print(format_string.format(' '), end='')
            else:
                print('   ', end='')

            print(' ', end='')
        print()

def step(levels):
    for level, data in levels.items():
        if data['scanner_pos'] in (0, data['scanner_range'] - 1):
            data['scanner_dir'] *= -1

        data['scanner_pos'] = data['scanner_pos'] + data['scanner_dir']

def caught(levels, cur_depth):
    if cur_depth not in levels:
        # No scanner on this level
        return False

    if levels[cur_depth]['scanner_pos'] == 0:
        return True
    else:
        return False

# Part 1
# Simulation method
def run_firewall(levels, delay=0, break_if_caught=False):
    # Make a copy
    levels_copy = copy.deepcopy(levels)
    got_caught = False

    cur_depth = -1 - delay
    print_level(levels_copy, cur_depth)
    max_depth = max(levels_copy.keys()) + 1
    score = 0
    for i in range(max_depth + delay):
        cur_depth += 1
        print_level(levels_copy, cur_depth)
        if caught(levels_copy, cur_depth):
            got_caught = True
            if DEBUG:
                print('Caught!')
            score += cur_depth * levels_copy[cur_depth]['scanner_range']
            if break_if_caught:
                return got_caught, score
        step(levels_copy)
        print_level(levels_copy, cur_depth)
        if DEBUG:
            print('--------------------------------')

    return (got_caught, score)

print('Score: {}'.format(run_firewall(levels)[1]))

# Do it without simulating
score = 0
for level in levels:
    rng = levels[level]['scanner_range']
    period = (rng - 1) * 2
    if level % period == 0:
        score += level * rng
print('Score: {}'.format(score))

## Part 2
# To never get caught, we need that the scanner is never at
# position 0 when we are in that level. The scanner is at
# position 0 at (0 + (range - 1) * 2 * n. So a range of 4 is
# at 0 every six iterations.
#
# The scanner is at our position if level + delay is congruent
# with the scanner period. So a range of 4 hits us at
# level 0, delay 0; level 1, delay 5; level 2, delay 4...
delay = 0
while True:
    fail = False
    for level in levels:
        rng = levels[level]['scanner_range']
        period = (rng - 1) * 2
        if (delay + level) % period == 0:
            fail = True
            break
    if not fail:
        print('Succeeded at delay {}'.format(delay))
        break
    delay += 1
