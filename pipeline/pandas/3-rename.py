#!/usr/bin/env python3
"""Module that renames and converts the Timestamp column of a DataFrame."""
import pandas as pd


def rename(df):
    """Rename Timestamp to Datetime, convert it, and keep Datetime, Close."""
    df = df.rename(columns={"Timestamp": "Datetime"})
    df["Datetime"] = pd.to_datetime(df["Datetime"], unit="s")
    return df[["Datetime", "Close"]]
