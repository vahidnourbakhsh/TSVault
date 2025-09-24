# TSVault
![TSVault Logo](./docs/logo/logo-color-narrow.png)

[![Python Package using Conda](https://github.com/vahidnourbakhsh/TSVault/actions/workflows/python-app.yml/badge.svg)](https://github.com/vahidnourbakhsh/TSVault/actions/workflows/python-app.yml)

## About

**TSVault** is a comprehensive collection of tutorials, models, and utility functions for time series analysis. This repository provides practical implementations and educational resources for various time series forecasting techniques, uncertainty quantification, and advanced modeling approaches.

## Table of Contents

- [Utilities](#utilities)
- [Prediction Intervals](#prediction-intervals)
- [Natural Language Processing for Time Series](#natural-language-processing-for-time-series)
- [Data](#data)
- [Getting Started](#getting-started)

## Utilities

Essential utility functions for time series analysis are documented and demonstrated in:

- **`utilities/learn_utilities.ipynb`** - Interactive tutorial explaining key utility functions
- **`utilities/utilities.py`** - Collection of reusable functions for time series data handling and preprocessing

## Prediction Intervals

This section focuses on **uncertainty quantification** in time series forecasting. Prediction intervals provide crucial information about forecast reliability and risk assessment.

### 📚 Theory and Methods

**`prediction_intervals/prediction_uncertainty.md`** provides comprehensive coverage of:

- Parametric methods (assuming normal distribution of errors)
- Bootstrapping techniques for non-parametric approaches
- Quantile regression for robust uncertainty estimation
- Bayesian methods for full posterior distributions

### 💻 Practical Implementations

- **`parametric_method.ipynb`** - Implementation of parametric approaches using distributional assumptions
- **`bootrstrapping.ipynb`** - Bootstrap-based prediction intervals for robust uncertainty estimation
- **`quantile_regression.ipynb`** - Quantile regression methods for direct interval estimation

Each notebook includes:

- ✅ Step-by-step implementation
- ✅ Real-world examples with sample data
- ✅ Comparison of different approaches
- ✅ Visualization of prediction intervals

## Natural Language Processing for Time Series

**`natural_language_processing/ds_beach_demand_nlp.ipynb`** demonstrates how to incorporate NLP techniques into time series forecasting:

- **Multi-modal forecasting**: Combines historical sales data with item descriptions
- **Deep learning approach**: Uses neural networks to capture complex relationships between items
- **Semantic relationships**: Leverages item descriptions to understand product similarities and substitutions

This implementation builds upon the work by Dr. Jeff Heaton ([YouTube tutorial](https://youtu.be/zN3LlMOFqxM)) with modifications to integrate our tested utility functions and improved preprocessing pipelines.

## Data

The repository includes sample datasets for hands-on practice:

- **`data/beach_restaurant_demand_forecast/`** - Restaurant demand forecasting dataset with:
  - `items.csv` - Product catalog with descriptions
  - `restaurants.csv` - Restaurant information
  - `sales_train.csv` - Historical sales data

## Getting Started

### Prerequisites

Ensure you have Python 3.10+ and the required dependencies. Use the provided environment file:

```bash
conda env create -f environment.yml
conda activate tsvault
```

### Quick Start

1. Clone the repository
2. Set up the environment
3. Start with the utilities notebook to understand the core functions
4. Explore prediction intervals for uncertainty quantification
5. Try the NLP-enhanced forecasting for advanced applications

---

**Contributors**: This project is actively maintained and welcomes contributions for new time series methods and improvements.
