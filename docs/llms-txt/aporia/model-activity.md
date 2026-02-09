# Source: https://docs.aporia.com/monitors-and-alerts/model-activity.md

# Source: https://docs.aporia.com/v1/monitors/model-activity.md

# Model Activity

### Why Monitor Model Activity?

In many cases, the number of model predictions is within a predictable range. Identifying deviations from the range can indicate on underlying problems, anomalous events, or an ongoing trend that is worth noting.

Causes of change in the number of predictions include:

* Natural increase in model invocations
* Serving environment fault
* Malicious attempt to analyze model behavior

### Comparison methods

For this monitor, the following comparison methods are available:

* [Change in percentage](https://docs.aporia.com/v1/monitor-template#comparison-methods)
* [Absolute value](https://docs.aporia.com/v1/monitor-template#comparison-methods)
* [Anomaly detection](https://docs.aporia.com/v1/monitor-template#comparison-methods)

### Customizing your monitor

Configuration may slightly vary depending on the comparison method you choose.

#### STEP 1: choose the predictions you would like to monitor

You may select as many prediction fields as you want 😊

Note that the monitor will run on each selected field separately.

#### STEP 2: choose inspection period and baseline

For the fields you chose in the previous step, the monitor will raise an alert if the amount of predictions in the inspection period exceeds your threshold boundaries compared to the baseline's amount of predictions.

#### STEP 3: calibrate thresholds

This step is important to make sure you have the right amount of alerts that fits your needs. For anomaly detection method, use the monitor preview to help you decide what is the appropriate sensitivity level.
