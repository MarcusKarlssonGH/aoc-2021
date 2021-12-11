from itertools import product, count


def parse_input(filename):
    grid = {}
    for row, line in enumerate(open(filename).read().splitlines()):
        for col, c in enumerate(line):
            grid[complex(col, row)] = int(c)
    return grid

def get_adjacent(f):
    deltas = [complex(*p) for p in product((-1,0,1), (-1, 0, 1)) if p != (0, 0)]
    adjacent = [f + d for d in deltas]
    return {a for a in adjacent if 0 <= a.real <= 9 and 0 <= a.imag <= 9}

def get_flashing(grid):
    flashed = set()
    unflashed = {o for o in grid if grid[o] > 9}
    while unflashed:
        for a in [a for f in unflashed for a in get_adjacent(f)]:
            grid[a] += 1
        flashed.update(unflashed)
        unflashed = {o for o in grid if grid[o] > 9}.difference(flashed)
    return flashed

def count_flashes(grid, nr_steps=100):
    nr_flashes = 0
    for _ in range(1, nr_steps + 1):
        grid = {k: v + 1 for k, v in grid.items()}
        flashed = get_flashing(grid)
        nr_flashes += len(flashed)
        grid.update({k: 0 for k in flashed})
    return nr_flashes

def find_synch_step(grid):
    for step in count(start=1): # I hate whiles
        grid = {k: v + 1 for k, v in grid.items()}
        flashed = get_flashing(grid)
        if len(flashed) == len(grid):
            return step
        grid.update({k: 0 for k in flashed})

grid = parse_input("input/day11.in")
print(f"Part 1: {count_flashes(grid)}")
print(f"Part 2: {find_synch_step(grid)}")

