import sys

def open_and_read(fname: str) -> list[str]:
    with open(fname, "r") as contents:
        lines: list[str] = contents.readlines()

    return lines

def parse_line(line: str) -> str: ...



def main(fname: str) -> bool:
    encoding_contents: list[str] = open_and_read(fname)

    return True

if __name__ == "__main__":
    input_fn: str = sys.argv[1]
    success: bool = main(input_fn)
