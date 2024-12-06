"""CLI for Advent of Code."""

import logging

import typer

from . import day1, day2, day3, day4, day5

logger = logging.getLogger(__name__)

app = typer.Typer()

app.add_typer(day1.app, name="day1")
app.add_typer(day2.app, name="day2")
app.add_typer(day3.app, name="day3")
app.add_typer(day4.app, name="day4")
app.add_typer(day5.app, name="day5")


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
