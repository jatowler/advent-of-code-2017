#!/usr/bin/env python3

graph = {}
with open('input', 'r') as f:
    pipes = [l.strip() for l in f.readlines()]
    for pipe in pipes:
        base, neighbor = pipe.split(' <-> ')
        graph[base] = neighbor.split(', ')

# Need size of group including zero

def visit(node, visited=None):
    if visited is None:
        visited = []

    if node not in visited:
        visited.append(node)
        for child in graph[node]:
            visit(child, visited)

    return len(visited)

print('Group 0 has {} members'.format(visit('0')))

visited = []
groups = 0
for node in graph:
    if node not in visited:
        groups += 1
        visit(node, visited)

print('Found {} groups'.format(groups))
