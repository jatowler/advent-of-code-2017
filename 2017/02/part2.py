#!/usr/bin/env python3

lines = []
with open('input', 'r') as f:
    for line in f:
        l = [int(n) for n in line.split()]
        lines.append(l)

checksum = 0

for line in lines:
    for n in line:
        for m in line:
            if n == m:
                continue
            if n % m == 0:
                checksum += n / m
                print('{} / {} = {}'.format(n, m, n / m))

print('Checksum is {}'.format(checksum))
