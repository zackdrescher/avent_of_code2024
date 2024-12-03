from pathlib import Path

import typer

from .analyze_report import is_safe, safe_with_problem_dampener
from .load_reports import load_reports

app = typer.Typer()


@app.command()
def part1(file_path: Path) -> None:
    """Run day2."""
    reports = load_reports(file_path)

    saftey = [is_safe(report) for report in reports]
    print(saftey)
    result = sum(saftey)

    print(result)


@app.command()
def part2(file_path: Path) -> None:
    """Run day2."""
    reports = load_reports(file_path)

    saftey = [safe_with_problem_dampener(report) for report in reports]
    result = sum(saftey)

    print(result)
