#!/usr/bin/env python3
"""Module that sorts a DataFrame by the High price."""


def high(df):
    """Return df sorted by the High column in descending order."""
    return df.sort_values(by="High", ascending=False)
