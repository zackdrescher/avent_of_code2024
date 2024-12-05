from pathlib import Path

from .load_wordsearch import load_data


class WordSearch:
    @classmethod
    def from_file(cls, file_path: Path) -> "WordSearch":
        return cls(load_data(file_path))

    def __init__(self, word_search: list[str]) -> None:
        if len({len(line) for line in word_search}) != 1:
            msg = "Word search is not a rectangle"
            raise ValueError(msg)

        self.__word_search = word_search
        self.__width = len(word_search[0])
        self.__height = len(word_search)

    def __getitem__(self, index: tuple[int, int]) -> str:
        return self.__word_search[index[0]][index[1]]

    def count(self, word: str) -> int:
        count = 0
        for row_ix in range(len(self.__word_search)):
            for col_ix in range(len(self.__word_search[row_ix])):
                count += self.count_at(word, row_ix, col_ix)

        return count

    def count_at(self, word: str, row: int, col: int) -> int:
        runs = self.get_runs_at(len(word), row, col)
        count = 0
        for run in runs:
            if "".join(self[row_ix, col_ix] for row_ix, col_ix in run) == word:
                count += 1
        return count

    def get_runs_in_direction(
        self,
        length: int,
        row: int,
        col: int,
        row_delta: int,
        col_delta: int,
    ) -> list[tuple[int, int]]:
        run = []
        for i in range(length):
            row_ix = row + i * row_delta
            col_ix = col + i * col_delta
            if (
                row_ix < 0
                or row_ix >= self.__height
                or col_ix < 0
                or col_ix >= self.__width
            ):
                break
            run.append((row_ix, col_ix))
        return run

    def get_runs_at(
        self,
        length: int,
        row: int,
        col: int,
    ) -> list[list[tuple[int, int]]]:
        return [
            self.get_runs_in_direction(length, row, col, row_delta, col_delta)
            for row_delta, col_delta in [
                (0, 1),
                (1, 0),
                (0, -1),
                (-1, 0),
                (1, 1),
                (1, -1),
                (-1, 1),
                (-1, -1),
            ]
        ]

    __ms_set = {"M", "S"}

    def count_cross(self):
        count = 0
        for row_ix in range(1, len(self.__word_search) - 1):
            for col_ix in range(1, len(self.__word_search[row_ix]) - 1):
                count += self.is_cross(row_ix, col_ix)
        return count

    def is_cross(self, row: int, col: int) -> bool:
        if self[row, col] != "A":
            return False

        return {self[row + 1, col + 1], self[row - 1, col - 1]} == self.__ms_set and {
            self[row + 1, col - 1],
            self[row - 1, col + 1],
        } == self.__ms_set
