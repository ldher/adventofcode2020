import re
from math import prod
from pathlib import Path


REGEX_PASSPORT = re.compile(r"\S+:\S+")
PASSPORT_MANDATORY_KEYS = {
    "eyr",
    "hcl",
    "pid",
    "hgt",
    "ecl",
    "iyr",
    "byr",
}
# key : (parser, validator)
# parser raises AttributeError if format does not match
PASSPORT_VALUES_PARSERS = {
    "eyr": (
        lambda eyr: re.fullmatch(r"\d{4}", eyr).string,
        lambda eyr: 2020 <= int(eyr) <= 2030,
    ),
    "hcl": (lambda hcl: re.fullmatch(r"#[0-9a-z]{6}", hcl).string, bool),
    "pid": (lambda pid: re.fullmatch(r"\d{9}", pid).string, bool),
    "hgt": (
        lambda hgt: re.fullmatch(r"(\d+)(in|cm)", hgt).groups(),
        lambda hgt: 59 <= int(hgt[0]) <= 76
        if hgt[1] == "in"
        else 150 <= int(hgt[0]) <= 193,
    ),
    "ecl": (lambda ecl: ecl in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}, bool),
    "iyr": (
        lambda iyr: re.fullmatch(r"\d{4}", iyr).string,
        lambda iyr: 2010 <= int(iyr) <= 2020,
    ),
    "byr": (
        lambda byr: re.fullmatch(r"\d{4}", byr).string,
        lambda byr: 1920 <= int(byr) <= 2002,
    ),
    "cid": (
        lambda byr: True,
        lambda iyr: True,
    ),
}


def is_values_valid(passport):
    fields = dict(field.split(":") for field in re.findall(REGEX_PASSPORT, passport))
    if len(PASSPORT_MANDATORY_KEYS - fields.keys()) > 0:
        return False
    try:
        parsed_values = {
            k: PASSPORT_VALUES_PARSERS.get(k)[0](v) for k, v in fields.items()
        }
    except AttributeError:
        return False

    return prod(PASSPORT_VALUES_PARSERS.get(k)[1](v) for k, v in parsed_values.items())


def is_keys_valid(passport):
    field_keys = {field.split(":")[0] for field in re.findall(REGEX_PASSPORT, passport)}
    return len(PASSPORT_MANDATORY_KEYS - field_keys) == 0


if __name__ == "__main__":
    passports_test = Path("input_test").read_text().strip().split("\n\n")
    passports_test_valid = Path("input_test_valid").read_text().strip().split("\n\n")
    passports_test_invalid = (
        Path("input_test_invalid").read_text().strip().split("\n\n")
    )
    passports = Path("input").read_text().strip().split("\n\n")

    print("Part One")
    assert sum(is_keys_valid(passport) for passport in passports_test) == 2
    assert sum(is_keys_valid(passport) for passport in passports_test_valid) == 4

    print(sum(is_keys_valid(passport) for passport in passports))

    print("Part Two")
    assert sum(is_values_valid(passport) for passport in passports_test_valid) == 4
    assert sum(is_values_valid(passport) for passport in passports_test_invalid) == 0

    print(sum(is_values_valid(passport) for passport in passports))

    print("done")
