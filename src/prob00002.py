#!/usr/bin/env python
def fibo():
    a, b = 0, 1
    while b <= 4000000:
        a, b = b, a + b
        yield b

print(sum(filter(lambda x: x % 2 == 0, fibo())))
