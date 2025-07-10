#!/usr/bin/env python3
"""Post-generation hook for cookiecutter template."""

import os
import shutil


def main():
    """Clean up empty directories and files."""
    # Remove .gitkeep files from directories that weren't selected
    directories_to_create = [
        "entrypoints",
        "tests",
        "notebooks",
        "data",
    ]

    for dir_name in directories_to_create:
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

    # Remove hooks directory
    if os.path.exists("hooks"):
        shutil.rmtree("hooks")

    # Run 'make init'
    os.system("make init")


if __name__ == "__main__":
    main()
