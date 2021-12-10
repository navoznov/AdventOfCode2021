from typing import Counter
import numpy as np

lines = open("Day10/input.txt").read().split('\n')

mappings = {"(": ")", "[": "]", "{": "}", "<": ">"}


def get_first_illegal_character_and_stack(line):
    stack = []
    openings = mappings.keys()
    for i, ch in enumerate(line):
        if ch in openings:
            stack.append(ch)
        else:
            if len(stack) == 0:
                return ch, None

            ch2 = stack.pop()
            if ch != mappings[ch2]:
                return ch, None

    return None, stack


assert (get_first_illegal_character_and_stack("(()]")[0] == "]")

illegal_charecters = [
    get_first_illegal_character_and_stack(line) for line in lines
]

# part 1
costs = {")": 3, "]": 57, "}": 1197, ">": 25137}
print(sum([costs[x] for x, stack in illegal_charecters if x]))

# part 2


def calc_score(stack):
    result = 0
    costs = {")": 1, "]": 2, "}": 3, ">": 4}
    for x in stack:
        closing = x
        result = result * 5 + costs[closing]
    return result


assert (calc_score("])}>") == 294)
assert (calc_score("}}]])})]") == 288957)

stacks = [stack for _, stack in illegal_charecters if stack]
stacks = [reversed(s) for s in stacks]
stacks = [[mappings[x] for x in s] for s in stacks]
scores = sorted([calc_score(s) for s in stacks])

print(scores[len(scores) // 2])