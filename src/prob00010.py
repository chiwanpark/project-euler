#!/usr/bin/env python
def primes():
    candidates = [2]
    p = 3

    while p <= 2000000:
        prime = True
        for candidate in candidates:
            if p % candidate == 0:
                prime = False
                break

        if prime:
            candidates.append(p)

        p += 2

    return candidates

print(sum(primes()))
