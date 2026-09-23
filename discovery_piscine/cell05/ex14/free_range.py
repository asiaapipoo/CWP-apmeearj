#!/usr/bin/env python3
import sys

if len(sys.argv) == 3:
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        step = 1 if a <= b else -1
        print(list(range(a, b + step, step)))
    except ValueError:
        print("none")
else:
    print("none")