# Source: https://docs.aporia.com/v1/monitors/monitor-template.md

# Overview

By now, you probably understand why monitoring your model is essential to keeping it healthy and up-to-date in production.

In the following section, you will learn how to setup relevant monitors for your model and customize them for your needs.

If this is your first time creating a monitor in Aporia, feel free to quickly go over the following basic monitoring concepts.

### Monitor types

In general, monitors can be divided into four sections of interest:

* **Integrity** - credible data is basic to maintaining a successful model. Monitoring the appearance of new values, amount of missing ones and that all values are within a reasonable range can help you assure that and detect problems early.
* **Performance** - depending on your use-case and KPIs, you can use different performance metric to assess how productive your model is and decide when it's best to retrain it.
* **Drift** - drift of features or predictions can result in model performance degradation. Monitoring them both is useful to notice such trends early and take the proper action before it affects your business.
* **Activity** - it's great to know that after all your hard work your model is out there making real world decisions. Monitoring your activity can help you reflect that to others and notice any surprising changes in volume that needs further investigation

### Comparison methods

Aporia provides you with several comparison methods:

* **Absolute values** - thresholds or boundaries are defined by specific absolute values. The inspection data is a serving data segment of your choice.
* **Change in percentage** - thresholds or boundaries are defined by a change in percentage compared to baseline. Both baseline and inspection data are of the same serving data segment.
* **Anomaly detection** - detects anomalies in pattern compared to the baseline. Both baseline and inspection data are of the same serving data segment.
* **Compared to segment** - thresholds or boundaries are defined by a change in percentage compared to baseline. Inspection data and baseline data can be of deferent serving data segments.
* **Compared to training** - thresholds or boundaries are defined by a change in percentage compared to baseline. Baseline data includes all the training data reported, filtered by the same data segment as the inspection data's.

### It's time to create your own monitor! 🎬
