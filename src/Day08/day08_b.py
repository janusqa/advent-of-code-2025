from collections.abc import Sequence


class Day08B:
    def __init__(self, data: str) -> None:
        self.data = data

    def run(self) -> None:
        boxes = [
            tuple(int(item) for item in row.split(","))
            for row in self.data.splitlines()
        ]

        distances: dict[tuple[int, int], float] = {}

        for i in range(len(boxes)):
            for j in range(i + 1, len(boxes)):
                distances[(i, j)] = self.euclidan(boxes[i], boxes[j])

        sorted_edges = [
            item[0] for item in sorted(distances.items(), key=lambda k: k[1])
        ]

        # The index represents the NODE, and the value represents the root of the node
        # node connected to itself (index == value) means its a root node of a group
        # even if that group contains only one node
        roots: list[int] = list(range(len(boxes)))

        # The index represents the ROOT of a group and the value the size
        sizes: list[int] = [1] * len(boxes)

        e1, e2 = self.kruskal(sorted_edges, roots, sizes)
        print(boxes[e1][0] * boxes[e2][0])

    def euclidan(self, p1: Sequence[int], p2: Sequence[int]) -> float:
        return sum((b - a) ** 2 for a, b in zip(p1, p2, strict=True)) ** 0.5

    def kruskal(
        self,
        sorted_edges: list[tuple[int, int]],
        roots: list[int],
        sizes: list[int],
    ) -> tuple[int, int]:
        """
        Kruskal's algorithm (Minimum spanning Tree - MST).

        Kruskal's algorithm finds a minimum spanning forest of an undirected
        edge-weighted graph. If the graph is connected, it finds a minimum spanning tree.
        It is a greedy algorithm that in each step adds to the forest the lowest-weight
        edge that will not form a cycle.[2] The key steps of the algorithm are sorting and
        the use of a disjoint-set data structure to detect cycles. Its running time is
        dominated by the time to sort all of the graph edges by their weight.

        A minimum spanning tree of a connected weighted graph is a connected subgraph, without cycles,
        for which the sum of the weights of all the edges in the subgraph is minimal. For a disconnected
        graph, a minimum spanning forest is composed of a minimum spanning tree for each connected component.
        """

        def union(edge: tuple[int, int]) -> bool:
            """Merge two edges into a group if they are not already in the same group."""
            r1 = find(edge[0])
            r2 = find(edge[1])

            if r1 == r2:
                return False

            size = 0

            # OPTIMIAZTION: Always add the maller tree to the bigger tree
            # So that we have as shallow a tree as is possible
            if sizes[r1] < sizes[r2]:
                roots[r1] = r2
                sizes[r2] += sizes[r1]
                sizes[r1] = 0
                size = sizes[r2]
            else:
                roots[r2] = r1
                sizes[r1] += sizes[r2]
                sizes[r2] = 0
                size = sizes[r1]

            return size == len(roots)

        def find(node: int) -> int:
            """
            Find root of connected group this node is in.

            Additionally compress the path between this node and the root
            of the connected group it is in.
            """
            root = node
            while roots[root] != root:
                root = roots[root]

            # OPTIMIAZTION: compress paths aka like all nodes of a group
            # directcly back to the main route of the group
            n = node
            while roots[n] != root:
                temp = roots[n]
                roots[n] = root
                n = temp

            return root

        for edge in sorted_edges:
            if union(edge):
                break

        return edge
