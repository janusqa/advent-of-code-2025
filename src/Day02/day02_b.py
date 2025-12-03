import re


class Day02B:
    def __init__(self, data: str) -> None:
        self.data = data

    def run(self) -> None:
        pattern = r"(\d{1,})-(\d{1,})"
        matches = re.findall(pattern, self.data)

        total = 0

        for start, end in matches:
            for item_id in range(int(start), int(end) + 1):
                item_id_str = str(item_id)
                # double string, remove 1st and last char,
                # check that original string is in  there
                if item_id_str in (item_id_str * 2)[1:-1]:
                    total += item_id

        print(total)
