#!/usr/bin/env python3

NUM_ELEM = 256

with open('input', 'r') as f:
    lengths = [ord(c) for c in f.read().strip()]
    lengths.extend([17, 31, 73, 47, 23])

elements = range(NUM_ELEM)

index = 0
skip = 0
for hash_round in xrange(64):
    for length in lengths:
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

        index = (index + length + skip) % NUM_ELEM
        skip += 1

        print elements

dense_hash = []
for block_idx in xrange(16):
    block = elements[block_idx * 16:(block_idx + 1) * 16]
    output = block[0]
    for b in block[1:]:
        output ^= b

    dense_hash.append(output)

print [hex(o) for o in dense_hash]
