#!/usr/bin/env python3
"""Module that creates a pandas DataFrame from a numpy ndarray."""
import pandas as pd


def from_numpy(array):
    """Return a pd.DataFrame from array with columns labeled A, B, C..."""
    columns = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:array.shape[1]])
    return pd.DataFrame(array, columns=columns)
