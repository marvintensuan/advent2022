from copy import deepcopy
from itertools import compress
import re
from typing import Callable

TowerLike = dict[int, list[str]]
Crane = Callable[[str, TowerLike, bool], None]

get_numeric = re.compile("\d+")


def move(instr: str, data: TowerLike, reverse=False) -> None:
    n, src, dest = map(int, get_numeric.findall(instr))

    _new_src, _append_dest = data[src][: len(data[src]) - n], data[src][-n:]
    data[src] = _new_src
    data[dest] += _append_dest if reverse else _append_dest[::-1]


def solution(data: TowerLike, instructions: list[str], mover: Crane = move, reverse=True) -> str:
    _data = deepcopy(data)

    for instruction in instructions:
        mover(instruction, _data, reverse)

    return "".join([value.pop() for value in _data.values()])


if __name__ == "__main__":

    with open("inputs/day05_part1.txt") as f:
        _data = f.read().splitlines()

    data_instr = _data[10:]

    mask: list[bool] = [c.isdigit() for c in _data[8]]
    compressed = [[*compress(element, mask)] for element in _data[0:8]]
    transposed = [*zip(*reversed(compressed))]

    dv = [[c for c in element if c.isalpha()] for element in transposed]

    data: TowerLike = {key: value for key, value in zip(range(1, 10), dv)}


    print(f"{solution(data, data_instr, reverse=True)=}")
    print(f"{solution(data, data_instr, reverse=False)=}")
