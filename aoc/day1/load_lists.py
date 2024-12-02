from pathlib import Path


def load_lists(file_path: Path) -> tuple[list[int], list[int]]:
    with file_path.open() as file:
        rows = [(int(x) for x in line.strip().split("   ")) for line in file]
    return tuple(list(t) for t in zip(*rows))
