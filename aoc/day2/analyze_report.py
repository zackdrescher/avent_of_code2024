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
