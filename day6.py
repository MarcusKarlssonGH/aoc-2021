from collections import Counter

def count_fish(state, days):
    counts = Counter(state)
    for _ in range(days):
        for timer in range(9):
            counts[timer-1] = counts[timer]

        reborn = counts[-1]
        counts[8] = reborn
        counts[6] += reborn
        counts[-1] = 0
    return sum(v for v in counts.values())

state = [int(x) for x in open("input/day6.in").read().strip().split(",")]
print(f"Part 1: {count_fish(state, 80)}")
print(f"Part 2: {count_fish(state, 256)}")


