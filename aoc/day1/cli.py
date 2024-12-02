"""CLI for day1."""

import logging
from pathlib import Path

import typer

from .load_lists import load_lists

logger = logging.getLogger(__name__)

app = typer.Typer()


@app.command()
def run(file_path: Path) -> None:
    """Run day1."""
    logger.info("Running day1")
    list1, list2 = load_lists(file_path)
    typer.echo(f"list1: {list1}")
