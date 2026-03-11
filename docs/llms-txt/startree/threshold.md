# Source: https://docs.startree.ai/thirdeye/operators/post-processor/threshold.md

# Source: https://docs.startree.ai/thirdeye/operators/anomaly-detector/threshold.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# THRESHOLD

Detects an anomaly if a metric is above a maximum threshold or below a minimum threshold.

## Inputs

`"targetProperty": "current"`: The data on which to perform detection.

## Parameters

| name            | description                                             | default value |
| --------------- | ------------------------------------------------------- | ------------- |
| `component.min` | If the metric goes below this value, detect an anomaly. | `-Inf`        |
| `component.max` | If the metric goes above this value, detect an anomaly. | `+Inf`        |

## Example

```json  theme={null}
{
  "name": "root",
  "type": "AnomalyDetector",
  "params": {
    "type": "THRESHOLD",
    "component.max": "75",
    "component.min": "10",
    ...  # shared parameters
  },
  "inputs": [
    {   # current data
      "targetProperty": "current",
      "sourcePlanNode": "currentData",
      "sourceProperty": "currentOutput"
    }
  ]
}
```

Built with [Mintlify](https://mintlify.com).
