# Source: https://docs.aporia.com/monitors-and-alerts/metric-change.md

# Source: https://docs.aporia.com/v1/monitors/metric-change.md

# Source: https://docs.aporia.com/monitors-and-alerts/metric-change.md

# Source: https://docs.aporia.com/v1/monitors/metric-change.md

# Metric Change

### Why Monitor Metric Change

Monitoring and measuring changes in features / raw inputs metrics allows for early detection of basic problems or changes in the model's input data.

For example - we can monitor and detect a deviation of more than 20% from the average of the feature 'age' from the average the monitor was trained with.

### Comparison methods

For this monitor, the following comparison methods are available:

* [Change in percentage](https://docs.aporia.com/v1/monitor-template#comparison-methods)
* [Absolute value](https://docs.aporia.com/v1/monitor-template#comparison-methods)
* [Anomaly detection](https://docs.aporia.com/v1/monitor-template#comparison-methods)
* [Compared to segment](https://docs.aporia.com/v1/monitor-template#comparison-methods)
* [Compared to training](https://docs.aporia.com/v1/monitor-template#comparison-methods)

### Customizing your monitor

Configuration may slightly vary depending on the comparison method you choose.

#### STEP 1: choose the metrics you would like to monitor

You may select as many prediction fields as you want (from raw inputs / features) 😊 the monitor will run on each selected field separately.

Our metric change monitor supports the following metrics:

* Missing count
* Average
* Minimum
* Maximum
* Sum
* Variance
* STD

#### STEP 2: choose inspection period and baseline

For the fields you chose in the previous step, the monitor will raise an alert if the comparison between the inspection period and the baseline leads to a conclusion outside your threshold boundaries.

#### STEP 3: calibrate thresholds

This step is important to make sure you have the right amount of alerts that fits your needs. For anomaly detection method, use the monitor preview to help you decide what is the appropriate sensitivity level.
