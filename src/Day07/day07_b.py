class Day07B:
    def __init__(self, data: str) -> None:
        self.data = data

    def run(self) -> None:
        grid = self.data.splitlines()
        splitters = [
            (ridx, cidx)
            for ridx, row in enumerate(grid)
            for cidx, col in enumerate(row)
            if col == "^"
        ]
        directions = {"down": (1, 0), "right": (0, 1), "left": (0, -1)}
        memo: dict[tuple[int, int], int] = {}

        print(self.paths((0, grid[0].index("S")), grid, splitters, directions, memo))

    def paths(
        self,
        node: tuple[int, int],
        grid: list[str],
        splitters: list[tuple[int, int]],
        directions: dict[str, tuple[int, int]],
        memo: dict[tuple[int, int], int],
    ) -> int:
        if node in memo:
            return memo[node]

        if node[0] >= len(grid):
            return 1

        total = 0

        t = (node[0] + directions["down"][0], node[1] + directions["down"][1])
        if t in splitters:
            tl = (t[0] + directions["left"][0], t[1] + directions["left"][1])
            tr = (t[0] + directions["right"][0], t[1] + directions["right"][1])
            if 0 <= tl[1] < len(grid[0]):
                total += self.paths(tl, grid, splitters, directions, memo)
            if 0 <= tr[1] < len(grid[0]):
                total += self.paths(tr, grid, splitters, directions, memo)
        else:
            total += self.paths(t, grid, splitters, directions, memo)

        memo[node] = total

        return total
