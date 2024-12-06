from io import TextIOWrapper
from pathlib import Path


def load_data(
    file_path: Path,
) -> tuple[dict[int, set[int]], dict[int, set[int]], list[list[int]]]:
    with file_path.open() as file:
        preceded_by, followed_by = parse_rules(file)
        pages = parse_pages(file)

    return preceded_by, followed_by, pages


def parse_rules(file: TextIOWrapper) -> tuple[dict[int, set[int]], dict[int, set[int]]]:
    preceded_by = {}
    followed_by = {}
    line = file.readline().strip()
    while line:
        preceder, follower = map(int, line.split("|"))

        if follower not in preceded_by:
            preceded_by[follower] = {preceder}
        else:
            preceded_by[follower].add(preceder)

        if preceder not in followed_by:
            followed_by[preceder] = {follower}
        else:
            followed_by[preceder].add(follower)

        line = file.readline().strip()

    return preceded_by, followed_by


def parse_pages(file: TextIOWrapper) -> list[list[int]]:
    pages = []
    line = file.readline()
    while line:
        pages.append(list(map(int, line.split(","))))
        line = file.readline()

    return pages
