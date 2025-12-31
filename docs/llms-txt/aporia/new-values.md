# Source: https://docs.aporia.com/monitors-and-alerts/new-values.md

# Source: https://docs.aporia.com/v1/monitors/new-values.md

# Source: https://docs.aporia.com/monitors-and-alerts/new-values.md

# Source: https://docs.aporia.com/v1/monitors/new-values.md

# New Values

### Why Monitor New Values?

Monitoring new values of **categorical fields** helps to locate and examine changes in the model's input.

For example, setting the monitor for a feature named `state` will help us discover a new region for which the model is asked to predict results.

### Comparison methods

For this monitor, the following comparison methods are available:

* [Change in percentage](https://docs.aporia.com/v1/monitor-template#comparison-methods)
* [Compared to segment](https://docs.aporia.com/v1/monitor-template#comparison-methods)
* [Compared to training](https://docs.aporia.com/v1/monitor-template#comparison-methods)

### Customizing your monitor

Configuration may slightly vary depending on the comparison method you choose.

#### STEP 1: choose the fields you would like to monitor

You may select as many fields as you want (from features/raw inputs) 😊

Note that the monitor will run on each selected field separately.

#### STEP 2: choose inspection period and baseline

For the fields you chose in the previous step, the monitor will raise an alert if the amount of new values in the inspection period compared to the baseline's values exceeds your threshold.

#### STEP 3: calibrate thresholds

This step is important to make sure you have the right amount of alerts that fits your needs. You can always readjust it later if needed.
