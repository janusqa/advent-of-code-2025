def modulo(index: int, wrap_at: int, start_at: int = 0) -> int:
    """
    Return index wrapped into a range.

    Parameters
    ----------
    index : int
        The number to wrap.
    wrap_at : int
        The modulus / maximum value + 1 (for 0-based) or max value (for 1-based).
    start_at : int, optional
        Where to start the wrapping. Use 0 for 0-based (0..wrap_at-1)
        and 1 for 1-based (1..wrap_at). Default is 0.

    """
    return (
        (index % wrap_at + wrap_at) % wrap_at
        if start_at == 0
        else ((index - 1) % wrap_at) + 1
    )


def out_of_bounds(row: int, col: int, rubound: int, cubound: int) -> bool:
    return row < 0 or row > rubound or col < 0 or col > cubound


def cardinal_directions(movement: int = 4) -> list[tuple[int, int]]:
    base = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    diag = [(1, -1), (1, 1), (-1, 1), (-1, -1)]

    return base + diag if movement == 8 else base  # noqa: PLR2004
