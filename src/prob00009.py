#!/usr/bin/env python
from functools import reduce

def candidates():
    for i in range(1, 1001):
        for j in range(i + 1, 1001 - i):
            yield (i, j, 1000 - i - j)

print(reduce(lambda x, y: x * y, list(filter(lambda x: x[0] ** 2 + x[1] ** 2 == x[2] ** 2, candidates()))[0]))
