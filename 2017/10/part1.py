#!/usr/bin/env python3

NUM_ELEM = 256

with open('input', 'r') as f:
    lengths = [int(l) for l in f.read().strip().split(',')]

elements = range(NUM_ELEM)

index = 0
skip = 0

for length in lengths:
    print('Index is {}'.format(index))
    print('Length is {}'.format(length))
    print('Skip is {}'.format(skip))
    if index + length < NUM_ELEM + 1:
        sublist = elements[index:(index + length)]

        sublist.reverse()

        elements[index:(index + length)] = sublist
    else:
        rollover = length - (NUM_ELEM - index)
        sublist = elements[index:]
        sublist.extend(elements[0:rollover])

        sublist.reverse()

        elements[index:] = sublist[:NUM_ELEM - index]
        elements[0:rollover] = sublist[NUM_ELEM - index:]

    print('Sublist: {}'.format(sublist))

    index = (index + length + skip) % NUM_ELEM
    skip += 1

    print elements

print('Product of first two elements: {}'.format(elements[0] * elements[1]))
