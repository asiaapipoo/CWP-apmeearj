#!/usr/bin/env python3
import sys

a = sys.argv
print(c if len(a) == 3 and (c := a[2].count(a[1])) > 0 else "none")