#!/usr/bin/env python

def hailstone(n):
    count = 0
    while n > 1:
        if n % 2 == 0: n = n / 2
        else: n = 3 * n + 1
        count += 1
    return count

print(max(map(lambda x: (x, hailstone(x)), range(1, 1000000)), key=lambda x: x[1])[0])
