#!/usr/bin/env python3

lines = []
with open('input', 'r') as f:
    for line in f:
        l = [int(n) for n in line.split()]
        lines.append(l)

checksum = 0

for line in lines:
    checksum += abs(max(line) - min(line))

print('Checksum is {}'.format(checksum))
