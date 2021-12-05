depths = [int(line) for line in open("input/day1.in").readlines()]
count = sum(second > first for (first, second) in zip(depths, depths[1:]))
print(f"Part 1: {count}")
window_sums = [a + b + c  for a, b, c in zip(depths, depths[1:], depths[2:])]
count = sum(second > first for (first, second) in zip(window_sums, window_sums[1:]))
print(f"Part 2: {count}")
