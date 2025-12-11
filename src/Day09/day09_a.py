import re
from math import prod


class Day09A:
    def __init__(self, data: str) -> None:
        self.data = data

    def run(self) -> None:
        pattern = r"^(\d{1,}),(\d{1,})$"
        reds = [
            (int(x), int(y)) for x, y in re.findall(pattern, self.data, re.MULTILINE)
        ]

        pairs = [
            (reds[i], reds[j])
            for i in range(len(reds))
            for j in range(i + 1, len(reds))
        ]

        largest = 0
        for p1, p2 in pairs:
            largest = max(
                largest,
                prod(
                    [abs(a - b) + 1 for a, b in zip(p1, p2, strict=True)],
                ),
            )

        print(largest)
