from pathlib import Path

import typer

from .analyze_report import is_safe
from .load_reports import load_reports

app = typer.Typer()


@app.command()
def part1(file_path: Path) -> None:
    """Run day2."""
    reports = load_reports(file_path)

    saftey = [is_safe(report) for report in reports]
    result = sum(saftey)

    print(result)
