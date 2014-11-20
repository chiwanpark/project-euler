#!/usr/bin/env python
from functools import reduce

def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

print(reduce(lambda x, y: lcm(x, y), range(1, 21)))
