"""TSVault - A comprehensive collection of time series analysis tools and tutorials.

This package provides practical implementations and educational resources for
various time series forecasting techniques, uncertainty quantification, and
advanced modeling approaches.
"""

__version__ = "0.1.0"
__author__ = "TSVault Contributors"

from .utilities.utilities import series_to_supervised

__all__ = [
    "series_to_supervised",
]
