#!/usr/bin/env python3

with open('input', 'r') as f:
    data = f.read()[:-1]

modulo = len(data) / 2

total = 0

for idx, char in enumerate(data):
    if char == data[(idx + modulo) % len(data)]:
        total += int(char)

print('Sum is {}'.format(total))
