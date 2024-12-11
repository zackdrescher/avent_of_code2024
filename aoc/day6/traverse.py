from .guard import GUARD_SYMBOLS, GUARD_TRANSITIONS
from .load_data import Board, Position


def left_board(position: Position, height: int, width: int) -> bool:
    return (
        position[0] < 0
        or position[1] < 0
        or position[1] >= width
        or position[0] >= height
    )


def traverse(position: Position, board: Board) -> Board:
    height = len(board)
    width = len(board[0])

    if any(len(row) != width for row in board):
        msg = "Board is not rectangular"
        raise ValueError(msg)

    guard = "^"

    while not left_board(position, height, width):
        board[position[0]][position[1]] = "X"

        move = GUARD_SYMBOLS[guard]
        next_postion = (position[0] + move[0], position[1] + move[1])

        if (
            not left_board(next_postion, height, width)
            and board[next_postion[0]][next_postion[1]] == "#"
        ):
            guard = GUARD_TRANSITIONS[guard]
            continue

        position = next_postion

    return board
