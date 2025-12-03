class Day03A:
    def __init__(self, data: str) -> None:
        self.data = data

    def run(self) -> None:
        banks = self.data.splitlines()

        total_voltage = 0
        for bank in banks:
            total_voltage += self.largest_voltage(bank)

        print(total_voltage)

    def largest_voltage(self, bank: str) -> int:
        max_first = max(bank[:-1])
        index = bank.index(max_first)
        max_second = max(bank[index + 1 :])

        return int(f"{max_first}{max_second}")
