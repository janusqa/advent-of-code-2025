import re


class Day02A:
    def __init__(self, data: str) -> None:
        self.data = data

    def run(self) -> None:
        pattern = r"(\d{1,})-(\d{1,})"
        matches = re.findall(pattern, self.data)

        total = 0

        for start, end in matches:
            for item_id in range(int(start), int(end) + 1):
                item_id_str = str(item_id)
                parts_len = len(item_id_str) // 2
                if (
                    len(item_id_str) % 2 == 0
                    and item_id_str[:parts_len] == item_id_str[parts_len:]
                ):
                    total += item_id

        print(total)
