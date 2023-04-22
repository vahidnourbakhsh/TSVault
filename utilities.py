"""Utility functions used for our time series data preparation.
"""
import pandas as pd
from typing import List

def series_to_supervised(data: pd.DataFrame, groupby_cols: List[str], value_cols: List[str],
                         window=1, lag=1, dropnan=True):
    """Use history according to `window` size to predict the future specified in `lag`.
    The output is a wide-format dataframe. This method creates (1, ..., window) features for each of the columns in `data`.
    """
    cols = list()
    
    # Current time step (t=0)
    cols.append(data)
    
    # Input sequence (t-n, ... t-1)
    for i in range(window, 0, -1):
        new_names = {name: f"{name}(t-{i})" for name in value_cols}
        cols.append(data.groupby(groupby_cols)[value_cols].shift(i).rename(columns=new_names))
        
    # Target time step (t=lag)
    new_names = {name: f"{name}(t+{lag})" for name in value_cols}
    cols.append(data.groupby(groupby_cols)[value_cols].shift(-lag).rename(columns=new_names))
    # Put it all together
    agg = pd.concat(cols, axis=1)
    # Drop rows with NaN values
    if dropnan:
        agg.dropna(inplace=True)
    return agg