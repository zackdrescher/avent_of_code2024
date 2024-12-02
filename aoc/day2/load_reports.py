from pathlib import Path


def load_reports(file_path: Path) -> list[list[int]]:
    """Load reports from file."""
    with file_path.open() as file:
        return [[int(x) for x in line.split(" ")] for line in file]
