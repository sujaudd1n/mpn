#!/usr/bin/env python3
import sys

def main():
    objs = sys.argv[1:]
    for obj in objs:
        help(obj)

if __name__ == "__main__":
    main()
