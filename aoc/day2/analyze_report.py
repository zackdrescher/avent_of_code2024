def is_safe(report: list[int]) -> bool:
    """Check if the report is safe."""
    previous = report[0]
    is_inc: bool | None = None
    for current in report[1:]:
        diff = current - previous
        if diff == 0 or abs(diff) > 3:
            return False

        if is_inc is None:
            is_inc = diff > 0

        if is_inc != (diff > 0):
            return False

        previous = current
    return True


def safe_with_problem_dampener(report: list[int]) -> bool:
    """Check if the report is safe with a problem dampener."""
    if is_safe(report):
        return True

    def drop_value(report: list[int], index: int) -> list[int]:
        return report[:index] + report[index + 1 :]

    return any(is_safe(drop_value(report, i)) for i in range(len(report)))
