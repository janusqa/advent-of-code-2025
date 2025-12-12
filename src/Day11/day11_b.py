import re


class Day11B:
    def __init__(self, data: str) -> None:
        self.data = data

    def run(self) -> None:
        pattern = r"^([a-z]{3}): (.+)$"
        network: dict[str, list[str]] = {
            a: b.split() for a, b in re.findall(pattern, self.data, re.MULTILINE)
        }

        memo: dict[str, int] = {}

        print(
            (
                self.count_paths("svr", "dac", network, memo)
                * self.count_paths("dac", "fft", network, memo)
                * self.count_paths("fft", "out", network, memo)
            )
            + (
                self.count_paths("svr", "fft", network, memo)
                * self.count_paths("fft", "dac", network, memo)
                * self.count_paths("dac", "out", network, memo)
            ),
        )

    def count_paths(
        self,
        start: str,
        end: str,
        network: dict[str, list[str]],
        memo: dict[str, int],
    ) -> int:
        key = f"{start}{end}"

        if key in memo:
            return memo[key]

        if start == end:
            return 1

        paths = 0

        for neighbour in network.get(start, []):
            paths += self.count_paths(neighbour, end, network, memo)

        memo[key] = paths

        return paths
