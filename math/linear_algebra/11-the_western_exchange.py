#!/usr/bin/env python3
"""Module that transposes a numpy.ndarray."""
import numpy as np


def np_transpose(matrix):
    """Return a new numpy.ndarray that is the transpose of matrix."""
    return np.transpose(matrix).copy()
