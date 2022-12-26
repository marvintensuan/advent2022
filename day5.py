from copy import deepcopy
from itertools import compress
import re
from typing import Callable

TowerLike = dict[int, list[str]]
Crane = Callable[[str, TowerLike], None]

get_numeric = re.compile("\d+")


def move(instr: str, data: TowerLike) -> None:
    n, src, dest = map(int, get_numeric.findall(instr))
    for _ in range(n):
        item = data[src].pop()
        data[dest].append(item)


def move_many_at_once(instr: str, data: TowerLike) -> None:
    n, src, dest = map(int, get_numeric.findall(instr))

    _new_src, _append_dest = data[src][: len(data[src]) - n], data[src][-n:]
    data[src] = _new_src
    data[dest] += _append_dest


def solution(data: TowerLike, instructions: list[str], mover: Crane = move) -> str:
    _data = deepcopy(data)

    for instruction in instructions:
        mover(instruction, _data)

    return "".join([value.pop() for value in _data.values()])


if __name__ == "__main__":

    with open("inputs/day05_part1.txt") as f:
        _data = f.read().splitlines()

    data_instr = _data[10:]

    compressor: list[bool] = [c.isdigit() for c in _data[8]]
    compressed = [[*compress(element, compressor)] for element in _data[0:8]]
    transposed = [*zip(*reversed(compressed))]

    dv = [[c for c in element if c.isalpha()] for element in transposed]

    data: TowerLike = {key: value for key, value in zip(range(1, 10), dv)}

    sample_data = {1: ["Z", "N"], 2: ["M", "C", "D"], 3: ["P"]}

    sample_instr = [
        "move 1 from 2 to 1",
        "move 3 from 1 to 3",
        "move 2 from 2 to 1",
        "move 1 from 1 to 2",
    ]

    print(f"{solution(data, data_instr)=}")
    print(f"{solution(sample_data, sample_instr)=}")
    print(f"{solution(data, data_instr, mover=move_many_at_once)=}")
    print(f"{solution(sample_data, sample_instr, mover=move_many_at_once)=}")
