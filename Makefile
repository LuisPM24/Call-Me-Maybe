VENV = venv
PYTHON = $(VENV)/bin/python3
MYPY = $(VENV)/bin/mypy
FLAKE8 = $(VENV)/bin/flake8
PIP = $(VENV)/bin/pip
CONFIG_FILE = config.txt

install:
	uv sync

run:
	uv run $(PYTHON) -m src

debug:
	uv run $(PYTHON) -m pdb -m src

clean:
	rm -rf __pycache__ src/__pycache__ .mypy_cache .pytest_cache

lint:
	uv run $(FLAKE8) .
	uv run $(MYPY) . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	uv run $(FLAKE8) .
	uv run $(MYPY) . --strict

.PHONY: install run debug clean lint lint-strict