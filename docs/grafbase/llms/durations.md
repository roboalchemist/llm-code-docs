# Source: https://grafbase.com/docs/gateway/configuration/durations.md

# Durations

Many values in the configuration represent a duration. The format used in the Grafbase Gateway is inherited from the [duration_str](https://docs.rs/duration-str/0.12.0/duration_str/) crate.

The duration strings are composed of a number followed by a unit. The supported units are:

- y:Year. Support string value: [“y” | “year” | “Y” | “YEAR” | “Year”]. e.g. 1y
- mon:Month.Support string value: [“mon” | “MON” | “Month” | “month” | “MONTH”]. e.g. 1mon
- w:Week.Support string value: [“w” | “W” | “Week” | “WEEK” | “week”]. e.g. 1w
- d:Day.Support string value: [“d” | “D” | “Day” | “DAY” | “day”]. e.g. 1d
- h:Hour.Support string value: [“h” | “H” | “hr” | “Hour” | “HOUR” | “hour”]. e.g. 1h
- m:Minute.Support string value: [“m” | “M” | “Minute” | “MINUTE” | “minute” | “min” | “MIN”]. e.g. 1m
- s:Second.Support string value: [“s” | “S” | “Second” | “SECOND” | “second” | “sec” | “SEC”]. e.g. 1s
- ms:Millisecond.Support string value: [“ms” | “MS” | “Millisecond” | “MilliSecond” | “MILLISECOND” | “millisecond” | “mSEC” ]. e.g. 1ms
- µs:Microsecond.Support string value: [“µs” | “µS” | “µsecond” | “us” | “uS” | “usecond” | “Microsecond” | “MicroSecond” | “MICROSECOND” | “microsecond” | “µSEC”]. e.g. 1µs
- ns:Nanosecond.Support string value: [“ns” | “NS” | “Nanosecond” | “NanoSecond” | “NANOSECOND” | “nanosecond” | “nSEC”]. e.g. 1ns

This list is taken from the [duration_str docs](https://docs.rs/duration-str/0.12.0/duration_str/).

## Examples

- "1s": one second.
- "200.5ms": 200.5 milliseconds.
- "5d": 5 days.