from marsrover.parser import parseAndExecute
import sys

def main():
    if len(sys.argv) != 2:
        print(f'Error: usage python3 {sys.argv[0]} path_to_file', file=sys.stderr)
        sys.exit(1)
    parseAndExecute(sys.argv[1])


if __name__ == "__main__":
    main()