from collections import deque


class Day07A:
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

        tachyons: deque[tuple[int, int]] = deque()
        visited: set[tuple[int, int]] = set()

        tachyons.append((0, grid[0].index("S")))
        visited.add((0, grid[0].index("S")))

        splits = 0

        while tachyons:
            r, c = tachyons.popleft()
            t = (r + directions["down"][0], c + directions["down"][1])

            if t[0] >= len(grid) or t in visited:
                continue

            if t in splitters:
                splits += 1
                tl = (t[0] + directions["left"][0], t[1] + directions["left"][1])
                tr = (t[0] + directions["right"][0], t[1] + directions["right"][1])
                if 0 <= tl[1] < len(grid[0]) and tl not in visited:
                    tachyons.append(tl)
                    visited.add(tl)
                if 0 <= tr[1] < len(grid[0]) and tr not in visited:
                    tachyons.append(tr)
                    visited.add(tr)
            else:
                tachyons.append(t)
                visited.add(t)

        print(splits)
