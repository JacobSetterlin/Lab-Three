"""
Word Counter
Jacob Setterlin
This file is used to hold the main logic of the program.

Last updated on 10/1/2026
"""

from pathlib import Path

def main():
    """Used to run the main logic of the program."""

    file_paths = {"1": Path.cwd() / "textfiles" / "monte_cristo.txt",
                  "2": Path.cwd() / "textfiles" / "princess_mars.txt",
                  "3": Path.cwd() / "textfiles" / "Tarzan.txt",
                  "4": Path.cwd() / "textfiles" / "treasure_island.txt"}

main()