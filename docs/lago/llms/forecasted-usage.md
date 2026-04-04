# Source: https://getlago.com/docs/guide/analytics/forecasted-usage.md

> ## Documentation Index
> Fetch the complete documentation index at: https://getlago.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# (Beta) Forecasted usage

## Overview

The Forecasted Usage feature leverages machine learning to predict future usage. This helps you anticipate customer usage patterns and do revenue forecasting with confidence.

The forecasting system uses a machine learning pipeline that trains multiple models on historical usage data and generates probabilistic predictions for future periods.

<Frame caption="Forecasted usage dashboard">
  <img src="https://mintcdn.com/lago-docs/7U6qGW2huMnU4aEA/guide/analytics/images/forecasted-usage.png?fit=max&auto=format&n=7U6qGW2huMnU4aEA&q=85&s=e1bf64aec1297d4bd815d35f552360ab" data-og-width="3266" width="3266" data-og-height="1596" height="1596" data-path="guide/analytics/images/forecasted-usage.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lago-docs/7U6qGW2huMnU4aEA/guide/analytics/images/forecasted-usage.png?w=280&fit=max&auto=format&n=7U6qGW2huMnU4aEA&q=85&s=2fae69631146de4cb9141f5b1be62c7f 280w, https://mintcdn.com/lago-docs/7U6qGW2huMnU4aEA/guide/analytics/images/forecasted-usage.png?w=560&fit=max&auto=format&n=7U6qGW2huMnU4aEA&q=85&s=aab18cfcf3bd2ede312bd3e452e9a749 560w, https://mintcdn.com/lago-docs/7U6qGW2huMnU4aEA/guide/analytics/images/forecasted-usage.png?w=840&fit=max&auto=format&n=7U6qGW2huMnU4aEA&q=85&s=4dbf34ca6b9c37197ed689f2b904030e 840w, https://mintcdn.com/lago-docs/7U6qGW2huMnU4aEA/guide/analytics/images/forecasted-usage.png?w=1100&fit=max&auto=format&n=7U6qGW2huMnU4aEA&q=85&s=dcbad1da6393c357fe7317dde6580ee2 1100w, https://mintcdn.com/lago-docs/7U6qGW2huMnU4aEA/guide/analytics/images/forecasted-usage.png?w=1650&fit=max&auto=format&n=7U6qGW2huMnU4aEA&q=85&s=3d336704ce4dd3dfce49a0534d8df8c1 1650w, https://mintcdn.com/lago-docs/7U6qGW2huMnU4aEA/guide/analytics/images/forecasted-usage.png?w=2500&fit=max&auto=format&n=7U6qGW2huMnU4aEA&q=85&s=79e7207e549c852de4cf8066c96912a8 2500w" />
</Frame>

## How forecasting works

### Data-driven predictions

The ML pipeline uses historical usage data, grouped by billable metric, subscription, charge, and charge filter to identify patterns and trends and train ML models.

The target variable to forecast is future paid usage, as opposed to just invoiced usage which may or may not be eventually paid.

The model generates forecasts for 12 months ahead at monthly granularity.

As a rule of thumb, the forecasts are updated in the first 2 weeks of the month.

### Forecasting methods

The system supports two main forecasting approaches:

#### 1. Trained ML Models

Advanced machine learning models that learn from historical patterns, including:

* **LightGBM**: Gradient boosting model with quantile loss for probabilistic forecasting
* **N-BEATS**: Deep learning neural network specialized for time series
* **Ensemble**: Combines multiple models for improved accuracy

These models generate three forecast scenarios (conservative, realistic, and optimistic) based on different probability quantiles.

#### 2. Historical Mean

A simpler baseline method that uses historical average usage as the forecast. It is used whenever there is insufficient data to train ML models.

### Probabilistic forecasting

All trained model forecasts include three scenarios:

* **Conservative**: Lower-bound estimate for cautious planning
* **Realistic**: Median forecast representing the most likely outcome
* **Optimistic**: Upper-bound estimate for best-case scenarios

This probabilistic approach helps you understand the range of possible outcomes and plan accordingly.

### Subscription growth

We explicitly model the growth in the number of subscriptions using the historical data of your organization.

### Limitations

The models forecast the future usage amounts for a subset of all potential future revenue sources. For example, it doesn't explicitly account for new business products and features.
Recently created and unused/deleted billable metrics and charges can be excluded from the forecasts.

## Filtering options

Filter forecasted usage data by:

* Currency
* Customer country
* Customer external ID
* Customer type
* Customer has TaxID
* Plan code
* Subscription external ID
* Billable metric

<Info>
  **PREMIUM FEATURE** ✨

  Forecasted Usage and advanced filtering options are only available to users with a premium license. Please
  **[contact us](mailto:hello@getlago.com)** to get access to Lago Cloud and Lago
  Self-Hosted Premium.
</Info>
