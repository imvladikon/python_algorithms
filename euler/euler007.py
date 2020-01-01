#!/bin/python3

import sys
import math

#https://www.hackerrank.com/contests/projecteuler/challenges/euler007/problem

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_range(n):
    k = n
    yield 2
    k -= 1
    number = 3
    while k>0:
        if is_prime(number):
            yield number
            k -= 1
        number += 2

t = int(input().strip())
data = [int(input().strip()) for a0 in range(t)]
primes = [i for i in prime_range(max(data)+1)]
for n in data:
    print(primes[n-1])





