# Source: https://docs.startree.ai/thirdeye/operators/post-processor/anomaly_merger.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# ANOMALY_MERGER

Merges anomalies. See [anomaly merge](/thirdeye/concepts-data-alerts-notifications/concepts-anomaly-merger-rules).

## Inputs

The info source is the output of the detector. Anomalies of this output are merged.

```json  theme={null}
{
  "sourcePlanNode": "anomalyDetector"
}
```

## Parameters

| name                                    | description                                                                                                                                                                                                                                                                                                                               | default value |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `component.mergeMaxGap`                 | Maximum gap between 2 anomalies for the anomalies to be merged. In ISO-8601 format. To disable anomalies merging, set this value to `P0D`.                                                                                                                                                                                                | PT2H          |
| `component.mergeMaxDuration`            | Maximum duration of an anomaly merger. At merge time, if an anomaly merger would get bigger than this limit, the anomalies are not merged.                                                                                                                                                                                                | P7D           |
| `component.reNotifyPercentageThreshold` | For detection replay when data is mutable. If the percentage difference between an existing anomaly and a new anomaly on the same time frame is above this threshold, renotify. Combined with `reNotifyAbsoluteThreshold`. Both thresholds must pass to be re-notified. If zero, always renotify. If null or negative, never re-notifies. | -1            |
| `component.reNotifyAbsoluteThreshold`   | For detection replay when data is mutable. If the absolute difference between an existing anomaly and a new anomaly on the same time frame is above this threshold, renotify. Combined with `reNotifyPercentageThreshold`. Both thresholds must pass to be re-notified. If zero, always renotify. If null or negative, never re-notifies. | -1            |

## Example

```json  theme={null}
{
  "name": "root",
  "type": "PostProcessor",
  "params": {
    "type": "ANOMALY_MERGER",
    "component.mergeMaxGap": "PT1H",
    "component.mergeMaxDuration": "P3D"
  },
  "inputs": [
    {
      "sourcePlanNode": "anomalyDetector"
    }
  ]
}
```

[iso-8601](https://en.wikipedia.org/wiki/ISO_8601#Durations)

Built with [Mintlify](https://mintlify.com).
