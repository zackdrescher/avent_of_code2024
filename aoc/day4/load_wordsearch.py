from pathlib import Path


def load_data(file_path: Path) -> list[str]:
    with file_path.open() as file:
        return [line.strip() for line in file]
