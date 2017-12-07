#!/usr/bin/env python3

import math

input = 312051

def find_distance(square):
    # Find the largest square smaller than the number
    ring = int(math.ceil(math.sqrt(square)))
    if ring % 2 == 0:
        ring += 1

    # The minimum distance for all squares on that ring
    base_distance = (ring - 1) / 2

    # Additional distance based on this square
    index = (square - (ring - 2)**2) % (ring - 1)
    additional_dist = abs(index - (ring / 2))

    print('ring: {}'.format(ring))
    print(base_distance)
    print(additional_dist)
    return base_distance + additional_dist

print('Distance for {} is {}'.format(input, find_distance(input)))
