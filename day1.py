from numpy import convolve, ones


def parse_input(filename):
    with open(filename) as file:
        return [int(line) for line in file.readlines()]


measurements = parse_input("input/day1.in")

count = sum(second > first for (first, second) in zip(measurements, measurements[1:]))
print(f"Part 1: {count}")


window_sums = convolve(measurements, ones(3), "valid")
count = sum(second > first for (first, second) in zip(window_sums, window_sums[1:]))
print(f"Part 2: {count}")
