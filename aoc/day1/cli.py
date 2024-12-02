"""CLI for day1."""

import logging
from pathlib import Path

import typer

from .load_lists import load_lists
from .value_counts import value_counts

logger = logging.getLogger(__name__)

app = typer.Typer()


@app.command()
def part1(file_path: Path) -> None:
    """Run day1."""
    logger.info("Running day1")
    list1, list2 = load_lists(file_path)
    list1.sort()
    list2.sort()
    result = sum(abs(one - two) for one, two in zip(list1, list2))

    typer.echo(f"Result: {result}")


@app.command()
def part2(file_path: Path) -> None:
    """Run day1."""
    logger.info("Running day1")
    list1, list2 = load_lists(file_path)

    counts = value_counts(list2)

    result = sum(number * counts.get(number, 0) for number in list1)

    typer.echo(f"Result: {result}")
