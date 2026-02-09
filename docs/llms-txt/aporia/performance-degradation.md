# Source: https://docs.aporia.com/monitors-and-alerts/performance-degradation.md

# Source: https://docs.aporia.com/v1/monitors/performance-degradation.md

# Performance Degradation

### Why Monitor Performance Degradation?

ML models performance often unexpectedly degrade when they are deployed in real-world domains. It is very important to track the true model performance metrics from real-world data and react in time, to avoid the consequences of poor model performance.

Causes of model's performance degradation include:

* Input data changes (various reasons)
* Concept drift

### Comparison methods

For this monitor, the following comparison methods are available:

* [Change in percentage](https://docs.aporia.com/v1/monitor-template#comparison-methods)
* [Absolute value](https://docs.aporia.com/v1/monitor-template#comparison-methods)
* [Anomaly detection](https://docs.aporia.com/v1/monitor-template#comparison-methods)
* [Compared to segment](https://docs.aporia.com/v1/monitor-template#comparison-methods)
* [Compared to training](https://docs.aporia.com/v1/monitor-template#comparison-methods)

### Customizing your monitor

Configuration may slightly vary depending on the comparison method you choose.

#### STEP 1: choose the predictions & metrics you would like to monitor

You may select as many prediction fields as you want 😊 the monitor will run on each selected field separately.

Our performance degradation monitor supports a large variety of metrics that can measure the performance of your model's predictions given their corresponding actuals. You can check the full list of metric supported by Aporia in our [glossary](https://docs.aporia.com/v1/api-reference/metrics-glossary).

#### STEP 2: choose inspection period and baseline

For the fields you chose in the previous step, the monitor will raise an alert if the comparison between the inspection period and the baseline leads to a conclusion outside your threshold boundaries.

#### STEP 3: calibrate thresholds

This step is important to make sure you have the right amount of alerts that fits your needs. For anomaly detection method, use the monitor preview to help you decide what is the appropriate sensitivity level.
