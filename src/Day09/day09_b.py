import re
from collections import deque
from itertools import pairwise
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

        lines = [(reds[i], reds[(i + 1) % len(reds)]) for i in range(len(reds))]

        pairs = [
            (reds[i], reds[j])
            for i in range(len(reds))
            for j in range(i + 1, len(reds))
        ]

        rects: list[tuple[tuple[tuple[int, int], tuple[int, int]], int]] = []
        for p1, p2 in pairs:
            rects.append(
                (
                    (p1, p2),
                    prod(
                        [abs(a - b) + 1 for a, b in zip(p1, p2, strict=True)],
                    ),
                ),
            )
        rects = sorted(rects, key=lambda x: x[1], reverse=True)

        # polygon: list[tuple[int, int]] = []
        # n = len(reds)
        # for i in range(n):
        #     p1 = reds[i]
        #     p2 = reds[(i + 1) % n]  # wraps around
        #     polygon.extend(self.draw_line(p1, p2))
        #     polygon.append(p2)

        # largest = 0
        # outside = self.outside(set(polygon))
        # for rect in rects:
        #     perimeter = self.rect_perimeter(rect[0][0], rect[0][1])
        #     if not perimeter & outside:
        #         largest = max(rect[1], largest)
        #         break

        # print(largest)

        largest: tuple[tuple[tuple[int, int], tuple[int, int]], int] | None = None
        for (a, b), area in rects:
            # Check if rectangle is completely separated from all polygon edges
            is_separated = True
            for line_start, line_end in lines:
                # Extract coordinates
                ax, ay = a
                bx, by = b
                lx1, ly1 = line_start
                lx2, ly2 = line_end

                # Determine rectangle bounds
                rect_left = min(ax, bx)
                rect_right = max(ax, bx)
                rect_bottom = min(ay, by)
                rect_top = max(ay, by)

                # Determine line bounds
                line_left = min(lx1, lx2)
                line_right = max(lx1, lx2)
                line_bottom = min(ly1, ly2)
                line_top = max(ly1, ly2)

                # Check separation
                left_of_rect = rect_right <= line_left
                right_of_rect = rect_left >= line_right
                above_rect = rect_top <= line_bottom
                below_rect = rect_bottom >= line_top

                # If the line intersects with the rectangle, break
                if not (left_of_rect or right_of_rect or above_rect or below_rect):
                    is_separated = False
                    break

            if is_separated:
                largest = ((a, b), area)
                break

        print(largest[1]) if largest else print(0)

    # def draw_line(
    #     self,
    #     p1: tuple[int, int],
    #     p2: tuple[int, int],
    # ) -> list[tuple[int, int]]:
    #     x1, y1 = p1
    #     x2, y2 = p2

    #     line: list[tuple[int, int]] = []

    #     if x1 == x2:
    #         r = range(y1 + 1, y2) if y2 > y1 else range(y1 - 1, y2, -1)
    #         for p in r:
    #             line.append((x1, p))
    #     elif y1 == y2:
    #         r = range(x1 + 1, x2) if x2 > x1 else range(x1 - 1, x2, -1)
    #         for p in r:
    #             line.append((p, y1))
    #     else:
    #         msg = f"Points not aligned: {p1} -> {p2}"
    #         raise ValueError(msg)

    #     return line

    # def outside(
    #     self,
    #     polygon: set[tuple[int, int]],
    # ) -> set[tuple[int, int]]:
    #     # Get polygon bounds
    #     xs = [x for x, _ in polygon]
    #     ys = [y for _, y in polygon]
    #     min_x, max_x = min(xs), max(xs)
    #     min_y, max_y = min(ys), max(ys)

    #     # Slightly larger bounding box to start flood fill
    #     bounding_box = [
    #         (min_x - 1, min_y - 1),
    #         (max_x + 1, min_y - 1),
    #         (max_x + 1, max_y + 1),
    #         (min_x - 1, max_y + 1),
    #     ]
    #     bxs = [x for x, _ in bounding_box]
    #     bys = [y for _, y in bounding_box]
    #     bmin_x, bmax_x = min(bxs), max(bxs)
    #     bmin_y, bmax_y = min(bys), max(bys)

    #     outside: set[tuple[int, int]] = set()
    #     queue: deque[tuple[int, int]] = deque()
    #     visited: set[tuple[int, int]] = set()

    #     queue.append(bounding_box[0])

    #     while queue:
    #         point = queue.popleft()

    #         if point in visited:
    #             continue
    #         visited.add(point)

    #         if point in polygon:
    #             continue

    #         outside.add(point)

    #         for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
    #             nx, ny = point[0] + dx, point[1] + dy
    #             if bmin_x <= nx <= bmax_x and bmin_y <= ny <= bmax_y:
    #                 queue.append((nx, ny))

    #     return outside

    # def rect_perimeter(
    #     self,
    #     p1: tuple[int, int],
    #     p2: tuple[int, int],
    # ) -> set[tuple[int, int]]:
    #     x1, y1 = p1
    #     x2, y2 = p2
    #     min_x, max_x = min(x1, x2), max(x1, x2)
    #     min_y, max_y = min(y1, y2), max(y1, y2)

    #     perimeter = set()
    #     # top and bottom edges
    #     for x in range(min_x, max_x + 1):
    #         perimeter.add((x, min_y))
    #         perimeter.add((x, max_y))
    #     # left and right edges (without corners to avoid double-count)
    #     for y in range(min_y + 1, max_y):
    #         perimeter.add((min_x, y))
    #         perimeter.add((max_x, y))
    #     return perimeter

    # def draw_plot(
    #     self,
    #     boundary: list[tuple[int, int]],
    # ) -> None:
    #     if not boundary:
    #         return

    #     # 1️⃣ Find min/max to normalize
    #     x_coords = [x for x, _ in boundary]
    #     y_coords = [y for _, y in boundary]

    #     # Plot points and connect them in order

    #     plt.figure(figsize=(12, 12))
    #     plt.scatter(x_coords, y_coords, color="red", s=10)
    #     plt.plot(
    #         x_coords + [x_coords[0]],  # noqa: RUF005
    #         y_coords + [y_coords[0]],  # noqa: RUF005
    #         color="green",
    #         linewidth=1,
    #     )

    #     # Optional: invert y-axis to match typical grid orientation
    #     plt.gca().invert_yaxis()

    #     # Equal aspect ratio to avoid distortion
    #     plt.axis("equal")
    #     plt.show()
