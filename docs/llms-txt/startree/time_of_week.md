# Source: https://docs.startree.ai/thirdeye/operators/post-processor/time_of_week.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# TIME_OF_WEEK

Adds a `TIME_OF_WEEK` label to anomalies that happen during a specific time of the week. For instance, can be used to filter anomalies that happen on Saturday.

## Inputs

The info source is the output of the detector. Labels are applied to the anomalies of this input.

```json  theme={null}
{
  "sourcePlanNode": "anomalyDetector"
}
```

## Parameters

| name                       | description                                                                             | default value   |
| -------------------------- | --------------------------------------------------------------------------------------- | --------------- |
| `component.daysOfWeek`     | A list of days to match. Eg `["MONDAY", "SATURDAY"]`.                                   | `[]` (no match) |
| `component.hoursOfDay`     | A list of hours to match. Eg `[0,1,2,23]`                                               | `[]` (no match) |
| `component.dayHoursOfWeek` | A map of `<day, List<hour>>` to match. Eg `{"FRIDAY": [22, 23], "SATURDAY": [0, 1, 2]}` | `{}` (no match) |

To determine days, the timezone defined in [metadata\$timezone](/thirdeye/alert-configuration#timezone) is used.

## Example

```json  theme={null}
{
  "name": "root",
  "type": "PostProcessor",
  "params": {
    "type": "TIME_OF_WEEK",
    "component.ignore": "true",
    "component.daysOfWeek": ["MONDAY", "SATURDAY"],
    "component.hoursOfDay": [0,1,2,23],
    "component.dayHoursOfWeek": {"FRIDAY": [22, 23], "SATURDAY": [0, 1, 2]}
  },
  "inputs": [
    {
      "sourcePlanNode": "anomalyDetector"
    }
  ]
}
```

Built with [Mintlify](https://mintlify.com).
