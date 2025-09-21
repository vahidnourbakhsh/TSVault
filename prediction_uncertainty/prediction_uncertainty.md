# Calculating prediction distribution in time series forecasting

Time series forecasting doesn't just involve predicting a single future value (a point forecast), but often also aims to quantify the uncertainty surrounding that prediction, usually expressed as a prediction interval or a complete prediction distribution.

Here are the key approaches to calculating prediction distributions and intervals in time series forecasting:

## 1. Parametric methods

These methods assume that the forecast errors (residuals) follow a specific probability distribution, most commonly a normal distribution.
With this assumption, a prediction interval can be constructed around the point forecast using the estimated standard deviation of the forecast errors and a multiplier based on the desired confidence level (e.g., 1.96 for a 95% interval).
While simple to calculate, the assumption of normality might not always hold in real-world time series data, according to OTexts.

## 2. Bootstrapping

This approach is useful when the normality assumption for residuals is inappropriate.
It involves simulating multiple future paths of the time series by repeatedly sampling from the historical residuals and adding them to the point forecasts.
The prediction intervals are then derived from the percentiles of these simulated paths (e.g., the 2.5th and 97.5th percentiles for a 95% interval).
Bootstrapping can be computationally intensive, especially for models requiring numerous iterations.

## 3. Quantile regression

Instead of estimating the conditional mean, quantile regression models directly estimate the conditional quantiles of the response variable.
By training separate models for different quantiles (e.g., the 0.1 and 0.9 quantiles), prediction intervals can be formed as the range between the corresponding quantile predictions.
This method is more robust to outliers and does not assume a specific distribution for the errors.
However, each quantile needs its own regressor, and the approach might not be suitable for all types of regression models.

## 4. Bayesian methods

Bayesian methods treat model parameters and future observations as random variables and provide a full posterior distribution for the predictions.
This approach naturally incorporates prior knowledge and updates beliefs as new data arrives, offering a comprehensive understanding of uncertainty.
Prediction intervals are derived from the posterior distribution of the predictions.
Bayesian methods can be computationally intensive, often requiring Markov Chain Monte Carlo (MCMC) sampling techniques.

## 5. Other considerations

- Model uncertainty: Prediction intervals often only account for the random error term, but uncertainty also arises from model selection and parameter estimation.
- Out-of-sample coverage: Forecast accuracy can be worse out-of-sample, so it's important to validate the empirical coverage of the prediction intervals.
- Transformations: If the data is transformed, the prediction intervals should be calculated on the transformed scale and then back-transformed to the original scale.

The choice of method depends on the specific characteristics of the time series, the assumptions that can be made about the error distribution, and the computational resources available.
