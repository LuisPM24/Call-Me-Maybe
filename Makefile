MYPY = $(VENV)/bin/mypy
FLAKE8 = $(VENV)/bin/flake8
PIP = $(VENV)/bin/pip
CONFIG_FILE = config.txt

install:
	uv sync

run:
	uv run python -m src

debug:
	uv run python -m pdb -m src

test:
	uv run pytest

clean:
	rm -rf __pycache__ src/__pycache__ tests/__pycache__
	rm -rf .mypy_cache .pytest_cache

lint:
	uv run flake8 .
	uv run mypy . --warn-return-any --warn-unused-ignores \
		--ignore-missing-imports --disallow-untyped-defs \
		--check-untyped-defs

lint-strict:
	uv run flake8 .
	uv run mypy . --strict

.PHONY: install run debug test clean lint lint-strict