from pathlib import Path

import typer

from .wordsearch import WordSearch

app = typer.Typer()


@app.command()
def part1(file_path: Path) -> None:
    """Run day4."""
    wordsearch = WordSearch.from_file(file_path)
    result = wordsearch.count("XMAS")
    typer.echo(result)


@app.command()
def part2(file_path: Path) -> None:
    """Run day4."""
    wordsearch = WordSearch.from_file(file_path)
    result = wordsearch.count_cross()
    typer.echo(result)
