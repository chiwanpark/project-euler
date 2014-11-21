#!/usr/bin/env python
from functools import reduce
from operator import mul, add

print(reduce(add, map(lambda x: int(x), str(reduce(mul, range(1, 101))))))
