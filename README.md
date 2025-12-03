# Advent of Code 2025
Language: PHP

# Description
Advent of Code is an Advent calendar of small programming puzzles for a variety of skill sets and skill levels that can be solved in any programming language you like. People use them as a speed contest, interview prep, company training, university coursework, practice problems, or to challenge each other.

You don't need a computer science background to participate - just a little programming knowledge and some problem solving skills will get you pretty far. Nor do you need a fancy computer; every problem has a solution that completes in at most 15 seconds on ten-year-old hardware.<br/>
Source: [Advent of Code Github Topic](https://github.com/topics/advent-of-code)<br/>

[Day 01](https://github.com/janusqa/advent-of-code-2025/tree/main/src/Day01)<br/>
[Day 02](https://github.com/janusqa/advent-of-code-2025/tree/main/src/Day02)<br/>
[Day 03](https://github.com/janusqa/advent-of-code-2025/tree/main/src/Day03)<br/>
[Day 04](https://github.com/janusqa/advent-of-code-2025/tree/main/src/Day04)<br/>
[Day 05](https://github.com/janusqa/advent-of-code-2025/tree/main/src/Day05)<br/>
[Day 06](https://github.com/janusqa/advent-of-code-2025/tree/main/src/Day06)<br/>
[Day 07](https://github.com/janusqa/advent-of-code-2025/tree/main/src/Day07)<br/>
[Day 08](https://github.com/janusqa/advent-of-code-2025/tree/main/src/Day08)<br/>
[Day 09](https://github.com/janusqa/advent-of-code-2025/tree/main/src/Day09)<br/>
[Day 10](https://github.com/janusqa/advent-of-code-2025/tree/main/src/Day10)<br/>
[Day 11](https://github.com/janusqa/advent-of-code-2025/tree/main/src/Day11)<br/>
[Day 12](https://github.com/janusqa/advent-of-code-2025/tree/main/src/Day12)<br/>
<br/>
Keywords: aoc adventofcode

### UV
- uv init .
- uv tool install ruff

### Pytest
- uv run pytest
- uv run pytest tests/test_name_of_test.py
- constraints for test
    1. Write a pytest test suite following these specific rules.
    2. Never use f-strings directly as arguments to error constructors like pytest.fail().
    3. F-strings are permitted when assigned to variables first, then passed to error constructors.
    4. Use type hints where appropriate throughout the code.
    5. Only use built-in type hinting (no imports from typing module). Exceptions require explicit approval.
    6. Absolutely no assert statements - use pytest.fail() with error messages instead.
    7. All test method docstrings must have their first line ending with a period.
    8. Pay special attention to f-string usage (rules 2-3) and type hinting restrictions (rules 4-5).
    9. Use a test class structure with fixtures as shown in the example.
      
      ```python
      from my_class_module import Solution

      class MyTestClass:
        @pytest.fixture
        def solution(self) -> Solution:
          """Return a Solution instance for testing."""
          return Solution()
      ```

    10. The method being tested must literally be named function_under_test when called.
      
      ```python
      def my_test_1(self, solution: Solution) -> None
        solution.function_under_test()
      ```

    11. Import the Solution class from "my_class_module" as specified.


