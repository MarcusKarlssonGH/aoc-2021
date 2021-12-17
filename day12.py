from collections import defaultdict

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

def create_counter(connections, allow_two = False):
    def count_paths(path=[], cave='start', allow_two = allow_two):
        if cave == 'end':
            return 1
        path.append(cave)
        count = 0
        for n in connections[cave]:
            if is_small(n) and n in path:
                if allow_two and n not in ['start', 'end']:
                    count += count_paths(list(path), n, False)
            else:
                count += count_paths(list(path), n, allow_two)
        return count
    return count_paths

connections = parse_tree("input/day12.in")
count_paths = create_counter(connections, allow_two = False)
# print(f"{count_paths(allow_two=True)}")
print(f"Part 1: {count_paths()}")
print(f"Part 2: {count_paths(allow_two=True)}")
