from collections import Counter


def get_power(report):
    gamma, epsilon = "", ""
    for bit in range(len(report[0])):
        gamma += get_most_common(bit, report)
        epsilon += get_least_common(bit, report)
    return int(gamma, 2) * int(epsilon, 2)


def get_most_common(bit, candidates):
    counts = Counter([c[bit] for c in candidates])
    return "1" if counts["1"] >= counts["0"] else "0"


def get_least_common(bit, candidates):
    counts = Counter([c[bit] for c in candidates])
    return "0" if counts["0"] <= counts["1"] else "1"


def get_oxygen(report):
    candidates = set(report)
    for bit in range(len(report[0])):
        most_common = get_most_common(bit, candidates)
        candidates = {c for c in candidates if c[bit] == most_common}
        if len(candidates) == 1:
            return int(candidates.pop(), 2)


def get_co2(report):
    candidates = set(report)
    for bit in range(len(report[0])):
        least_common = get_least_common(bit, candidates)
        candidates = {c for c in candidates if c[bit] == least_common}
        if len(candidates) == 1:
            return int(candidates.pop(), 2)


report = [line.strip() for line in open("input/day3.in").readlines()]
print(f"Part 1: {get_power(report)}")
print(f"Part 2: {get_oxygen(report) * get_co2(report)}")
