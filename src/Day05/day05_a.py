import re


class Day05A:
    def __init__(self, data: str) -> None:
        self.data = data

    def run(self) -> None:
        pattern_id_ranges = r"^(\d{1,})-(\d{1,})$"
        pattern_id = r"^(\d{1,})$"
        id_ranges = sorted(
            [
                (int(start), int(end))
                for start, end in re.findall(pattern_id_ranges, self.data, re.MULTILINE)
            ],
            key=lambda t: t[0],
        )
        ids = [int(i) for i in re.findall(pattern_id, self.data, re.MULTILINE)]

        merged_id_ranges_list: list[list[int]] = []
        for start, end in id_ranges:
            if not merged_id_ranges_list or start > merged_id_ranges_list[-1][-1]:
                merged_id_ranges_list.append([start, end])
            else:
                merged_id_ranges_list[-1][-1] = max(end, merged_id_ranges_list[-1][-1])

        merged_id_ranges = [(start, end) for start, end in merged_id_ranges_list]

        fresh = 0

        for i in ids:
            for start, end in merged_id_ranges:
                if start <= i <= end:
                    fresh += 1

        print(fresh)
