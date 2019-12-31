import sys
import numpy as np


class FloydWarshall(object):
    max_weight = sys.maxsize
    matrix = [[]]

    def set_max_weight(self, value):
        self.max_weight = value

    def get_max_weight(self):
        return self.max_weight

    def __init__(self, matrix, max_weight):
        self.max_weight = max_weight
        self.matrix = matrix

    def find(self):
        m = self.matrix
        n = len(m[0])
        for k in range(n):
            for i in range(n):
                for j in range(i):
                    m[j, i] = min([m[i, j], m[i, k] + m[k, j]])
                    m[i, j] = m[j, i]
        return m

    def build_matrix(self, nodes, array_from, array_to, array_weight):
        matrix = self.max_weight * \
                 np.full((nodes, nodes), self.max_weight, dtype=int)
        for idx in range(nodes):
            matrix[idx, idx] = 0
        length = len(array_weight)
        for idx in range(length):
            i = array_from[idx] - 1
            j = array_to[idx] - 1
            matrix[i, j] = array_weight[idx]
            matrix[j, i] = array_weight[idx]
        return matrix
