from pathlib import Path
from collections import Counter


def count_answers(group):
    answers = group.replace("\n", "")
    return len(set(answers))


def count_all_yes(group):
    counter = Counter(group)
    group_size = (counter.get("\n") or 0) + 1
    return len({answer for answer, count in counter.items() if count == group_size})


if __name__ == "__main__":
    groups = Path("input").read_text().strip().split("\n\n")
    groups_test = Path("input_test").read_text().strip().split("\n\n")

    print("Part One")
    assert sum(count_answers(group) for group in groups_test) == 11

    print(sum(count_answers(group) for group in groups))

    print("Part Two")
    assert sum(count_all_yes(group) for group in groups_test) == 6

    print(sum(count_all_yes(group) for group in groups))
    print("done")
