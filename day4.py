from dataclasses import dataclass


@dataclass
class CardNumber:
    row: int
    col: int
    value: int
    is_marked: bool = False

def parse_input(filename):
    with open(filename) as file:
        numbers, *rest = file.read().split("\n\n")
        numbers = [int(n) for n in numbers.split(",")]
        cards = []
        for card_string in rest:
            card = []
            for (i, line) in enumerate(card_string.splitlines()):
                for (j, n) in enumerate(line.strip().split()):
                    card.append(CardNumber(i, j, int(n)))
            cards.append(card)
        return numbers, cards

def mark(number, card):
    for cn in card:
        if cn.value == number:
            cn.is_marked = True
            return

def get_row(idx, card):
    return [number for number in card if number.row == idx]

def get_rows(card):
    dim = 5
    return [get_row(r, card) for r in range(dim)]

def get_col(idx, card):
    return [number for number in card if number.col == idx]

def get_cols(card):
    dim = 5
    return [get_col(c, card) for c in range(dim)]

def is_winner(card):
    for row in get_rows(card):
        if all(number.is_marked for number in row):
            return True
    for col in get_cols(card):
        if all(number.is_marked for number in col):
            return True
    return False

def get_winner(cards):
    return next((card for card in cards if is_winner(card)), None)

def get_marked_numbers(card):
    return [n for n in card if n.is_marked]

def get_unmarked_numbers(card):
    return [n for n in card if not n.is_marked]

def play_bingo(numbers, cards):
    scores = []
    remaining_cards = list(cards)
    for number in numbers:
        remaining_cards = [card for card in remaining_cards if not is_winner(card)]
        for card in remaining_cards:
            mark(number, card)
        if (winner := get_winner(remaining_cards)):
            unmarked_sum = sum(n.value for n in get_unmarked_numbers(winner))
            scores.append(unmarked_sum * number)
    return scores


numbers, cards = parse_input("input/day4.in")
first, *_, last = play_bingo(numbers, cards)
print(f"Part 1: {first}")
print(f"Part 2: {last}")
