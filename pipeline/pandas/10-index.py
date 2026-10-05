#!/usr/bin/env python3
"""Module that sets the Timestamp column as a DataFrame's index."""


def index(df):
    """Return df with the Timestamp column as its index."""
    return df.set_index("Timestamp")
