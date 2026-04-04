# Source: https://docs.aporia.com/monitors-and-alerts/missing-values.md

# Source: https://docs.aporia.com/v1/monitors/missing-values.md

# Missing Values

### Why Monitor Missing Values?

In real world data, there are often cases where a particular data element is missing. It is important to monitor the changes in missing values in order to spot and handle cases in which the model has not been trained to deal with.

Causes of missing values include:

* Serving environment fault
* Data store / provider schema changes
* Changes in internal API
* Changes in model subject input

### Comparison methods

For this monitor, the following comparison methods are available:

* [Change in percentage](https://docs.aporia.com/v1/monitor-template#comparison-methods)
* [Absolute value](https://docs.aporia.com/v1/monitor-template#comparison-methods)
* [Anomaly detection](https://docs.aporia.com/v1/monitor-template#comparison-methods)
* [Compared to segment](https://docs.aporia.com/v1/monitor-template#comparison-methods)

### Customizing your monitor

Configuration may slightly vary depending on the comparison method you choose.

#### STEP 1: choose the fields you would like to monitor

You may select as many fields as you want (from features/raw inputs) 😊

Note that the monitor will run on each selected field separately.

#### STEP 2: choose inspection period and baseline

For the fields you chose in the previous step, the monitor will raise an alert if the comparison between the inspection period and the baseline leads to a conclusion outside your threshold boundaries.

#### STEP 3: calibrate thresholds

This step is important to make sure you have the right amount of alerts that fits your needs. For anomaly detection method, use the monitor preview to help you decide what is the appropriate sensitivity level.
