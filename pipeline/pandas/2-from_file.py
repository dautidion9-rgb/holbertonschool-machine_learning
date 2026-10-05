#!/usr/bin/env python3
"""Module that loads data from a file as a pandas DataFrame."""
import pandas as pd


def from_file(filename, delimiter):
    """Return a pd.DataFrame loaded from filename using delimiter."""
    return pd.read_csv(filename, delimiter=delimiter)
