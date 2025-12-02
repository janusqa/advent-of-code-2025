import re

from utils import modulo


class Day01A:
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
            match direction:
                case "R":
                    current = modulo(current + moves, self.max_num)
                case "L":
                    current = modulo(current - moves, self.max_num)

            if current == 0:
                password += 1

        print(password)
