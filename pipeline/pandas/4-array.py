#!/usr/bin/env python3
"""Module that converts part of a DataFrame to a numpy.ndarray."""


def array(df):
    """Return the last 10 rows of High and Close as a numpy.ndarray."""
    return df[["High", "Close"]].tail(10).to_numpy()
