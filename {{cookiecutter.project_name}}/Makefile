.PHONY: mypy lint-format check-lint-format pre-commit-install pre-commit-autoupdate upgrade-dependencies init
.ONESHELL: # Run commands in a single shell

# Initialize the project
init:
	uvx pre-commit install
	uv add --dev mypy pytest

# Run linters and formatters + auto-fix errors if possible
lint-format:
	set -e
	set -x
	uvx ruff format
	uvx ruff check --fix
	uv run mypy .

# Run linter checks without auto-fixing errors
check-lint-format:
	set -e
	set -x
	uv run mypy .
	uvx ruff check

pre-commit-install:
	uvx pre-commit install

pre-commit-autoupdate:
	uvx pre-commit autoupdate

test:
	uv run pytest

# NOTE: This won't modify the pyproject.toml file, it will only update the dependencies in the virtual environment and lock file
upgrade-dependencies:
	uv sync --upgrade

generate-requirements-txt:
	uv pip compile pyproject.toml -o requirements.txt
