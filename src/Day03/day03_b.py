class Day03B:
    def __init__(self, data: str) -> None:
        self.data = data

    def run(self) -> None:
        banks = self.data.splitlines()

        total_voltage = 0
        for bank in banks:
            total_voltage += self.largest_voltage(bank)

        print(total_voltage)

    def largest_voltage(self, bank: str) -> int:
        largest: list[str] = []

        batteries_needed = 12

        while batteries_needed > 0:
            # slice of s[:-0] will give an empty sring so be careful!
            # instead return full string if you run into s[]:-0]
            select_from = (
                bank if batteries_needed - 1 == 0 else bank[: -(batteries_needed - 1)]
            )
            joltage = max(select_from)
            i = bank.index(joltage)
            batteries_needed -= 1
            bank = bank[i + 1 :]
            largest.append(joltage)

        return int("".join(largest))
