#!/usr/bin/env python3
"""Module that slices columns and rows of a DataFrame."""


def slice(df):
    """Return High, Low, Close and Volume_(BTC), taking every 60th row."""
    return df[["High", "Low", "Close", "Volume_(BTC)"]].iloc[::60]
