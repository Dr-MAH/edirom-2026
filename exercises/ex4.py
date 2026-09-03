# Run this with `python exercises/ex4.py machine.txt` from the root of the project directory.

import sys


def readfn(fname: str) -> list[str]:
    with open(fname, "r") as fname:
        contents = fname.readlines()
    return contents

def main(fname: str) -> None:
    contents: list[str] = readfn(fname)
    for i, line in enumerate(c):
        print(f"{i} {line}")

if __name__ == "__main__":
    fn: str = sys.argv[1]
    main(fn)