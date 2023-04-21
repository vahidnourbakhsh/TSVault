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
    assert all(df2.iloc[0].values == [100.0, 1, date(2022, 1, 2), 150, 200.0])
    assert all(df2.iloc[1].values == [110.0, 2, date(2022, 1, 11), 165, 220.0])
