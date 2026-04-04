# Source: https://docs.aporia.com/monitors-and-alerts/prediction-drift.md

# Source: https://docs.aporia.com/v1/monitors/prediction-drift.md

# Prediction Drift

### Why Monitor Prediction Drift?

Prediction drift allows you to monitor a change in the distribution of the predicted label or value.

For example, a larger proportion of credit-worthy applications when your product was launched in a more affluent area. Your model still holds, but your business may be unprepared for this scenario.

### Comparison methods

For this monitor, the following comparison methods are available:

* [Anomaly detection](https://docs.aporia.com/v1/monitor-template#comparison-methods)
* [Compared to segment](https://docs.aporia.com/v1/monitor-template#comparison-methods)
* [Compared to training](https://docs.aporia.com/v1/monitor-template#comparison-methods)

### Customizing your monitor

Configuration may slightly vary depending on the baseline you choose.

#### STEP 1: choose the predictions you would like to monitor

You may select as many prediction fields as you want 😊

Note that the monitor will run on each selected field separately.

#### STEP 2: choose inspection period and baseline

For the predictions you chose in the previous step, the monitor will compare the inspection period distribution with the baseline distribution. An alert will raise if the monitor finds a drift between these two distributions.

#### STEP 3: calibrate thresholds

Use the monitor preview to help you choose the right threshold and make sure you have the amount of alerts that fits your needs.

The threshold for categorical predictions is different than the one for numeric predictions. Make sure to calibrate them both if relevant.

### How are drifts calculated?

For numeric predictions, Aporia detects drifts based on the [Jensen–Shannon](https://en.wikipedia.org/wiki/Jensen%E2%80%93Shannon_divergence) divergence metric. For categorical predictions, drifts are detected using [Hellinger distance](https://en.wikipedia.org/wiki/Hellinger_distance).

If you need to use other metrics, please contact us.
