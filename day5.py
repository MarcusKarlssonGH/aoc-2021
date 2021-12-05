from collections import Counter
from itertools import zip_longest
import re

def parse_input(filename):
    lines = []
    for line in open(filename).readlines():
        x1, y1, x2, y2 = (int(num) for num in re.findall(r'\d+', line))
        lines.append((get_range(x1, x2), get_range(y1, y2)))
    return lines

def get_range(start, end):
    if start <= end:
        return range(start, end + 1)
    return range(start, end - 1, -1)

def get_points(line):
    xrange, yrange = line
    short = min(xrange, yrange, key=len)
    return zip_longest(xrange, yrange, fillvalue=short.start)

def is_diagonal(line):
    xrange, yrange = line
    return len(xrange) > 1 and len(yrange) > 1

lines = parse_input('input/day5.in')
counts = Counter()
for line in [l for l in lines if not is_diagonal(l)]:
    counts.update(get_points(line))
print(f"Part 1: {len([c for c in counts.values() if c >= 2])}")

counts = Counter()
for line in lines:
    counts.update(get_points(line))
print(f"Part 2: {len([c for c in counts.values() if c >= 2])}")
