#!/usr/bin/env python3

DIRECTIONS = {'n': (0, 1, -1),
              'ne':  (1, 0, -1),
              'se':  (1, -1, 0),
              's':  (0, -1, 1),
              'sw':  (-1, 0, 1),
              'nw': (-1, 1, 0)}

def move_dir(position, dir):
    return [sum(x) for x in zip(position, DIRECTIONS[dir])]

def dist(position):
    return sum([abs(c) for c in position]) / 2

with open('input', 'r') as f:
    dirs = f.read().strip().split(',')

child_pos = (0, 0, 0)
farthest = -1
for dir in dirs:
    child_pos = move_dir(child_pos, dir)
    print child_pos
    if dist(child_pos) > farthest:
        farthest = dist(child_pos)
        print farthest

print('Distance to final: {}'.format(dist(child_pos)))
print('Farthest wandering: {}'.format(farthest))
