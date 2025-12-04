from collections import deque

from utils import cardinal_directions, out_of_bounds


class Day04B:
    def __init__(self, data: str) -> None:
        self.data = data

    def run(self) -> None:  # noqa: C901
        grid: list[list[str]] = []
        for line in self.data.splitlines():
            grid.append(list(line))

        inventory: dict[tuple[int, int], list[tuple[int, int]]] = {}

        for r_index, r_value in enumerate(grid):
            for c_index, c_value in enumerate(r_value):
                if c_value == "@":
                    inventory[(r_index, c_index)] = []
                    for x, y in cardinal_directions(movement=8):
                        rr = r_index + x
                        cc = c_index + y
                        if out_of_bounds(rr, cc, len(grid) - 1, len(grid[0]) - 1):
                            continue
                        if grid[rr][cc] == "@":
                            inventory[(r_index, c_index)].append((rr, cc))

        queue: deque[tuple[int, int]] = deque()
        removed = 0

        for roll, neighbours in inventory.items():
            if len(neighbours) < 4:  # noqa: PLR2004
                queue.append(roll)

        while queue:
            roll = queue.popleft()
            removed += 1
            for neighbour in inventory[roll]:
                inventory[neighbour][:] = [n for n in inventory[neighbour] if n != roll]
                if len(inventory[neighbour]) < 4 and neighbour not in queue:  # noqa: PLR2004
                    queue.append(neighbour)
