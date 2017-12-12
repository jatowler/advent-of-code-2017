#!/usr/bin/env python3

GROUP_OPEN = '{'
GROUP_CLOSE = '}'
GROUP_SEP = ','
GARBAGE_OPEN = '<'
GARBAGE_CLOSE = '>'
IGNORE = '!'

NORMAL_MODE = 0
GARBAGE_MODE = 1

IGNORE_FLAG = False

with open('input', 'r') as f:
    data = [l.strip() for l in f.readlines()]

for l in data:
    print l

    group_depth = 0
    score = 0
    garbage_count = 0 # For part 2
    index = -1
    mode = NORMAL_MODE
    while (index + 1) < len(l):
        index += 1
        char = l[index]

        if IGNORE_FLAG:
            #print('Ignoring {}'.format(char))
            IGNORE_FLAG = False
            continue

        if char == IGNORE:
            #print('Encountered ignore char')
            IGNORE_FLAG = True
            continue

        if mode == NORMAL_MODE:
            if char == GROUP_OPEN:
                #print('Opening group depth {}'.format(group_depth + 1))
                group_depth += 1
            elif char == GROUP_CLOSE:
                score += group_depth
                group_depth -= 1
                #print('Closing group depth {}'.format(group_depth + 1))
                #print('  Score {}'.format(score))
            elif char == GARBAGE_OPEN:
                #print('Opening garbage')
                mode = GARBAGE_MODE
            elif char == GARBAGE_CLOSE:
                #print('Closing garbage')
                # Probably shouldn't happen
                pass
        elif mode == GARBAGE_MODE:
            if char == GARBAGE_CLOSE:
                #print('Exiting garbage mode')
                mode = NORMAL_MODE
            else:
                garbage_count += 1
        else:
            print('Something went wrong')
            break
    print('Score: {}'.format(score))
    print('Garbage count: {}'.format(garbage_count))
