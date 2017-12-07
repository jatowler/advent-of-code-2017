#!/usr/bin/env python3

with open('input', 'r') as f:
    data = f.read()[:-1]

# Copy first character to end to simplify
data = data + data[0]

total = 0

for idx, char in enumerate(data[:-1]):
    if char == data[idx + 1]:
        total += int(char)

print('Sum is {}'.format(total))
