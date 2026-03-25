# Source: https://docs.startree.ai/thirdeye/concepts-data-alerts-notifications/concepts-anomaly-merger-rules.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Anomaly Merger Rules

Consider an alert that runs with hourly granularity and an incident that last 3 hours. The alert will detect an anomaly 3 times, but it is actually the same incident. ThirdEye merges the anomalies in a single one.

By default, the following rules are applied:

1. consecutive anomalies are merged
2. if an anomaly lasts for more than 7 days, a new anomaly is created

## Examples

### Anomaly merge

1. Default behavior
   <img src="https://mintcdn.com/startree/zMiJ17Ik7Xto2JoM/img/thirdeye/_merge_anomalies_default.png?fit=max&auto=format&n=zMiJ17Ik7Xto2JoM&q=85&s=f40c58d511f153498aac0d231f0aa672" alt="merging anomalies" width="2822" height="718" data-path="img/thirdeye/_merge_anomalies_default.png" />
2. Custom behavior\
   You can configure ThirdEye to merge anomalies that have a small gap between them using [mergeMaxGap](/thirdeye/templates/startree-threshold#anomaly-merger).\
   For instance, with `mergeMaxGap=PT2H`, anomalies that have less than 2 hours between them are merged together.
   <img src="https://mintcdn.com/startree/zMiJ17Ik7Xto2JoM/img/thirdeye/_merge_anomalies_custom.png?fit=max&auto=format&n=zMiJ17Ik7Xto2JoM&q=85&s=615dae25f5cb9bd1195f0ba26b7df96b" alt="custom merging anomalies" width="1411" height="355" data-path="img/thirdeye/_merge_anomalies_custom.png" />
3. Disable anomaly merger\
   You can disable anomaly merger by setting `mergeMaxGap=PT0S`.
   <img src="https://mintcdn.com/startree/zMiJ17Ik7Xto2JoM/img/thirdeye/_merge_anomalies_disabled.png?fit=max&auto=format&n=zMiJ17Ik7Xto2JoM&q=85&s=0c57f27f043f0ce11312c6811eb95ec3" alt="anomaly merger disabled" width="2824" height="723" data-path="img/thirdeye/_merge_anomalies_disabled.png" />

### Anomaly max length

A new anomaly is created when the maximum length is reached. You can customize this maximum length with [mergeMaxDuration](/thirdeye/templates/startree-threshold#anomaly-merger).
<img src="https://mintcdn.com/startree/zMiJ17Ik7Xto2JoM/img/thirdeye/_merge_max_length.png?fit=max&auto=format&n=zMiJ17Ik7Xto2JoM&q=85&s=5ae217cef9e62da3f58647c985bcbfc4" alt="merging maximum" width="1410" height="339" data-path="img/thirdeye/_merge_max_length.png" />

Built with [Mintlify](https://mintlify.com).
