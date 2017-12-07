#!/usr/bin/env python

with open('input', 'r') as f:
    bins = [int(b) for b in f.read().rstrip().split()]

print bins

def redistribute(bins):
    # Find index of biggest
    max_value = int(max(bins))
    max_index = bins.index(max(bins))

    bins[max_index] = 0
    for i in xrange(max_value):
        index = (max_index + i + 1) % len(bins)
        bins[index] += 1

distributions = [bins[:]]


num_steps = 0
while True:
    num_steps += 1
    redistribute(bins)
    if bins in distributions:
        break
    distributions.append(bins[:])

print('Part 1')
print('Final distribution:')
print(bins)
print('Took {} steps'.format(num_steps))

# Part 2
dup_index = distributions.index(bins)
print('Cycle length is {}'.format(num_steps - dup_index))
