from collections import Counter, defaultdict

def parse_input(filename):
    with open(filename) as file:
        template, rest = file.read().split('\n\n')
        template = template.strip()
        pairs = [(a, b) for (a, b) in zip(template, template[1:])]
        mapping = {}
        for line in rest.splitlines():
            a, b = line.split(' -> ')
            mapping[(a[0], a[1])] = [(a[0], b), (b, a[1])]
        return pairs, mapping

def solve(nr_steps, pairs, mapping):
    def evolve(counts):
        new_counts = Counter()
        for pair, count in counts.items():
            for p in mapping[pair]:
                new_counts[p] += count
        return new_counts

    pair_counts = Counter(pairs)
    for _ in range(nr_steps):
        pair_counts = evolve(pair_counts)
    counts = Counter()
    for (left, _), count in pair_counts.items():
        counts[left] += count
    *_, (_, last) = pairs
    counts[last] += 1
    return max(counts.values()) - min(counts.values())

pairs, mapping = parse_input('input/day14.in')
print(f"Part 1: {solve(10, pairs, mapping)}")
print(f"Part 2: {solve(40, pairs, mapping)}")
