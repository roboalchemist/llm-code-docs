# Source: https://firebase.google.com/docs/reference/remote-config/rest/v1/ExperimentVariant.md.txt

# ExperimentVariant

Experiment variant.

| JSON representation |
|---|
| ``` { "name": string, "weight": integer } ``` |

| Fields ||
|---|---|
| `name` | `string` Identifier. The name of the variant. Eg: "Notification A", "Control". Variant names must be unique for a single experiment. |
| `weight` | `integer` Action weight proportional to other Actions. This number should be a whole number in the range \[1-100\] inclusive. If a weight is not specified, this value will be treated as 1. Example: if Action 1 has a weight of 1 and Action 2 has a weight of 2, Action 2 is twice as likely to be assigned to an instance. |