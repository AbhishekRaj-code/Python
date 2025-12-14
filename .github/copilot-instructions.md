# Copilot / AI Agent Instructions

Short, practical guidance for working productively in this repo.

## Purpose
- This repository is a collection of small Python learning examples (scripts, small apps, and exercises). Most files are runnable scripts (no test harnesses or packaging).

## Big picture
- Top-level folders group topics (e.g., `Control Structures/`, `Data Structure/`, `learning_flask/`).
- Most logic lives in single-file scripts intended to be run directly (look for `if __name__ == "__main__"`).
- The `learning_flask/Registration Form/` example is a minimal Flask app that uses the default `templates/` folder to render pages.

## How to run / local dev
- General: run scripts with the system Python (Windows): `python <path-to-file>` (quote paths that contain spaces). Example:
  - `python "learning_flask/Registration Form/registration.py"`
- Flask example specifics:
  - Install Flask (`pip install Flask`) if not present.
  - The example runs the app directly (`web.run(debug=True)`), so running the script starts a debug server on localhost.
- GUI example specifics:
  - `Calculator(tkinter).py` uses `tkinter` (bundled with CPython on most platforms) — run it to launch the window.
- Interactive scripts (e.g., `phoneBook.py`) use `input()` loops; run them in a terminal rather than trying to auto-test without adaptation.

## Dependencies & environment
- There is no `requirements.txt` or virtual env checked in. If you add third-party libs, add a `requirements.txt` at repo root.
- Target Python: modern 3.x (code uses f-strings and type constructs compatible with Python 3.6+; prefer 3.8+).

## Project-specific conventions and gotchas
- Filenames and folders sometimes include spaces and punctuation (e.g., `Registration Form`, `Calculator(tkinter).py`). Always quote paths in shell commands and imports where relevant.
- Keep changes minimal and focused: files are educational examples — preserve pedagogical intent (clear, readable, simple).
- Flask templates are under `learning_flask/Registration Form/templates/`. Keep template filenames stable when changing views.

## When making changes
- If you add dependencies, update `requirements.txt` and document run instructions in the example folder's README.
- For non-trivial code changes, include a small runnable example or a short script demonstrating the change (these projects have no test framework yet).
- Prefer explicit, dependency-free implementations when possible to keep examples easy to run for learners.

## Files to inspect for patterns
- `learning_flask/Registration Form/registration.py` — minimal Flask app pattern and `templates/` usage.
- `phoneBook.py` — class-based example with interactive CLI loop.
- `Calculator(tkinter).py` — example using a platform GUI (tkinter).

If anything here is unclear or you'd like me to expand a section (examples, run commands, or a short checklist for PRs), tell me which part and I'll iterate.
