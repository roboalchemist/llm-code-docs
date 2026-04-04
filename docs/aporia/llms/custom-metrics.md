# Source: https://docs.aporia.com/ml-monitoring-as-code/custom-metrics.md

# Source: https://docs.aporia.com/monitors-and-alerts/custom-metrics.md

# Source: https://docs.aporia.com/v1/monitors/custom-metrics.md

# Custom Metric

In case the monitoring metrics provided by Aporia are insufficient for your use-case, you can define your own custom metric using our custom metric definition language.

### Comparison methods

For this monitor, the following comparison methods are available:

* [Change in percentage](https://docs.aporia.com/v1/monitor-template#comparison-methods)
* [Absolute value](https://docs.aporia.com/v1/monitor-template#comparison-methods)
* [Anomaly detection](https://docs.aporia.com/v1/monitor-template#comparison-methods)

### Customizing your monitor

Configuration may slightly vary depending on the comparison method you choose.

#### STEP 1: choose the metrics you would like to monitor

You can either choose a custom metric you have previously defined or create a new one.

If this is your first time creating a custom metric in Aporia, you can read about our custom metric definition language [here](https://docs.aporia.com/v1/api-reference/custom-metric-definition-language).

#### STEP 2: choose inspection period and baseline

For the fields you chose in the previous step, the monitor will raise an alert if the comparison between the inspection period and the baseline leads to a conclusion outside your threshold boundaries.

#### STEP 3: calibrate thresholds

This step is important to make sure you have the right amount of alerts that fits your needs. For anomaly detection method, use the monitor preview to help you decide what is the appropriate sensitivity level.
