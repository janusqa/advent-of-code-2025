import importlib
import sys
import time
from pathlib import Path

if __name__ == "__main__":
    # Get day and part from command line arguments
    args = sys.argv[1:]
    day = args[0].zfill(2) if len(args) > 0 else None
    part = args[1].lower() if len(args) > 1 else None

    if not day or part not in ["a", "b", "c"]:
        print("Usage: uv run runner.py <day> <part>")
        print("Example: uv run runner.py 1 a")
        sys.exit(1)

    # Build the class name dynamically
    base_dir = Path(__file__).resolve().parent
    sys.path.insert(0, str(base_dir))
    module_name = f"Day{day}.day{day}_{part}"
    class_name = f"Day{day}{part.upper()}"
    try:
        module = importlib.import_module(module_name)
        day_class = getattr(module, class_name)
    except (ModuleNotFoundError, AttributeError):
        print(f"Solution for Day {day} Part {part} not found.")
        sys.exit(1)

    # Build the file path for the solution and input file
    input_file = Path(__file__).resolve().parent / f"Day{day}" / "input.txt"
    if not input_file.exists():
        print(f"Input file for Day {day} not found.")
        sys.exit(1)

    # Load the input
    with input_file.open("r") as f:
        data = f.read()

    # Run the solution file and pass the input
    print(f"Running Advent of Code 2025 - Day {day} Part {part}...")
    day_instance = day_class(data)
    start = time.perf_counter()
    day_instance.run()
    end = time.perf_counter()
    print(f"Execution time: {end - start:.3f}s")
