def parse_input(filename):
    grid = set()
    with open(filename) as file:
        dots, folds = file.read().split('\n\n')
        for line in dots.splitlines():
            x, y = line.split(',')
            grid.add((int(x), int(y)))
        lines = []
        for line in folds.splitlines():
            a, n = line.split('=')
            lines.append((a[-1], int(n)))

    return grid, lines

def fold_left(dots, number):
    after_fold = set()
    for dot in dots:
        x, y = dot
        if x < number:
            after_fold.add(dot)
        else:
            after_fold.add((number - abs(x - number), y))
    return after_fold

def fold_up(dots, number):
    after_fold = set()
    for dot in dots:
        x, y = dot
        if y < number:
            after_fold.add(dot)
        else:
            after_fold.add((x, number - abs(y - number)))
    return after_fold

def fold(dots, line):
    direction, number = line
    if direction == 'y':
        return fold_up(dots, number)
    return fold_left(dots, number)

def print_dots(dots):
    ymax = int(max(c[1] for c in dots))
    xmax = int(max(c[0] for c in dots))
    dots_str = ""
    for y in range(ymax + 1):
        for x in range(xmax + 1):
            d = (x, y)
            dots_str += "#" if d in dots else "."
        dots_str += '\n'
    print(dots_str)


dots, lines = parse_input('input/day13.in')
print(f"Part 1: {len(fold(dots, lines[0]))}")

for line in lines:
    dots = fold(dots, line)

print("Part 2:")
print_dots(dots)

