<!-- Project-specific Copilot / AI agent instructions -->
# Copilot instructions for Final-Project-Sudoku

This repository is a small Sudoku puzzle generator. The goal of this file is to give an AI coding agent the minimal, concrete knowledge to be productive here.

- **Project shape:** Single-shot script + helper
  - Key files: `sudoku_generator.py` (core implementation), `main.sh` (attempted runner), `README.md` (fork instructions).
  - There is no tests/CI or package manifest. Treat changes as local, small edits unless the user asks to add tests.

- **Big picture / behavior:**
  - `sudoku_generator.py` implements class `SudokuGenerator` and a convenience function `generate_sudoku(size, removed)` which produces a 2D list (board) representing a Sudoku solution with `removed` cells set to `0`.
  - The generator follows a common algorithm: fill diagonal boxes, fill remaining cells with backtracking, then remove cells randomly. There is no attempt to ensure a unique solution after removal.
  - Several blocks in the file are annotated with `""" DO NOT CHANGE """` — preserve these unless the user explicitly asks to refactor those algorithms.

- **Important implementation details & gotchas:**
  - `SudokuGenerator.__init__` computes `self.box_length = math.sqrt(row_length)`. `math.sqrt` returns a float; downstream code uses `self.box_length` in `range()` calls. Be careful — if you modify or run code that expects an `int`, convert with `int(math.sqrt(...))` or `math.isqrt` to avoid TypeError.
  - `remove_cells()` uses random removal and does not check puzzle uniqueness.
  - `main.sh` currently contains `python3 sudoku.py` but there is no `sudoku.py` in the repo — prefer using `sudoku_generator.py` or create a small runner script.

- **How to run / quick examples** (use these exact snippets when adding small tests or a runner):
  - Import and call from Python REPL or a short script:

```python
from sudoku_generator import generate_sudoku
board = generate_sudoku(9, 40)  # 9x9 board, 40 removed cells
for row in board:
    print(row)
```

  - Shell (quick check):
```bash
python3 -c "from sudoku_generator import generate_sudoku; import pprint; pprint.pp(generate_sudoku(9,40))"
```

- **When editing this repo (agent-specific rules):**
  - Preserve the algorithmic blocks labelled `DO NOT CHANGE` unless the user asks for algorithmic improvements. Prefer small, local fixes (e.g., convert `box_length` to int) and document them in the change.
  - Fix obvious runtime mismatches conservatively (for example, update `main.sh` to `python3 sudoku_generator.py` only after confirming how the user wants the project executed).
  - Report any missing files referenced by scripts (e.g., `main.sh -> sudoku.py`) before creating new files that could diverge from the author's intent.

- **Common change examples** (what an AI agent may be asked to implement):
  - Add a runnable `if __name__ == '__main__'` runner to `sudoku_generator.py` that accepts CLI args: size and removed.
  - Convert `self.box_length` to an `int` and update any range usage to avoid float-related TypeError.
  - Add a small wrapper script `sudoku.py` (or update `main.sh`) that calls the generator and prints CSV/pretty output.

- **Files to inspect before making changes:**
  - `sudoku_generator.py` — core logic and algorithm comments (start here).
  - `main.sh` — broken reference to `sudoku.py`; check with the user before changing.
  - `README.md` — contains only forking instructions; no runtime guidance.

If anything here is unclear or you'd like me to make one of the suggested changes (add runner, fix `box_length`, update `main.sh`, or add a test harness), tell me which change and I'll implement it.
