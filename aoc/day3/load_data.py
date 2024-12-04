from pathlib import Path


def load_data(file_path: Path) -> str:
    with file_path.open() as file:
        return file.read()
