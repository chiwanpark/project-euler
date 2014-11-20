#!/usr/bin/env python
from collections import defaultdict
from operator import mul
from functools import reduce

def triangulars():
    n = 2
    while True:
        yield n * (n + 1) // 2
        n += 1

def factors(n):
    if n == 1: return defaultdict(lambda: 0)
    for i in range(2, n + 1):
        if n % i == 0:
            result = factors(n // i)
            result[i] += 1
            return result

for i in triangulars():
    if reduce(mul, map(lambda x: x + 1, factors(i).values())) >= 500:
        print(i)
        break
