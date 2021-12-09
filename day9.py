def parse_input(filename):
    with open(filename) as file:
        heights = {}
        for i, line in enumerate(file.readlines()):
            for j, h in enumerate(line.strip()):
                heights[(i,j)] = int(h)
    return heights

def get_adjacent(p):
    x, y = p
    return [(x + dx, y + dy) for (dx, dy) in [(0,1), (0,-1), (1, 0), (-1, 0)]]

def get_low_points(heights):
    low_points = []
    for p, h in heights.items():
        adjacent_heights = [heights.get(n, 9) for n in get_adjacent(p)]
        if all(ah > h for ah in adjacent_heights):
            low_points.append(p)
    return low_points

def get_basins(heights, low_points):
    visited = set()
    basins = []
    for low_point in low_points:
        basin, queue = set(), set()
        queue.add(low_point)
        basin.add(low_point)
        while queue:
            p = queue.pop()
            visited.add(p)
            adjacent = {a for a in get_adjacent(p)
                        if heights.get(a, 9) < 9 and a not in visited}
            queue.update(adjacent)
            basin.update(adjacent)
        basins.append(basin)
    return basins

heights = parse_input("input/day9.in")
low_points = get_low_points(heights)
risk = sum([heights[p] + 1 for p in low_points])
print(f"Part 1: {risk}")

basins = get_basins(heights, low_points)
a, b, c , *_ = sorted([len(b) for b in basins], reverse=True)
print(f"Part 2: {a * b * c}")
