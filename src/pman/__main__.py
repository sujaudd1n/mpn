import sys
from pman.python_help import show_python_help

if __name__ == "__main__":
    args = sys.argv[1:]
    sys.exit(show_python_help(args))
