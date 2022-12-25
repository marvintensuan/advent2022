from string import ascii_letters

from more_itertools import chunked

priority: dict = dict(zip(ascii_letters, range(1, 57)))


def split_half(txt: str) -> tuple[str, str]:
    el = len(txt) // 2
    return txt[:el], txt[el:]


def get_common(first: str, second: str) -> str:
    common = set(first) & set(second)
    assert len(common) == 1, f"There are more than 1 {common=}"
    return common.pop()


def get_common_three(first: str, second: str, third: str) -> str:
    common = set(first) & set(second) & set(third)
    assert len(common) == 1, f"There are more than 1 {common=}"
    return common.pop()


sample = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw",
]


def part1(data: list[str]) -> int:
    splat = [split_half(item) for item in data]
    commons = [get_common(a, b) for a, b in splat]
    priorities = [priority[letter] for letter in commons]
    return sum(priorities)


def part2(data: list[str]) -> int:
    chunk3 = [*chunked(data, 3)]
    commons = [get_common_three(a, b, c) for a, b, c in chunk3]
    priorities = [priority[letter] for letter in commons]
    return sum(priorities)


with open("inputs/day03_part1.txt") as f:
    data = f.read().splitlines()

print(f"{part1(data)=:,}")
print(f"{part2(data)=:,}")
