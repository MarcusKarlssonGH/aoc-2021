crabs = [int(x) for x in open("input/day7.in").read().strip().split(",")]

def get_total_cost(crabs, get_fuel):
    counts = {x: crabs.count(x) for x in crabs}
    totals = []
    for i in range(min(crabs), max(crabs)):
        totals.append(sum([get_fuel(abs(i - p)) * c for p, c in counts.items()]))
    return min(totals)

print(get_total_cost(crabs, lambda x: x))
print(get_total_cost(crabs, lambda x: sum(range(x + 1))))
