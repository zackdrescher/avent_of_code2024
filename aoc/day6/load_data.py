from pathlib import Path

from .guard import GUARD_SYMBOLS

Board = list[list[str]]
Position = tuple[int, int]


def load_data(file_path: Path) -> tuple[Position, Board]:
    guard_position = None
    board = []

    with file_path.open() as file:
        for r, line in enumerate(file):
            board.append(list(line.strip()))
            for c, char in enumerate(line):
                if char == "^":
                    if guard_position is not None:
                        msg = f"More than one guard found. first: {guard_position}, second: {(r,c)}"
                        raise ValueError(
                            msg,
                        )
                    guard_position = (r, c)

    if guard_position is None:
        msg = "No gaurd found!"
        raise ValueError(msg)

    return guard_position, board
