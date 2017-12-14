#!/usr/bin/env python3

with open('input', 'r') as f:
    dirs = [(d[0], int(d[1:])) for d in f.read().strip().split(', ')]

def turn(cur_dir, turn_dir):
    if turn_dir == 'L':
        new_dir = cur_dir - 1
    elif turn_dir == 'R':
        new_dir = cur_dir + 1
    else:
        new_dir = cur_dir

    if new_dir < 0:
        new_dir = 3
    if new_dir > 3:
        new_dir = 0

    return new_dir

def move(cur_pose, step):
    new_dir = turn(cur_pose[0], step[0])

    if new_dir == 0: # north
        new_pose = (new_dir, cur_pose[1], cur_pose[2] + step[1])
    elif new_dir == 1: # east
        new_pose = (new_dir, cur_pose[1] + step[1], cur_pose[2])
    elif new_dir == 2: # south
        new_pose = (new_dir, cur_pose[1], cur_pose[2] - step[1])
    elif new_dir == 3: # west
        new_pose = (new_dir, cur_pose[1] - step[1], cur_pose[2])
    else:
        print('Something went wrong')
        print('  Cur pose: {}'.format(cur_pose))
        print('  Cur step: {}'.format(step))
        new_pose = cur_pose

    print('{} + {} = {}'.format(
        cur_pose, step, new_pose))
    return new_pose

# Part 1
cur_pose = (0, 0, 0)
for dir in dirs:
    cur_pose = move(cur_pose, dir)

print('Distance to HQ: {}'.format(
    abs(cur_pose[1]) + abs(cur_pose[2])))

# Part 2
cur_pose = (0, 0, 0)
poses = set()
done = False
for dir in dirs:
    if done:
        break

    # For this part, we need to walk every step
    new_dir = turn(cur_pose[0], dir[0])
    for i in xrange(dir[1]):
        if new_dir == 0: # north
            cur_pose = (new_dir, cur_pose[1], cur_pose[2] + 1)
        elif new_dir == 1: # east
            cur_pose = (new_dir, cur_pose[1] + 1, cur_pose[2])
        elif new_dir == 2: # south
            cur_pose = (new_dir, cur_pose[1], cur_pose[2] - 1)
        elif new_dir == 3: # west
            cur_pose = (new_dir, cur_pose[1] - 1, cur_pose[2])

        if cur_pose[1:] in poses:
            print('Duplicate detected!')
            print('  Pose: {}'.format(cur_pose))
            print('  Distance: {}'.format(
                abs(cur_pose[1]) + abs(cur_pose[2])))
            done = True
            break
        else:
            poses.add(cur_pose[1:])
