import sys
import math


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    max_prime_factor = 1
    for i in range(1, int(math.sqrt(n))):
        if n % i == 0:
            max_prime_factor = i
