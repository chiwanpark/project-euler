#!/usr/bin/env python
from collections import defaultdict
from operator import mul, add
from functools import reduce

def factors(n):
    for i in range(2, n + 1):
        if n % i == 0:
            ret = factors(n // i)
            ret[i] += 1
            return ret
    return defaultdict(lambda: 0)

def d(n):
    if n == 1: return 0
    f = factors(n)
    return reduce(mul, map(lambda z: reduce(add, map(lambda x: z ** x, range(f[z] + 1))), f.keys())) - n

print(sum(filter(lambda x: x == d(d(x)) and x != d(x), range(2, 10001))))
