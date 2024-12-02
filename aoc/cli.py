"""CLI for Advent of Code."""

import logging

import typer

from . import day1

logger = logging.getLogger(__name__)

app = typer.Typer()

app.add_typer(day1.app, name="day1")


@app.callback()
def setup(log_level: str = "INFO") -> None:
    """Set up the CLI."""
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    logger.debug("Log level set to %s via cli option", log_level)


if __name__ == "__main__":
    app()
