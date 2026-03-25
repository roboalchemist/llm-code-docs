# Source: https://docs.startree.ai/thirdeye/operators/post-processor/detector.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# DETECTOR

<Info>
  Enterprise only
</Info>

Some detectors can be used as postProcessors. A label is added to main detector anomalies if they are not flagged as an anomaly by the postProcessor detector. By default, the postProcessor detector is applied to the metric that was used for the detection. This corresponds to an `AND` operation of 2 detectors. A different metric can also be provided by passing an input `current`. The detector will run on this input.

## Compatible detectors

* [OFFSET\_AGGREGATION](/thirdeye/operators/anomaly-detector/offset_aggregation)

## Inputs

The info source is the output of the detector. Labels are applied to the anomalies of this input.

```json  theme={null}
{
  "sourcePlanNode": "anomalyDetector"
}
```

*Optional*: A different side data input to run detection on:

```json  theme={null}
{
  "targetProperty": "current",
  "sourcePlanNode": "controlDataFetcher",
  "sourceProperty": "controlDataOutput"
}
```

## Parameters

All parameters of the anomaly detector can be used.

Additional parameters:

| name                  | description                                                                                                     | default value |
| --------------------- | --------------------------------------------------------------------------------------------------------------- | ------------- |
| `component.ignore`    | If true, anomalies that are not detected by the postProcessor detector will be filtered.                        | `false`       |
| `component.valueName` | Optional. The name of the metric. Used in the label: `"{ValueName} not anomalous according to <TYPE> detector"` | `Value`       |

## Examples

Without side input

```json  theme={null}
{
  "name": "root",
  "type": "PostProcessor",
  "params": {
    "type": "OFFSET_AGGREGATION",
    "component.ignore": "true",  # filter anomaly in notifications an ui by default,
    "component.valueName": "Business KPI", # customize label
    "component.offsets": ["P7D", "P14D"], # parameter of the detector
    ... 
    "component.aggregation": "MEDIAN" # parameter of the detector
  },
  "inputs": [
    {
      "sourcePlanNode": "anomalyDetector"
    }
  ]
}
```

With side input

```json  theme={null}
{
  "name": "root",
  "type": "PostProcessor",
  "params": {
    "type": "OFFSET_AGGREGATION",
    "component.ignore": "true",
    "component.valueName": "GuardRail KPI", # customize label,
    "component.timestamp": "ts",      # time column of the side input
    "component.metric": "sideMetric"  # column in the side input to run detector on
    "component.offsets": ["P7D", "P14D"], # parameter of the detector
    ... 
    "component.aggregation": "MEDIAN" # parameter of the detector
  },
  "inputs": [
    {
      "sourcePlanNode": "anomalyDetector"
    },
    {
      "targetProperty": "current",
      "sourcePlanNode": "controlDataFetcher",
      "sourceProperty": "controlDataOutput"
    }
  ]
}
```

Built with [Mintlify](https://mintlify.com).
