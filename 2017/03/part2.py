#!/usr/bin/env python3

input = 312051

def biggest_total(input):
    # Go ahead and create the spiral
    x = 0
    y = 0

    # Just to make the first update step work right
    dx = 0
    dy = -1

    grid = {}

    neighbors = [(1, 0),
                 (1, 1),
                 (0, 1),
                 (-1, 1),
                 (-1, 0),
                 (-1, -1),
                 (0, -1),
                 (1, -1)]
    while True:
        cur_total = 0
        for neighbor in neighbors:
            coord = (x + neighbor[0],
                     y + neighbor[1])
            if coord in grid:
                cur_total += grid[coord]

        if cur_total > input:
            print(cur_total)
            break

        if (x, y) == (0, 0):
            # First step
            grid[(0, 0)] = 1
        else:
            print('Writing {} to ({},{})'.format(cur_total, x, y))
            grid[(x, y)] = cur_total

        # Update step
        if (x == y) or (x > 0 and x == -y + 1) or (x < 0 and x == -y):
            dx, dy = -dy, dx

        x += dx
        y += dy

print(biggest_total(input))
