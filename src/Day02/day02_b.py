import re

from utils import modulo


class Day01B:
    def __init__(self, data: str) -> None:
        self.data = data
        self.max_num = 100

    def run(self) -> None:
        pattern = r"^(R|L)(\d{1,})$"
        matches = re.findall(pattern, self.data, re.MULTILINE)

        current = 50
        password = 0

        for direction, moves_str in matches:
            moves = int(moves_str)

            full_cycles = moves // self.max_num
            partial_cycle = moves % self.max_num

            match direction:
                case "R":
                    if (
                        partial_cycle > 0
                        and current != 0
                        and current + partial_cycle >= self.max_num
                    ):
                        password += 1
                    current = modulo(current + moves, self.max_num)
                case "L":
                    if (
                        partial_cycle > 0
                        and current != 0
                        and current - partial_cycle <= 0
                    ):
                        password += 1
                    current = modulo(current - moves, self.max_num)

            password += full_cycles

        print(password)
