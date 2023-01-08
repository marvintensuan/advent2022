from functools import reduce
from itertools import product
from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    from collections.abc import Sequence

Address: TypeAlias = tuple[int, int]
InputData: TypeAlias = Sequence[Sequence[int]]


def perimeter_count(data):
    assert len(data) == len(data[0]), "Data is not a square"
    return len(data) * 4 - 4


def generate_addresses(n: int) -> list[Address]:
    return [*product(range(n), range(n))]


def addresses_of_edges(n: int) -> set[Address]:
    addresses = generate_addresses(n)
    return set(addr for addr in addresses if ((0 in addr) or (n - 1 in addr)))


def scanmax(array: Sequence[int], is_reversed=False) -> list[int]:
    r: list[int] = reduce(
        lambda acc, val: acc + [max([*acc, val])], array[::-1] if is_reversed else array, []
    )
    return r[::-1] if is_reversed else r


def to_compress(array: list[int], prev=-1) -> list[bool]:
    frst = array[0]
    t: list[bool] = [frst > prev]
    if len(array) == 1:
        return [True]
    return t + to_compress(array[1:], prev=frst)


def interior(data: InputData, is_reversed=False) -> list[list[bool]]:
    _data = [scanmax(row, is_reversed=is_reversed) for row in data]
    return [to_compress(row[::-1])[::-1] if is_reversed else to_compress(row) for row in _data]


def part1(data: InputData) -> int:

    addresses = generate_addresses(len(data))
    edges = addresses_of_edges(len(data))
    T = [*zip(*data)]

    ltr = interior(data)
    rtl = interior(data, is_reversed=True)
    top_to_bot = interior(T)
    bot_to_top = interior(T, is_reversed=True)

    visible_interior_trees = set()
    for row, column in addresses:
        if (row, column) in edges:
            continue

        xval = ltr[row][column]
        yval = rtl[row][column]

        xTval = top_to_bot[column][row]
        yTval = bot_to_top[column][row]

        if any([xval, yval, xTval, yTval]):
            visible_interior_trees.add((row, column))

    return perimeter_count(data) + len(visible_interior_trees)


if __name__ == "__main__":

    with open("inputs/day08_part1.txt") as f:
        data = [[*map(int, line)] for line in f.read().splitlines()]

    print(f"{part1(data)=:,}")
