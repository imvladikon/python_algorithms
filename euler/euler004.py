#!/bin/python3

import sys
from collections import defaultdict

t = int(input().strip())
palindromes = defaultdict(bool)
palindromes[101101] = True
palindromes[999 * 999] = True
for i in range(100, 999):
    for j in range(100_000 // i + 1, 999):
        number = i * j
        # it's not good to use number to str conversion
        # but it's kinda readable ;)
        string = str(number)
        if not len(string) == 6:
            continue
        if string[::-1] == string:
            palindromes[number] = True

for a0 in range(t):
    n = int(input().strip())
    for i in range(n - 1, 101100, -1):
        if palindromes.get(i):
            print(i)
            break

