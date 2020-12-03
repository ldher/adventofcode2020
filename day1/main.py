from pathlib import Path
import numpy as np
from itertools import combinations
from math import prod


def find_2020_numpy(expenses):
    inverted_expenses = 2020 - expenses
    i, j = np.intersect1d(inverted_expenses, expenses)
    return i, j


def find_2020_param(expenses, nb):
    for t in combinations(expenses, nb):
        if sum(t) == 2020:
            return t


if __name__ == "__main__":
    input = Path("input")
    expenses_report = np.unique(np.fromfile(input, sep="\n", dtype=int))
    expenses_report.sort()

    print("Part One")
    result = find_2020_param(expenses_report, 2)
    print(f"{result} : {prod(result)}")

    result = find_2020_numpy(expenses_report)
    print(f"{result} : {np.prod(result)}")

    print("Part Two")
    result = find_2020_param(expenses_report, 3)
    print(f"{result} : {prod(result)}")

    print("done")
