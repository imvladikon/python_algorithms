#!/bin/python3

import sys

#for step = 1
def arithmetic_progression(a,b):
    return b*(a+b)/2

def square_sequence(n):
    return n*(n+1)*(2*n+1)/6

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sum_p = arithmetic_progression(1,n)
    print(int(sum_p*sum_p - square_sequence(n)))

