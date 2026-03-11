# Source: https://docs.startree.ai/thirdeye/operators/anomaly-detector/absolute.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# ABSOLUTE_CHANGE

Compares current time series to a baseline. If the absolute change is above a certain threshold, detect it as an anomaly.

## Inputs

`"targetProperty": "current"`: The data on which to perform detection.

`"targetProperty": "baseline"`: The data to use as a baseline.

The inputs should have the same size.

## Parameters

| name                       | description                                                                                                                     | default value |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `component.absoluteChange` | The absolute change threshold. If the absolute change when compared to the baseline is above this threshold, detect an anomaly. |               |
| `component.pattern`        | Detect as an anomaly if the metric drop, rise or both directions. `UP`, `DOWN`, `UP_OR_DOWN`.                                   | `UP_OR_DOWN`  |

## Example

```json  theme={null}
{
  "name": "root",
  "type": "AnomalyDetector",
  "params": {
    "type": "ABSOLUTE_CHANGE",
    "component.absoluteChange": "150",
    "component.offset": "DOWN",
    ...  # shared parameters
  }, 
  "inputs": [
    {    # baseline data
      "targetProperty": "baseline",               
      "sourcePlanNode": "baselineDataFetcher",
      "sourceProperty": "baselineOutput"
    },
    {    # current data
      "targetProperty": "current",                
      "sourcePlanNode": "currentDataFetcher",
      "sourceProperty": "currentOutput"
    }
  ]
}
```

Built with [Mintlify](https://mintlify.com).
