from pulp import (  # type: ignore[import-untyped]
    PULP_CBC_CMD,
    LpInteger,
    LpMinimize,
    LpProblem,
    LpVariable,
    lpSum,
)
from z3 import Int, Optimize  # type: ignore[import-untyped]


class Day10B:
    def __init__(self, data: str) -> None:
        self.data = data

    def run(self) -> None:
        rows = [part.split() for part in self.data.splitlines()]

        machines: list[tuple[list[str], list[tuple[int, ...]], tuple[int, ...]]] = []
        for row in rows:
            indicator = row[0]
            buttons = row[1:-1]
            joltages = row[-1]
            machines.append(
                (
                    list(indicator[1:-1]),
                    [
                        tuple([int(b) for b in button[1:-1].split(",")])
                        for button in buttons
                    ],
                    tuple([int(joltage) for joltage in joltages[1:-1].split(",")]),
                ),
            )

        print(sum([self.solve_z3(machine) for machine in machines]))

    def solve_z3(
        self,
        machine: tuple[list[str], list[tuple[int, ...]], tuple[int, ...]],
    ) -> int:
        """
        Linear Programming.

        Construct a system of linear equations to be solved by pulp.
        Each equation represents the target to be reached on one side
        on the other is the sum of the times each button that affects
        the target needs to be pressed.
        """
        buttons = machine[1]
        joltages = machine[2]

        # Step 1: create/initilize z3 solver
        z3_problem = Optimize()

        # Step 2: create integer variables for each button
        # x represents the times each bunntion is pressed.
        # x[0] is the number of times the first button is pressed and so on
        button_presses = [Int(f"x{i}") for i in range(len(buttons))]

        # Step 3: set contraints on variables. eg. must be greater than or equal to 0
        # NOTE: with pulp we do this driectly when creating the variables with lowBound etc.
        for bp in button_presses:
            z3_problem.add(bp >= 0)

        # Step 4: add constraints for each counter
        for i, joltage in enumerate(joltages):
            button_presses_for_joltage = [
                button_presses[bidx]
                for bidx, button in enumerate(buttons)
                if i in button
            ]
            # set up the equation for this joltage
            z3_problem.add(sum(button_presses_for_joltage) == joltage)

        # Step 5: add the ojective: minimize total presses
        z3_problem.minimize(sum(button_presses))

        # Step 6: solve
        # equivalent to pulp's solve. It's saying if a solution exists
        if z3_problem.check().r == 1:  # sat
            # the solution is in model, i.e the value of each of our variables
            model = z3_problem.model()
            return sum([model[bp].as_long() for bp in button_presses])

        raise ValueError("No solution found")

    def solve_pulp(
        self,
        machine: tuple[list[str], list[tuple[int, ...]], tuple[int, ...]],
    ) -> int:
        """
        Linear Programming.

        Construct a system of linear equations to be solved by pulp.
        Each equation represents the target to be reached on one side
        on the other is the sum of the times each button that affects
        the target needs to be pressed.
        """
        buttons = machine[1]
        joltages = machine[2]

        # Step 1: create/initilize pulp solver
        lp_problem = LpProblem("Minimize_Button_Presses", LpMinimize)

        # Step 2: create integer variables for each button
        # x represents the times each bunntion is pressed.
        # x[0] is the number of times the first button is pressed and so on
        # set constraints on variables here as well.  eg. must be greater than or equal to 0
        # and are integers
        button_presses = [
            LpVariable(f"x{b}", lowBound=0, cat=LpInteger) for b in range(len(buttons))
        ]

        # Step 3: add constraints for each counter
        for i, joltage in enumerate(joltages):
            button_presses_for_joltage = [
                button_presses[bidx]
                for bidx, button in enumerate(buttons)
                if i in button
            ]
            # set up the equation for this joltage
            lp_problem += lpSum(button_presses_for_joltage) == joltage

        # Step 4: add the ojective - minimize total presses
        lp_problem += lpSum(button_presses)

        # Step 5: solve
        lp_problem.solve(PULP_CBC_CMD(msg=0))

        return int(sum([button_press.varValue for button_press in button_presses]))
