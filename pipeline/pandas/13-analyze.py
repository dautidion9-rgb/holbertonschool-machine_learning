#!/usr/bin/env python3
"""Module that computes descriptive statistics for a DataFrame."""


def analyze(df):
    """Return descriptive statistics for all columns except Timestamp."""
    return df.drop(columns=["Timestamp"]).describe()
