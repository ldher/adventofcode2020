from collections import defaultdict
from pathlib import Path
import re


def parse_rule(rule):
    root, content = re.match(r"(\S+ \S+) bags contain (.*)", rule).groups()
    leaves = re.findall("(?:\d (\S+ \S+) bags?(?:\.|,))+", content)
    return root, leaves


def index_rules(rules, index=None):
    index = index or defaultdict(set)
    if len(rules) == 0:
        return index

    root, leaves = parse_rule(rules.pop())
    for leaf in leaves:
        index[leaf].add(root)

    return index_rules(rules, index)


def find_parents(index, parents=None, result=None):
    result = result or set()
    parents = parents if parents is not None else {"shiny gold"}

    if len(parents) == 0:
        return result

    current = parents.pop()
    try:
        new_parents = index.pop(current)
    except KeyError:
        result.add(current)
        return find_parents(index, parents, result)
    result.add(current)
    return find_parents(index, parents.union(new_parents), result)


if __name__ == "__main__":
    rules = Path("input").read_text().strip().split("\n")
    rules_test = Path("input_test").read_text().strip().split("\n")

    print("Part One")
    index_test = index_rules(rules_test)
    parents_test = find_parents(index_test)
    assert len(parents_test) - 1 == 4

    index = index_rules(rules)
    parents = find_parents(index)
    print(len(parents) - 1)

    print("done")
