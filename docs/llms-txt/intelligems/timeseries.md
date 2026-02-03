# Source: https://docs.intelligems.io/analytics/experiment-analytics/timeseries.md

# Time Series

Intelligems provides time series for most metrics, allowing you to view how your experiment has performed on these metrics over time. There are two time series modes, cumulative and discrete. Cumulative is enabled by default, to activate discrete, you can uncheck the “Cumulative” checkbox:

## Cumulative

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-372a2dc7fb4ad835671f7f8529a51c04c9cc4707%2FTimeseries.png?alt=media" alt=""><figcaption></figcaption></figure>

With this mode active, the metrics shown in the time series are up to and including the time on the x-axis. For example, in cumulative mode, at X = Jan 1, 2025, the data on the y-axis would be up to and including activity through Jan 1, 2025. Another way of thinking about this is that it’s a snapshot of how the data would have looked at the end of the day on Jan 1, 2025. This can be useful to see how the value of the metric evolved over the course of the experiment

### Confidence Intervals

In cumulative mode, you can enable confidence intervals by checking off the “Confidence Intervals” checkbox. This will overlay 95% interval bands around each test group’s lines, allowing you to visualize how certainty of the metric evolved over the course of the experiment. If no confidence interval appears for a timeframe, there may not be enough data available to calculate confidence intervals.

## Discrete

With this mode active (i.e., with the “Cumulative” checkbox unchecked) the metrics shown are for only the time period on the X-axis. For example, with daily intervals, at X = Jan 1, 2025, the data on the y-axis would be for the day of Jan 1, 2025 only. This can be useful to see if experiment performance differed significantly during a specific period, for example during a sale.
