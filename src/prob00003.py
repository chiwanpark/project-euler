#!/usr/bin/env python
def factor():
    n = 600851475143
    p = 1
    while n > 1:
        p += 1
        if n % p != 0: continue
        while n % p == 0: n /= p
        yield p

print(max(factor()))
