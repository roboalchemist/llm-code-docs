# Source: https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/Duration.md.txt

# Duration

- [JSON representation](https://firebase.google.com/docs/test-lab/reference/toolresults/rest/v1beta3/Duration#SCHEMA_REPRESENTATION)

A Duration represents a signed, fixed-length span of time represented as a count of seconds and fractions of seconds at nanosecond resolution. It is independent of any calendar and concepts like "day" or "month". It is related to Timestamp in that the difference between two Timestamp values is a Duration and it can be added or subtracted from a Timestamp. Range is approximately +-10,000 years.

|               JSON representation               |
|-------------------------------------------------|
| ``` { "seconds": string, "nanos": integer } ``` |

|                                                                                                                                                                                               Fields                                                                                                                                                                                                ||
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `seconds` | `string (`[int64](https://developers.google.com/discovery/v1/type-format)` format)` Signed seconds of the span of time. Must be from -315,576,000,000 to +315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min \* 60 min/hr \* 24 hr/day \* 365.25 days/year \* 10000 years                                                                                       |
| `nanos`   | `integer` Signed fractions of a second at nanosecond resolution of the span of time. Durations less than one second are represented with a 0 `seconds` field and a positive or negative `nanos` field. For durations of one second or more, a non-zero value for the `nanos` field must be of the same sign as the `seconds` field. Must be from -999,999,999 to +999,999,999 inclusive. |