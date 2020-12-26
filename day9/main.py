from itertools import combinations
from collections import deque

import numpy as np


def is_valid(values, value):
    for t in combinations(set(values), 2):
        if sum(t) == value:
            return True
    return False


def find_invalid(values, preamble_size=25):
    preamble = deque(values[:preamble_size])
    values = values[preamble_size:]
    for value in values:
        if not is_valid(preamble, value):
            return value
        else:
            preamble.popleft()
            preamble.append(value)


def find_weakness(values, invalid):
    start, end = 0, 1
    while True:
        weakness = values[start:end]
        current_sum = sum(weakness)
        if current_sum < invalid:
            end += 1
        elif current_sum > invalid:
            start += 1
        else:
            break
    return min(weakness) + max(weakness)


if __name__ == "__main__":
    values = np.fromfile("input", dtype=int, sep="\n")
    values_test = np.fromfile("input_test", dtype=int, sep="\n")

    print("Part One")
    assert find_invalid(values_test, 5) == 127
    invalid = find_invalid(values)
    print(invalid)

    print("Part Two")
    assert find_weakness(values_test, 127) == 62
    print(find_weakness(values, invalid))

    print("done")
