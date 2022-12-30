from typing import Literal

InputStr = str | Literal["A", "B", "C", "X", "Y", "Z"]
TurnNames = Literal["rock", "paper", "scissors"]
ValidResults = Literal["win", "lose", "draw"]

mapping: dict[InputStr, TurnNames] = {
    "A": "rock",
    "X": "rock",
    "B": "paper",
    "Y": "paper",
    "C": "scissors",
    "Z": "scissors",
}

results: list[ValidResults] = ["lose", "draw", "win"]

points = {"rock": 1, "paper": 2, "scissors": 3}


rules: list[list[ValidResults]] = [
    # Rock - Paper - Scissors
    ["draw", "lose", "win"],  # Rock
    ["win", "draw", "lose"],  # Paper
    ["lose", "win", "draw"],  # Scissors
]


def battle(x: InputStr, y: InputStr) -> ValidResults:
    a = mapping[x]
    b = mapping[y]
    turn = ("rock", "paper", "scissors")
    return rules[turn.index(a)][turn.index(b)]


def calculate_score(move: TurnNames, result: ValidResults) -> int:
    return points[move] + (results.index(result) * 3)


def part1(data: list[list[InputStr]]) -> int:
    result = [calculate_score(mapping[you], battle(you, opponent)) for opponent, you in data]
    return sum(result)


if __name__ == "__main__":
    with open("inputs/day02_part1.txt") as f:
        data: list[list[str]] = [turn.split(" ") for turn in f.read().splitlines()]
        # data = [
        #     ["A", "Y"],
        #     ["B", "X"]
        # ]

    print(f"{part1(data)=:,}")
