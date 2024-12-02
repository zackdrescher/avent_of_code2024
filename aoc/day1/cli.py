"""CLI for day1."""

import typer

app = typer.Typer()


@app.command()
def run() -> None:
    """Run day1."""
    print("Day 1 of AoC 2020!")
    print("Run with 'python -m aoc.day1'")
