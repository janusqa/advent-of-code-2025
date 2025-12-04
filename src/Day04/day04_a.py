from utils import cardinal_directions, out_of_bounds


class Day04A:
    def __init__(self, data: str) -> None:
        self.data = data

    def run(self) -> None:
        grid: list[list[str]] = []
        for line in self.data.splitlines():
            grid.append(list(line))

        accessible = 0

        for r_index, r_value in enumerate(grid):
            for c_index, c_value in enumerate(r_value):
                if c_value == "@":
                    rolls = 0
                    for x, y in cardinal_directions(movement=8):
                        if rolls > 3:  # noqa: PLR2004
                            break
                        rr = r_index + x
                        cc = c_index + y
                        if out_of_bounds(rr, cc, len(grid) - 1, len(grid[0]) - 1):
                            continue
                        if grid[rr][cc] == "@":
                            rolls += 1
                    if rolls <= 3:  # noqa: PLR2004
                        accessible += 1

        print(accessible)
