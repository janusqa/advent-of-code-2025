class Day06A:
    def __init__(self, data: str) -> None:
        self.data = data

    def run(self) -> None:
        digits: list[list[int]] = []
        operators: list[str] = []
        rows = self.data.splitlines()

        for row in rows[:-1]:
            digits.append(
                [int(item.strip()) for item in row.split(" ") if len(item.strip()) > 0],
            )

        operators.extend(
            [item.strip() for item in rows[-1].split(" ") if len(item.strip()) > 0],
        )

        answers = [0 if operator == "+" else 1 for operator in operators]
        for drow in digits:
            for idx, col in enumerate(drow):
                match operators[idx]:
                    case "+":
                        answers[idx] += col
                    case "*":
                        answers[idx] *= col

        print(sum(answers))
