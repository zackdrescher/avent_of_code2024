import re
from pathlib import Path

import typer

from .load_data import load_data

app = typer.Typer()

mul_pattern = re.compile(r"mul\((\d+),(\d+)\)")

do_pattern = re.compile(r"do\(\)")
dont_pattern = re.compile(r"don't\(\)")


@app.command()
def part1(file_path: Path) -> None:
    data = load_data(file_path)

    matches = mul_pattern.findall(data)

    result = sum(int(a) * int(b) for a, b in matches)

    typer.echo(result)


@app.command()
def part2(file_path: Path) -> None:
    data = load_data(file_path)

    dos = [do.end() for do in do_pattern.finditer(data)]
    donts = [dont.end() for dont in dont_pattern.finditer(data)]

    enabled_intervals: list[tuple[int, int]] = []
    do: int | None = 0
    while dos and donts:
        dont = donts.pop(0)

        if do is not None:
            enabled_intervals.append((do, dont))

        dos = [d for d in dos if d > dont]
        do = dos.pop(0) if dos else None
        if not do:
            break

        donts = [d for d in donts if d > do]

    if do is not None:
        enabled_intervals.append((do, len(data)))

    matches = mul_pattern.finditer(data)

    result = sum(
        int(match.group(1)) * int(match.group(2))
        for match in matches
        if any(
            match.start() >= start and match.end() <= end
            for start, end in enabled_intervals
        )
    )

    typer.echo(result)
