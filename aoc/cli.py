"""CLI for Advent of Code."""

import typer

from . import day1

app = typer.Typer()

app.add_typer(day1.app, name="day1")

if __name__ == "__main__":
    app()
