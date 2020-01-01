#!/bin/python3

import sys
import math

def lcm(a, b):
    return int(a * b / math.gcd(a, b))



t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    a = 1
    for i in range(2, n + 1):
        a = lcm(a, i)
    print(a)


