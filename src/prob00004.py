#!/usr/bin/env python

def candidates():
    for i in range(100, 1000):
        for j in range(100, 1000):
            yield i * j

print(max(filter(lambda x: str(x) == reversed(str(x)), candidates())))
