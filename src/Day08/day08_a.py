import math
from collections import deque

from utils import euclidean


class Day08A:
    def __init__(self, data: str) -> None:
        self.data = data

    def run(self) -> None:  # noqa:C901
        boxes = [
            tuple(int(item) for item in row.split(","))
            for row in self.data.splitlines()
        ]

        distances: dict[tuple[int, int], float] = {}

        for i in range(len(boxes)):
            for j in range(i + 1, len(boxes)):
                distances[(i, j)] = round(euclidean(boxes[i], boxes[j]), 2)

        short_list = [
            item[0] for item in sorted(distances.items(), key=lambda k: k[1])
        ][:1000]

        circuits: dict[int, list[int]] = {}

        for n1, n2 in short_list:
            if n1 not in circuits:
                circuits[n1] = []
            if n2 not in circuits:
                circuits[n2] = []
            circuits[n1].append(n2)
            circuits[n2].append(n1)

        bfs: deque[int] = deque()
        visited: set[int] = set()
        connected: list[int] = []
        for node in circuits:
            c: list[int] = []
            bfs.append(node)
            while bfs:
                n = bfs.popleft()
                if n in visited:
                    continue
                c.append(n)
                visited.add(n)
                for neighbour in circuits[n]:
                    if neighbour in visited:
                        continue
                    bfs.append(neighbour)

            if len(c) > 0:
                connected.append(len(c))

        print(math.prod(sorted(connected, reverse=True)[:3]))
