#!/bin/python3

import sys
import operator
from functools import reduce

def prod(iterable):
    return reduce(operator.mul, iterable, 1)

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()[:n]
    count = 1+(len(num)-k) if len(num)>=k else 0
    max_prod = 0
    for i, c in enumerate(num):
        count -= 1
        p = prod(map(lambda c: int(c), num[i:i+k]))
        if p > max_prod:
            max_prod = p
        if count == 0:
            break
    print(max_prod)



