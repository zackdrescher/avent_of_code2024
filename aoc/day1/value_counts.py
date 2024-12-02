"""Contains the value_counts function."""


def value_counts(numbers: list[int]) -> dict[int, int]:
    """Count the number of occurrences of each number in a list."""
    counts = {}
    for number in numbers:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1
    return counts
