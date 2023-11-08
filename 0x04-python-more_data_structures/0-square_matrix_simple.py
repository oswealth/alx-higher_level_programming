#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for j in matrix:
        j = list(map(lambda x: x * x, j))
        new.append(j)
    return new
