#!/usr/bin/env python3
"""Module that transposes a 2D matrix."""


def matrix_transpose(matrix):
    """Return a new matrix that is the transpose of a 2D matrix."""
    return [[matrix[i][j] for i in range(len(matrix))]
            for j in range(len(matrix[0]))]
