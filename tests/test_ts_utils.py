"""Test utility functions used for our time series data preparation.
"""
import pandas as pd
from datetime import date

from utilities import series_to_supervised


def test_series_to_supervised():
    df = pd.DataFrame({"store": [1, 1, 1, 2, 2, 2],
    "date": [date(2022, 1, 1), date(2022, 1, 2), date(2022, 1, 3), date(2022, 1, 10), date(2022, 1, 11), date(2022, 1, 12)],
    "sales": [100, 150, 200, 110, 165, 220]})
    df2 = series_to_supervised(df, groupby_cols=["store"], value_cols=["sales"], window=1, lag=1, dropnan=True)
    assert len(df2) == 2
    assert all(df2.iloc[0].values == [1, date(2022, 1, 2), 150, 100.0, 200.0])
    assert all(df2.iloc[1].values == [2, date(2022, 1, 11), 165, 110.0, 220.0])


def test_series_to_supervised_2():
    df = pd.DataFrame({"store": [1, 1, 1, 1, 2, 2, 2, 2],
    "date": [date(2022, 1, 1), date(2022, 1, 2), date(2022, 1, 3), date(2022, 1, 4), date(2022, 1, 10), date(2022, 1, 11), date(2022, 1, 12), date(2022, 1, 13)],
    "sales": [100, 150, 200, 250, 110, 165, 220, 260]})
    df2 = series_to_supervised(df, groupby_cols=["store"], value_cols=["sales"], window=1, lag=1, dropnan=True)
    assert len(df2) == 4
    assert all(df2.iloc[0].values == [1, date(2022, 1, 2), 150, 100.0, 200.0])
    assert all(df2.iloc[1].values == [1, date(2022, 1, 3), 200, 150.0, 250.0])
    assert all(df2.iloc[2].values == [2, date(2022, 1, 11), 165, 110.0, 220.0])
    assert all(df2.iloc[3].values == [2, date(2022, 1, 12), 220, 165.0, 260.0])