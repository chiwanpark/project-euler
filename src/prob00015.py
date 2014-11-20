#!/usr/bin/env python
from operator import mul

print(reduce(mul, range(1, 41)) // reduce(mul, range(1, 21)) ** 2)
