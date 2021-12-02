def get_depth(commands):
    depth, horizontal_pos = 0, 0
    for command, value in commands:
        if command == "forward":
            horizontal_pos += value
        if command == "up":
            depth -= value
        if command == "down":
            depth += value
    return depth * horizontal_pos


def get_depth_with_aim(commands):
    depth, horizontal_pos, aim = 0, 0, 0
    for command, value in commands:
        if command == "forward":
            horizontal_pos += value
            depth += aim * value
        if command == "up":
            aim -= value
        if command == "down":
            aim += value
    return depth * horizontal_pos


commands = [(c, int(v)) for (c, v) in
            (line.split() for line in open("input/day2.in").readlines())]
print(f"Part 1: {get_depth(commands)}")
print(f"Part 2: {get_depth_with_aim(commands)}")
