from numpy import convolve, ones


measurements = [int(line) for line in open("input/day1.in").readlines()]
count = sum(second > first for (first, second) in zip(measurements, measurements[1:]))
print(f"Part 1: {count}")
window_sums = convolve(measurements, ones(3), "valid")
count = sum(second > first for (first, second) in zip(window_sums, window_sums[1:]))
print(f"Part 2: {count}")
