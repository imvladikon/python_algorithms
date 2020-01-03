
#Maximum_subarray_problem
#https://en.wikipedia.org/wiki/Maximum_subarray_problem

import numpy as np


def max_subarray(A):
    max_so_far = max_ending_here = 0
    for x in A:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far      = max(max_so_far, max_ending_here)
    return max_so_far


array = np.random.randint(-100,100,size=100000)
print(max_subarray(array))

