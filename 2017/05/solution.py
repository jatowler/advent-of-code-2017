#!/usr/bin/env python3

def part1(input):
    offset = 0
    steps = 0

    while True:
        next_offset = offset + input[offset]
        steps += 1
        if next_offset < 0 or next_offset >= len(input):
            return steps

        input[offset] += 1
        offset = next_offset

def part2(input):
    offset = 0
    steps = 0

    while True:
        next_offset = offset + input[offset]
        steps += 1
        if next_offset < 0 or next_offset >= len(input):
            return steps

        if input[offset] >= 3:
            input[offset] -= 1
        else:
            input[offset] += 1

        offset = next_offset

with open('input', 'r') as f:
    data = [int(line.rstrip()) for line in f.readlines()]

print(part1(data[:]))
print(part2(data[:]))
