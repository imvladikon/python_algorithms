#!/bin/python3

import sys

#arithmetic progression
def arith_prog(n, d):
    n = n - 1
    k = n // d
    return (d * k * (k + 1)) // 2

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(arith_prog(n, 3)+arith_prog(n, 5) - arith_prog(n, 3*5))

