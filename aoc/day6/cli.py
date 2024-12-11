from pathlib import Path

import typer

from .load_data import load_data
from .traverse import traverse

app = typer.Typer()


@app.command()
def part1(file_path: Path) -> None:
    position, board = load_data(file_path)

    board = traverse(position, board)

    result = sum(row.count("X") for row in board)

    typer.echo(result)
