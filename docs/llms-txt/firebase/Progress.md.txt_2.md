# Source: https://firebase.google.com/docs/firestore/reference/rest/v1beta1/Progress.md.txt

# Progress

Measures the progress of a particular metric.

| JSON representation ||
|---|---|
| ``` { "workCompleted": string, "workEstimated": string } ``` |

| Fields ||
|---|---|
| `workCompleted` | `string (https://developers.google.com/discovery/v1/type-format format)` An estimate of how much work has been completed. Note that this may be greater than `workEstimated`. |
| `workEstimated` | `string (https://developers.google.com/discovery/v1/type-format format)` An estimate of how much work needs to be performed. Zero if the work estimate is unavailable. May change as work progresses. |