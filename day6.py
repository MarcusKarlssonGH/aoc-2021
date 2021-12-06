def count_fish(state, days):
    counts = [state.count(n) for n in range(9)]
    for _ in range(days):
        reborn, *counts = counts
        counts.append(reborn)
        counts[6] += reborn
    return sum(counts)

state = [int(x) for x in open("input/day6.in").read().strip().split(",")]
print(f"Part 1: {count_fish(state, 80)}")
print(f"Part 2: {count_fish(state, 256)}")
