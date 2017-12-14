#!/usr/bin/env python3

import pprint
import re

def get_weight(child):
    matches = re.match(r'(\w+) \((\d+)\)', child)
    name = matches.group(1)
    weight = int(matches.group(2))
    return name, weight

# name : (weight, parent)
nodes = {}

with open('input', 'r') as f:
    for line in [l.rstrip() for l in f.readlines()]:
        data = line.split('->')
        name, weight = get_weight(data[0])

        if name in nodes:
            nodes[name] = (weight, nodes[name][1])
        else:
            nodes[name] = (weight, None)

        if len(data) > 1:
            # Has children
            children = [n.strip() for n in data[1].split(',')]
            for child in children:
                if child in nodes:
                    nodes[child] = (nodes[child][0], name)
                else:
                    nodes[child] = (None, name)

base_node = None

for k, v in nodes.iteritems():
    if v[1] == None:
        base_node = k
        break

print('Base node is {}'.format(base_node))

# Part 2

children = {}
for name, data in nodes.iteritems():
    if data[1] is not None:
        # has a parent
        if data[1] in children:
            children[data[1]].append(name)
        else:
            children[data[1]] = [name]

pprint.pprint(children)

def child_weight(parent):
    weight = nodes[parent][0]
    #print('base weight of {} is {}'.format(parent, weight))
    if parent in children:
        for child in children[parent]:
            sub_weight = child_weight(child)
            #print('  weight of {} is {}'.format(child, sub_weight))
            weight += sub_weight
            #print('  subtotal for {} is {}'.format(parent, weight))

    return weight

for node in children:
    child_weights = []
    for child in children[node]:
        child_weights.append(child_weight(child))

    # if one is different
    if not child_weights.count(child_weights[0]) == len(child_weights):
        print('{} is unbalanced'.format(node))
        pprint.pprint(zip(children[node],
                          [nodes[c][0] for c in children[node]],
                          child_weights))
        print
