#!/usr/bin/env python3
"""Module that adds two 2D matrices element-wise."""


def add_matrices2D(mat1, mat2):
    """Return a new matrix with the element-wise sum of mat1 and mat2."""
    if len(mat1) != len(mat2):
        return None
    for row1, row2 in zip(mat1, mat2):
        if len(row1) != len(row2):
            return None
    return [[row1[j] + row2[j] for j in range(len(row1))]
            for row1, row2 in zip(mat1, mat2)]
