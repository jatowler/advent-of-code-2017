#!/usr/bin/env python3

with open('input', 'r') as f:
    data = [line.rstrip().split() for line in f.readlines()]

valid_lines = 0
for line in data:
    if len(set(line)) == len(line):
        valid_lines += 1

print('There were {} valid lines'.format(valid_lines))
