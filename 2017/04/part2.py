#!/usr/bin/env python3

def has_duplicates(words):
    return len(set(line)) != len(line)

def has_anagram(words):
    for m in line:
        for n in line:
            if m == n:
                continue

            if sorted(m) == sorted(n):
                return True

    return False

with open('input', 'r') as f:
    data = [line.rstrip().split() for line in f.readlines()]

valid_lines = 0
for line in data:
    if has_duplicates(line):
        continue

    if has_anagram(line):
        continue

    valid_lines += 1

print('There were {} valid lines'.format(valid_lines))
