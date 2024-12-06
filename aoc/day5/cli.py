from functools import cmp_to_key
from pathlib import Path

import typer

from .load_data import load_data

app = typer.Typer()


def is_valid_page(followed_by: dict[int, set[int]], page: list[int]) -> bool:
    for i, number in enumerate(page):
        preceders = followed_by.get(number, set())

        if any(follower in preceders for follower in page[i + 1 :]):
            return False

    return True


def get_center_update(page: list[int]) -> int:
    return page[len(page) // 2]


@app.command()
def part1(file_path: Path):
    preceded_by, followed_by, pages = load_data(file_path)

    valid_pages = [page for page in pages if is_valid_page(preceded_by, page)]

    print(sum(get_center_update(page) for page in valid_pages))


class Comparer:
    def __init__(
        self,
        preceded_by: dict[int, set[int]],
        followed_by: dict[int, set[int]],
    ):
        self.__followed_by = followed_by
        self.__preceded_by = preceded_by

    def __call__(self, a: int, b: int) -> int:
        a_preceders = self.__followed_by.get(a, set())
        b_preceders = self.__followed_by.get(b, set())

        if a in b_preceders:
            return -1
        if b in a_preceders:
            return 1

        a_followers = self.__preceded_by.get(a, set())
        b_followers = self.__preceded_by.get(b, set())

        if b in a_followers:
            return -1
        if a in b_followers:
            return 1

        return 0


@app.command()
def part2(file_path: Path):
    preceded_by, followed_by, pages = load_data(file_path)

    invalid_pages = [page for page in pages if not is_valid_page(preceded_by, page)]

    comp = Comparer(preceded_by, followed_by)

    for page in invalid_pages:
        page.sort(key=cmp_to_key(comp))

    print(sum(get_center_update(page) for page in invalid_pages))
