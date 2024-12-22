from .guard import GUARD_SYMBOLS, GUARD_TRANSITIONS
from .load_data import Board, Position


def left_board(position: Position, height: int, width: int) -> bool:
    return (
        position[0] < 0
        or position[1] < 0
        or position[1] >= width
        or position[0] >= height
    )


def traverse(position: Position, board: Board) -> tuple[Board, set[Position]]:
    start_position = position[:]

    height = len(board)
    width = len(board[0])

    if any(len(row) != width for row in board):
        msg = "Board is not rectangular"
        raise ValueError(msg)

    guard = "^"

    loop_positions = set()
    hits = set()

    while not left_board(position, height, width):
        board[position[0]][position[1]] = "X"

        move = GUARD_SYMBOLS[guard]
        next_postion = (position[0] + move[0], position[1] + move[1])

        if (
            not left_board(next_postion, height, width)
            and board[next_postion[0]][next_postion[1]] == "#"
        ):
            hits.add((position, guard))
            guard = GUARD_TRANSITIONS[guard]
            continue

        if (
            not left_board(next_postion, height, width)
            and next_postion != start_position
            and loop_check(
                guard,
                position,
                board,
                height,
                width,
                hits,
            )
        ):
            loop_positions.add(next_postion)

        position = next_postion

    return board, loop_positions


def loop_check(
    guard: str,
    position: Position,
    board: Board,
    height: int,
    width: int,
    hits: set[tuple[Position, str]],
) -> bool:
    board = [row.copy() for row in board]
    move = GUARD_SYMBOLS[guard]
    loop_hits: set[tuple[Position, str]] = set(hits)
    board[position[0] + move[0]][position[1] + move[1]] = "#"
    loop_hits.add((position, guard))

    right_symbol = GUARD_TRANSITIONS[guard]
    right_move = GUARD_SYMBOLS[right_symbol]

    next_position = (position[0] + right_move[0], position[1] + right_move[1])

    while not left_board(next_position, height, width):
        next_occupant = board[next_position[0]][next_position[1]]

        if next_occupant == "#":
            if (position, right_symbol) in loop_hits:
                return True

            loop_hits.add((position, right_symbol))

            right_symbol = GUARD_TRANSITIONS[right_symbol]
            right_move = GUARD_SYMBOLS[right_symbol]

        position = next_position
        next_position = (
            next_position[0] + right_move[0],
            next_position[1] + right_move[1],
        )
    return False
