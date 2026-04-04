# Source: https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/PerfSample.md.txt

# PerfSample

- [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/PerfSample#SCHEMA_REPRESENTATION)

Resource representing a single performance measure or data point

|                                                              JSON representation                                                               |
|------------------------------------------------------------------------------------------------------------------------------------------------|
| ``` { "sampleTime": { object (https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/Timestamp) }, "value": number } ``` |

|                                                                         Fields                                                                          ||
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| `sampleTime` | `object (`[Timestamp](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/Timestamp)`)` Timestamp of collection. |
| `value`      | `number` Value observed                                                                                                                   |