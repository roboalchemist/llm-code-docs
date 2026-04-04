# Source: https://docs.aporia.com/monitors-and-alerts/data-drift.md

# Source: https://docs.aporia.com/v1/monitors/data-drift.md

# Data Drift

### Why Monitor Data Drift?

Data drifts are one of the top reasons why model accuracy degrades over time. Data drift is a change in model input data that leads to model performance degradation. Monitoring data drift helps detect these model performance issues.

Causes of data drift include:

* **Upstream process changes**, such as a sensor being replaced that changes the units of measurement from inches to centimeters.
* **Data quality issues**, such as a broken sensor always reading 0.
* **Natural drift in the data**, such as mean temperature changing with the seasons.
* **Change in relation between features**, or covariant shift.

### Comparison methods

For this monitor, the following comparison methods are available:

* [Anomaly detection](https://docs.aporia.com/v1/monitor-template#comparison-methods)
* [Compared to segment](https://docs.aporia.com/v1/monitor-template#comparison-methods)
* [Compared to training](https://docs.aporia.com/v1/monitor-template#comparison-methods)

### Customizing your monitor

Configuration may slightly vary depending on the baseline you choose.

#### STEP 1: choose the fields you would like to monitor

You may select as many fields as you want 😊

Note that the monitor will run on each selected field separately.

#### STEP 2: choose inspection period and baseline

For the fields you chose in the previous step, the monitor will compare the inspection period distribution with the baseline distribution. An alert will raise if the monitor finds a drift between these two distributions.

#### STEP 3: calibrate thresholds

Use the monitor preview to help you choose the right threshold and make sure you have the amount of alerts that fits your needs.

The threshold for categorical fields is different then the one for numeric fields. Make sure to calibrate them both if relevant.

### How are drifts calculated?

For numeric fields, Aporia detects drifts based on the [Jensen–Shannon](https://en.wikipedia.org/wiki/Jensen%E2%80%93Shannon_divergence) divergence metric. For categorical fields, drifts are detected using [Hellinger distance](https://en.wikipedia.org/wiki/Hellinger_distance).

If you need to use other metrics, please contact us.
