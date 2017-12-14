#!/usr/bin/env python3

from collections import defaultdict

with open('input', 'r') as f:
    instructions = [line.rstrip().split('if') for line in f.readlines()]

max_register = -1

registers = defaultdict(int)
for i in instructions:
    command = i[0].strip().split()
    reg = command[0]
    dir = command[1]
    val = int(command[2])

    condition = i[1].strip().split()
    test_reg = condition[0]
    test = condition[1]
    test_val = int(condition[2])

    cond_string = 'registers["{}"] {} {}'.format(test_reg, test, test_val)
    if eval(cond_string):
        if dir == 'inc':
            registers[reg] += val
        elif dir == 'dec':
            registers[reg] -= val
        else:
            print "'{}' is not valid".format(dir)

    # For Part 2
    m = max(registers.values())
    if m > max_register:
        max_register = m

print(max(registers.values()))

# For Part 2
print(max_register)
