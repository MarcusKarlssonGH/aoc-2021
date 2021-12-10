OPEN = ["(", "[", "{", "<"]
CLOSE = [")", "]", "}", ">"]
MATCHING = {o: c for o, c in zip(OPEN, CLOSE)}
SCORES = {c: v for c, v in zip(CLOSE, [3, 57, 1197, 25137])}
COMPLETION_SCORES = {c: v for c, v in zip(CLOSE, [1, 2, 3, 4])}

def get_syntax_error_score(line):
    opens = []
    for c in line:
        if c in OPEN:
            opens.append(c)
        if c in CLOSE and c != MATCHING[opens.pop()]:
            return SCORES[c]
    return 0

def get_completion_score(line):
    unmatched = simplify(line)
    s = 0
    completion = [MATCHING[c] for c in unmatched[::-1]]
    for c in completion:
        s *= 5
        s += COMPLETION_SCORES[c]
    return s

def simplify(line):
    remaining = []
    for c in line:
        if c in OPEN:
            remaining.append(c)
        if c in CLOSE:
            if c == MATCHING[remaining[-1]]:
                remaining.pop()
            else:
                remaining.append(c)
    return remaining

lines = [list(line.strip()) for line in open("input/day10.in").readlines()]
syntax_error_score = sum(get_syntax_error_score(line) for line in lines)
print(f"Part 1: {syntax_error_score}")
incomplete_lines = [line for line in lines if get_syntax_error_score(line) == 0]
completion_scores = [get_completion_score(line) for line in incomplete_lines]
print(f"Part 2: {sorted(completion_scores)[len(completion_scores) // 2]}")

