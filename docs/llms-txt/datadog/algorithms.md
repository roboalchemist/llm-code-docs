# Source: https://docs.datadoghq.com/dashboards/functions/algorithms.md

---
title: Algorithms
description: >-
  Implement anomaly detection, outlier detection, and forecasting algorithms for
  metrics in Datadog dashboards.
breadcrumbs: Docs > Dashboards > Functions > Algorithms
---

# Algorithms

## Anomalies{% #anomalies %}

| Function      | Description                                                                                | Example                                                |
| ------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------ |
| `anomalies()` | Overlay a gray band on the metric showing the expected behavior of a series based on past. | `anomalies(<METRIC_NAME>{*}, '<ALGORITHM>', <BOUNDS>)` |

The `anomalies()` function has two parameters:

- `ALGORITHM`: Methodology used to detect anomalies.
- `BOUNDS`: Width of the gray band. `bounds` can be interpreted as the standard deviations for your algorithm; a value of 2 or 3 should be large enough to include most "normal" points.

**Note**: If you are using the agile or robust anomaly detection algorithms with weekly or daily seasonality, you can update your anomaly detection monitor to account for a local timezone using both the API and the UI.

Here's a two-minute video walkthrough:

**Seasonality**: By default, the `robust` and `agile` algorithms use [weekly seasonality](https://docs.datadoghq.com/monitors/types/anomaly/?s=anomaly%20algorithm#seasonality), which requires three weeks of historical data to compute the baseline.

See the [Anomaly Monitor](https://docs.datadoghq.com/monitors/types/anomaly/) page for more info.

## Outliers{% #outliers %}

| Function     | Description                | Example                                                                |
| ------------ | -------------------------- | ---------------------------------------------------------------------- |
| `outliers()` | Highlight outliers series. | `outliers(<METRIC_NAME>{*}, '<ALGORITHM>', <TOLERANCE>, <PERCENTAGE>)` |

The `outliers()` function has three parameters:

- `ALGORITHM`: The outliers algorithm to use.
- `TOLERANCE`: The tolerance of the outliers algorithm.
- `PERCENTAGE`: The percentage of outlying points required to mark a series as an outlier (available only for MAD and scaledMAD algorithms)

{% video
   url="https://datadog-docs.imgix.net/images/dashboards/functions/algorithms/outlier.mp4" /%}

See the [Outlier Monitor](https://docs.datadoghq.com/monitors/types/outlier/) page for more info.

## Forecast{% #forecast %}

| Function     | Description                                       | Example                                                   |
| ------------ | ------------------------------------------------- | --------------------------------------------------------- |
| `forecast()` | Predicts where a metric is heading in the future. | `forecast(<METRIC_NAME>{*}, '<ALGORITHM>', <DEVIATIONS>)` |

The `forecast()` function has two parameters:

- `ALGORITHM`: The forecasting algorithm to use - select `linear` or `seasonal`. For more information about these algorithms, see the [Forecast Algorithms](https://docs.datadoghq.com/monitors/types/forecasts/?tab=linear#algorithms) section.
- `DEVIATIONS`: The width of the range of forecasted values. A value of 1 or 2 should be large enough to forecast most "normal" points accurately.

## Other functions{% #other-functions %}

- [Arithmetic: Perform Arithmetic operation on your metric.](https://docs.datadoghq.com/dashboards/functions/arithmetic)
- [Count: Count non zero or non null value of your metric.](https://docs.datadoghq.com/dashboards/functions/count)
- [Exclusion: Exclude certain values of your metric.](https://docs.datadoghq.com/dashboards/functions/exclusion)
- [Interpolation: Fill or set default values for your metric.](https://docs.datadoghq.com/dashboards/functions/interpolation)
- [Rank: Select only a subset of metrics.](https://docs.datadoghq.com/dashboards/functions/rank)
- [Rate: Calculate custom derivative over your metric.](https://docs.datadoghq.com/dashboards/functions/rate)
- [Regression: Apply some machine learning function to your metric.](https://docs.datadoghq.com/dashboards/functions/regression)
- [Rollup: Control the number of raw points used in your metric.](https://docs.datadoghq.com/dashboards/functions/rollup)
- [Smoothing: Smooth your metric variations.](https://docs.datadoghq.com/dashboards/functions/smoothing)
- [Timeshift: Shift your metric data point along the timeline.](https://docs.datadoghq.com/dashboards/functions/timeshift)
