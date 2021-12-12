# create tree (dict with edges?)
# search  e
from collections import defaultdict
from os import initgroups

def parse_tree(filename):
    with open(filename) as file:
        connections = defaultdict(list)
        for line in file.read().splitlines():
            a, b = line.split("-")
            connections[a].append(b)
            connections[b].append(a)
        return connections

def is_small(cave):
    return cave.islower()

connections = parse_tree("input/day12.in")
# print(connections)
paths = [['start']]

while True:
    all_new_paths = []
    unfinished_paths = [p for p in paths if p[-1] != 'end']
    finished_paths = [p for p in paths if p[-1] == 'end']
    for path in unfinished_paths:
        last = path[-1]
        neighbors = connections[last]
        to_add = [n for n in neighbors if not (is_small(n) and n in path)]
        for n in to_add:
            tmp = list(path)
            tmp.append(n)
            all_new_paths.append(tmp)

    paths = list(finished_paths) + list(all_new_paths)
    if all(p[-1] == 'end' for p in paths):
        break
    # print(paths)
    # print(len(paths))
    # input()
    # print(paths)
    # input()
# print(paths)
print(len(paths))



