from math import prod
from pathlib import Path


def count_trees(map, right=3, down=1):
    count = 0
    line_length = len(map[0])
    for x, y in zip(range(down, len(map), down), range(right, len(map) * right, right)):
        position = map[x][y % line_length]
        if position == "#":
            count += 1
    return count


if __name__ == "__main__":
    test_map = Path("test_input").read_text().strip().split("\n")
    map = Path("input").read_text().strip().split("\n")

    print("Part One")
    assert count_trees(test_map) == 7, count_trees(test_map)

    print(count_trees(map))

    print("Part Two")
    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]
    expectation = [2, 7, 3, 4, 2]
    assert prod(expectation) == 336
    assert [count_trees(test_map, *slope) for slope in slopes] == expectation

    print(prod(count_trees(map, *slope) for slope in slopes))

    print("done")
