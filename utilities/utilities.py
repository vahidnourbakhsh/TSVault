"""Utility functions used for our time series data preparation.
"""
import pandas as pd
from typing import List


def series_to_supervised(
    data: pd.DataFrame,
    groupby_cols: List[str],
    value_cols: List[str],
    window=1,
    lag=1,
    dropnan=True,
) -> pd.DataFrame():
    """Use history according to `window` size to predict the future specified in `lag`.
    The output is a wide-format dataframe. This method creates (1, ..., window) features for each of the columns in `data`.

    Args:
        data (pd.DataFrame): Input dataframe
        groupby_cols (List[str]): columns that are grouped. For example, if you are predicting demand for each (store, item), both store and item would be grouped_cols.
        value_cols (List[str]): Columns used for prediction, meaning we look at the history of these columns according to `window` size.
        window (int, optional): History window we would want to use for prediction (applies to `value_cols`). Defaults to 1.
        lag (int, optional): Future period we want to predict (applies to `value_cols`). Defaults to 1.
        dropnan (bool, optional): When we shift `val_cols` some values would be Null, by default the functions removes these records. Defaults to True.

    Returns:
        pd.DataFrame(): a wide-format dataframe which includes all `val_cols` that are shifted according to `window`.
    """
    cols = list()

    # Current time step (t=0)
    new_names = {name: f"{name}(t)" for name in value_cols}
    cols.append(data.rename(columns=new_names))

    # Input sequence (t-n, ... t-1)
    for i in range(window, 0, -1):
        new_names = {name: f"{name}(t-{i})" for name in value_cols}
        cols.append(
            data.groupby(groupby_cols)[value_cols].shift(i).rename(columns=new_names)
        )

    # Target time step (t=lag)
    new_names = {name: f"{name}(t+{lag})" for name in value_cols}
    cols.append(
        data.groupby(groupby_cols)[value_cols].shift(-lag).rename(columns=new_names)
    )
    # Put it all together
    agg = pd.concat(cols, axis=1)
    # Drop rows with NaN values
    if dropnan:
        agg.dropna(inplace=True)
    return agg
