import re
from math import prod


class Day12A:
    def __init__(self, data: str) -> None:
        self.data = data

    def run(self) -> None:
        problem = self.data.split("\n\n")
        regions_pattern = r"^(\d{1,}x\d{1,}): (.+)$"
        presents = [
            [
                [1 if char == "#" else 0 for char in row]
                for row in shape.splitlines()[1:]
            ]
            for shape in problem[:-1]
        ]
        present_sizes = [sum([sum(row) for row in present]) for present in presents]
        regions = [
            (
                tuple((int(wh)) for wh in k.split("x")),
                [int(n) for n in v.split()],
            )
            for k, v in re.findall(regions_pattern, problem[-1], re.MULTILINE)
        ]

        can_fit = 0
        for region in regions:
            region_area = prod(region[0])
            total_presents_area = sum(
                [
                    num_presents * present_sizes[idx]
                    for idx, num_presents in enumerate(region[1])
                ],
            )
            if region_area >= total_presents_area:
                can_fit += 1

        print(can_fit)
