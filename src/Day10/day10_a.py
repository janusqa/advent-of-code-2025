from collections import deque


class Day10A:
    def __init__(self, data: str) -> None:
        self.data = data

    def run(self) -> None:
        rows = [part.split() for part in self.data.splitlines()]

        machines: list[tuple[list[str], list[tuple[int, ...]], tuple[int, ...]]] = []
        for row in rows:
            indicator = row[0]
            buttons = row[1:-1]
            joltages = row[-1]
            machines.append(
                (
                    list(indicator[1:-1]),
                    [
                        tuple([int(b) for b in button[1:-1].split(",")])
                        for button in buttons
                    ],
                    tuple([int(joltage) for joltage in joltages[1:-1].split(",")]),
                ),
            )

        print(sum([self.solve(machine) for machine in machines]))

    def solve(
        self,
        machine: tuple[list[str], list[tuple[int, ...]], tuple[int, ...]],
    ) -> int:
        """BFS algorithm/search."""
        queue: deque[tuple[list[str], int]] = deque()
        queue.append((["."] * len(machine[0]), 0))
        visited: set[str] = set()

        while queue:
            state = queue.popleft()
            indicator, depth = state
            key = "".join(indicator)

            if key in visited:
                continue

            if key == "".join(machine[0]):
                return depth

            visited.add(key)

            for button in machine[1]:
                s = indicator[:]
                for b in button:
                    s[b] = "#" if s[b] == "." else "."
                queue.append((s, depth + 1))

        raise ValueError("Target state is unreachable")
