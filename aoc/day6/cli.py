from pathlib import Path

import typer

from .load_data import load_data
from .traverse import traverse

app = typer.Typer()


@app.command()
def part1(file_path: Path) -> None:
    position, board = load_data(file_path)

    board, _ = traverse(position, board)

    result = sum(row.count("X") for row in board)

    typer.echo(result)


@app.command()
def part2(file_path: Path) -> None:
    position, board = load_data(file_path)

    board, result = traverse(position, board)

    for position in result:
        board[position[0]][position[1]] = "O"
    typer.echo("\n".join("".join(row) for row in board))

    typer.echo(len(result))


@app.command()
def cheat(file_path: Path) -> None:
    G = {
        i + j * 1j: c
        for i, r in enumerate(open(file_path))
        for j, c in enumerate(r.strip())
    }

    start = min(p for p in G if G[p] == "^")

    def walk(G):
        pos, dir, seen = start, -1, set()
        while pos in G and (pos, dir) not in seen:
            seen |= {(pos, dir)}
            if G.get(pos + dir) == "#":
                dir *= -1j
            else:
                pos += dir
        return {p for p, _ in seen}, (pos, dir) in seen

    path = walk(G)[0]
    print(len(path), sum(walk(G | {o: "#"})[1] for o in path))
