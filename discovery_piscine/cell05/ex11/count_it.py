#!/usr/bin/env python3
import sys

args = sys.argv[1:]

if args:
    print(f"parameters: {len(args)}")
    for s in args:
        print(f"{s}: {len(s)}")
else:
    print("none")