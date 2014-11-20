#!/usr/bin/env python
from math import sqrt

def prime():
    yield 2
    count = 2
    p = 3
    while count < 10002:
        if len(list(filter(lambda x: p % x == 0, range(2, int(sqrt(p) + 1))))) == 0:
            yield p
            count += 1
        p += 2

print(max(prime()))
