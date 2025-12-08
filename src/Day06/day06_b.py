class Day06B:
    def __init__(self, data: str) -> None:
        self.data = data

    def run(self) -> None:
        rows = self.data.splitlines()
        max_row_len = max(len(row) for row in rows)
        operator_row = rows[-1]
        problem_cols: list[list[int]] = []
        for idx, col in enumerate(operator_row):
            if not problem_cols and col in "+*":
                problem_cols.append([idx, 0])
            elif col in "+*":
                problem_cols[-1][-1] = idx - 2
                problem_cols.append([idx, 0])
        problem_cols[-1][-1] = max_row_len - 1
        operators = [
            item.strip() for item in rows[-1].split(" ") if len(item.strip()) > 0
        ]
        problems = rows[:-1]

        total = 0

        for idx, problem_col in enumerate(problem_cols):
            col_total = 0 if operators[idx] == "+" else 1
            for column in range(problem_col[0], problem_col[-1] + 1):
                num = int(
                    "".join([row[column] for row in problems if row[column].isdigit()]),
                )
                match operators[idx]:
                    case "+":
                        col_total += num
                    case "*":
                        col_total *= num

            total += col_total

        print(total)
