from pathlib import Path

import typer

app = typer.Typer()


@app.command
def part1(file_path: Path) -> None:
    pass
