#!/usr/bin/env python3
"""Module that concatenates two DataFrames with Timestamp as first level."""
import pandas as pd
index = __import__('10-index').index


def hierarchy(df1, df2):
    """Return bitstamp and coinbase rows grouped by Timestamp, in order."""
    df1 = index(df1).loc[1417411980:1417417980]
    df2 = index(df2).loc[1417411980:1417417980]
    df = pd.concat([df2, df1], keys=["bitstamp", "coinbase"])
    df = df.swaplevel(0, 1)
    return df.sort_index()
