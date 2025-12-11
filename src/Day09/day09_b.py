import re
from math import prod

import matplotlib.pyplot as plt


class Day09B:
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

        rectangles: list[tuple[tuple[tuple[int, int], tuple[int, int]], int]] = []
        for p1, p2 in pairs:
            rectangles.append(
                (
                    (p1, p2),
                    prod(
                        [abs(a - b) + 1 for a, b in zip(p1, p2, strict=True)],
                    ),
                ),
            )
        rectangles = sorted(rectangles, key=lambda x: x[1], reverse=True)

        boundary: list[tuple[int, int]] = []
        n = len(reds)
        for i in range(n):
            p1 = reds[i]
            p2 = reds[(i + 1) % n]  # wraps around
            boundary.extend(self.draw_line(p1, p2))
            boundary.append(p2)

        allowed, offset_x, offset_y = self.allowed_grid(boundary)

        for (t1, t2), area in rectangles:
            xmin, xmax = sorted([t1[0], t2[0]])
            ymin, ymax = sorted([t1[1], t2[1]])

            valid = True

            # Check top & bottom edges
            for x in range(xmin, xmax + 1):
                if (
                    not allowed[ymin - offset_y][x - offset_x]
                    or not allowed[ymax - offset_y][x - offset_x]
                ):
                    valid = False
                    break

            # Check left & right edges
            if valid:
                for y in range(ymin + 1, ymax):
                    if (
                        not allowed[y - offset_y][xmin - offset_x]
                        or not allowed[y - offset_y][xmax - offset_x]
                    ):
                        valid = False
                        break

            if valid:
                print("Largest rectangle found:", (t1, t2), "Area:", area)
                break  # first valid rectangle is the largest

        # print(self.allowed(boundary))
        # self.draw_plot(boundary)

    def draw_line(
        self,
        p1: tuple[int, int],
        p2: tuple[int, int],
    ) -> list[tuple[int, int]]:
        x1, y1 = p1
        x2, y2 = p2

        line: list[tuple[int, int]] = []

        if x1 == x2:
            start = min(y1, y2) + 1
            end = max(y1, y2)
            for p in range(start, end):
                line.append((x1, p))
        elif y1 == y2:
            start = min(x1, x2) + 1
            end = max(x1, x2)
            for p in range(start, end):
                line.append((p, y1))
        else:
            msg = f"Points not aligned: {p1} -> {p2}"
            raise ValueError(msg)

        return line

    def allowed_grid(
        self,
        polygon: list[tuple[int, int]],
    ) -> tuple[list[list[bool]], int, int]:
        # calculate tight bounding box for polygon.  It will touch the polygon
        xs = [x for x, y in polygon]
        ys = [y for x, y in polygon]
        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)

        # set up an allowed grid based on the bounding box and initialize
        # every cell to false.
        width = max_x - min_x + 1
        height = max_y - min_y + 1
        # allowed[y][x] will correspond to grid coordinates: (x+min_x, y+min_y)
        allowed = [[False for _ in range(width)] for _ in range(height)]

        # on the allowed grid mark all boundary points as True, to indicate that
        # this point is in the polygon. note we need to off set each point  to line up
        # with our allowed grid
        for x, y in polygon:
            allowed[y - min_y][x - min_x] = True

        # Fill the interal area of the polygon
        for y in range(height):
            row = allowed[y]
            xs_true = [i for i, v in enumerate(row) if v]
            if xs_true:
                xmin_row, xmax_row = min(xs_true), max(xs_true)
                for x in range(xmin_row, xmax_row + 1):
                    row[x] = True

        return (allowed, min_x, min_y)

    def draw_plot(
        self,
        boundary: list[tuple[int, int]],
    ) -> None:
        if not boundary:
            return

        # 1️⃣ Find min/max to normalize
        x_coords = [x for x, _ in boundary]
        y_coords = [y for _, y in boundary]

        # Plot points and connect them in order

        plt.figure(figsize=(12, 12))
        plt.scatter(x_coords, y_coords, color="red", s=10)
        plt.plot(
            x_coords + [x_coords[0]],  # noqa: RUF005
            y_coords + [y_coords[0]],  # noqa: RUF005
            color="green",
            linewidth=1,
        )

        # Optional: invert y-axis to match typical grid orientation
        plt.gca().invert_yaxis()

        # Equal aspect ratio to avoid distortion
        plt.axis("equal")
        plt.show()
