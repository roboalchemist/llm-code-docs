# Source: https://docs.startree.ai/thirdeye/operators/post-processor/impact.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# IMPACT

<Info>
  Enterprise only
</Info>

<Warning>
  Experimental
</Warning>

Adds an `IMPACT` label to an anomaly if the sum of the differences between predictions and observed values on a window containing the anomaly is less than a given threshold. Intuitively, it is the sum of impacts in the last n points.

## Inputs

The info source is the output of the detector. Labels are applied to the anomalies of this input.

```json  theme={null}
{
  "sourcePlanNode": "anomalyDetector"
}
```

## Parameters

| name                                | description                                                                                              | default value                       |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| `component.threshold`               | If the sum of anomalies impact is below this threshold, label the anomaly.                               | `-1` (special value - no threshold) |
| `component.window`                  | Window to compute the impact. In ISO-8601 format.                                                        |                                     |
| `component.impactComputationMethod` | Method to compute the impact. `STANDARD_AREA` or `ABSOLUTE_AREA`. See below.                             | `STANDARD_AREA`                     |
| `component.monitoringGranularity`   | Granularity of the timeseries in ISO-8601 format. Should be same value as in the detector configuration. |                                     |

### `impactComputationMethod`

* `STANDARD_AREA`\
  `impact = sum(actual-expected) on the window`
* `ABSOLUTE_AREA`\
  `impact = sum(abs(actual-expected)) on the window`

## Example

```json  theme={null}
{
  "name": "root",
  "type": "PostProcessor",
  "params": {
    "type": "IMPACT",
    "component.ignore": "true",
    "component.monitoringGranularity": "PT1H",
    "component.impactComputationMethod": "STANDARD_AREA",
    "component.window": "PT12H",
    # anomaly can be ignored if the sum of the impacts in the last 12 hours is less than 500
    "component.threshold": "500"
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
