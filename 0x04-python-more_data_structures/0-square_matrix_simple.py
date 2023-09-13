#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    result = []
    for i in matrix:
        new = []
        for j in i:
            new.append(j ** 2)
        result.append(new)
    return result
