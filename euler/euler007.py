#!/bin/python3

import sys
import math


# https://www.hackerrank.com/contests/projecteuler/challenges/euler007/problem

def is_prime(n):
    """
    >>> is_prime(2)
    True
    >>> is_prime(19)
    True
    >>> is_prime(200)
    False
    """
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def prime_range(n):
    """
    >>> [i for i in prime_range(10)]
    [1, 2, 3, 5, 7, 11, 13, 17, 19, 23]
    >>> [i for i in prime_range(0)]
    []
    >>> [i for i in prime_range(1)]
    [1]
    """
    k = n
    for i in [1, 2]:
        if k == 0:
            break
        k -= 1
        yield i
    number = 3
    while k > 0:
        if is_prime(number):
            yield number
            k -= 1
        number += 2


def main():
    t = int(input().strip())
    data = [int(input().strip()) for a0 in range(t)]
    primes = [i for i in prime_range(max(data) + 1)]
    for n in data:
        print(primes[n - 1])

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    # main()
