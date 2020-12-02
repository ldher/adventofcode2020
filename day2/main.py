import re
from collections import Counter
from pathlib import Path


REGEX_DB_LINE = re.compile(r"(\d+)-(\d+) (\S): (\S+)")


def is_valid_part_one(i, j, letter, password):
    letter_count = Counter(password).get(letter)
    if letter_count is None:
        return False
    if int(i) <= letter_count <= int(j):
        return True
    return False


def is_valid_part_two(i, j, letter, password):
    i_ok, j_ok = password[i - 1] == letter, password[j - 1] == letter
    return i_ok + j_ok == 1


def is_valid(line, validation_func):
    match = re.match(REGEX_DB_LINE, line)
    i, j, letter, password = match.groups()
    return validation_func(int(i), int(j), letter, password)


if __name__ == '__main__':
    db = Path("input").read_text().strip().split('\n')

    print("Part One")
    assert is_valid("1-3 a: abcde", is_valid_part_one)
    assert not is_valid("1-3 b: cdefg", is_valid_part_one)
    assert is_valid("2-9 c: ccccccccc", is_valid_part_one)
    print(sum(is_valid(line, is_valid_part_one) for line in db))

    print("Part Two")
    assert is_valid("1-3 a: abcde", is_valid_part_two)
    assert not is_valid("1-3 b: cdefg", is_valid_part_two)
    assert not is_valid("2-9 c: ccccccccc", is_valid_part_two)
    print(sum(is_valid(line, is_valid_part_two) for line in db))

    print("done")
