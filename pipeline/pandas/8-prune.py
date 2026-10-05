#!/usr/bin/env python3
"""Module that removes rows with missing Close values from a DataFrame."""


def prune(df):
    """Return df without the rows where Close is NaN."""
    return df.dropna(subset=["Close"])
