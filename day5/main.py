from pathlib import Path


def find_seat(boarding_pass, row=(0.0, 127.0), column=(0.0, 7.0)):
    try:
        letter = boarding_pass.pop(0)
    except IndexError:
        return row[0] * 8 + column[0]

    min_, max_ = row
    increment = ((max_ - min_) + 1) / 2

    if letter == "F":
        return find_seat(boarding_pass, (min_, max_ - increment), column)

    if letter == "B":
        return find_seat(boarding_pass, (min_ + increment, max_), column)

    min_, max_ = column
    increment = ((max_ - min_) + 1) / 2

    if letter == "L":
        return find_seat(boarding_pass, row, (min_, max_ - increment))

    if letter == "R":
        return find_seat(boarding_pass, row, (min_ + increment, max_))


if __name__ == "__main__":
    boarding_passes = Path("input").read_text().strip().split("\n")

    print("Part One")
    assert find_seat(list("BFFFBBFRRR")) == 567
    assert find_seat(list("FFFBBBFRRR")) == 119
    assert find_seat(list("BBFFBBFRLL")) == 820

    seats = [find_seat(boarding_pass) for boarding_pass in map(list, boarding_passes)]
    print(max(seats))

    print("Part Two")
    min_seat, max_seat = int(min(seats)), int(max(seats))
    my_seat = sum(range(min_seat, max_seat + 1)) - sum(seats)
    print(my_seat)

    print("done")
