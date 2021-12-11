def parse_input(filename):
    with open(filename) as file:
        all_patterns = []
        displays = []
        for line in file.readlines():
            pat, digits = line.split("|")
            all_patterns.append([frozenset(x) for x in pat.split()])
            displays.append([frozenset(d) for d in digits.split()])
        return all_patterns, displays


def resolve(patterns):
    numbers = {}
    numbers[1] = next(p for p in patterns if len(p) == 2)
    numbers[4] = next(p for p in patterns if len(p) == 4)
    numbers[7] = next(p for p in patterns if len(p) == 3)
    numbers[8] = next(p for p in patterns if len(p) == 7)
    numbers[6] = next(p for p in patterns if len(p) == 6 and
                      len(numbers[1].intersection(p)) == 1)
    numbers[3] = next(p for p in patterns if len(p) == 5 and
                      len(numbers[1].intersection(p)) == 2)
    numbers[5] = next(p for p in patterns if len(p) == 5 and
                      len(numbers[6].intersection(p)) == 5)
    numbers[2] = next(p for p in patterns if len(p) == 5 and
                      len(numbers[5].intersection(p)) < 5 and
                      len(numbers[3].intersection(p)) < 5)
    numbers[9] = next(p for p in patterns if len(p) == 6 and
                      len(numbers[4].intersection(p)) == 4)
    numbers[0] = next(p for p in patterns if set(p) not in numbers.values())
    return {p: d for d, p in numbers.items()}


def translate(patterns, display):
    pattern2num = resolve(patterns)
    return sum(pattern2num[d] * 10 ** i for i, d in enumerate(display[::-1]))


all_patterns, displays = parse_input("input/day8.in")
nr_easy_digits = sum(len([x for x in display if len(x) in {2, 3, 4, 7}])
                     for display in displays)
print(f"Part 1: {nr_easy_digits}")
sum_of_displays = sum(translate(patterns, display)
                      for patterns, display in zip(all_patterns, displays))
print(f"Part 2: {sum_of_displays}")
