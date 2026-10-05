#!/usr/bin/env python3
"""Module that sorts a DataFrame in reverse time order and transposes it."""


def flip_switch(df):
    """Return df sorted newest first by Timestamp, then transposed."""
    return df.sort_values(by="Timestamp", ascending=False).transpose()
