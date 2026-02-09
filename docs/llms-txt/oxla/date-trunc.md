# Source: https://docs.oxla.com/sql-reference/sql-functions/timestamp-functions/date-trunc.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# DATE_TRUNC

## Overview

The `DATE_TRUNC()` function truncates a timestamp, timestamp with time zone or interval value to the specified precision,
effectively rounding down the value to the start of the given time unit. The return type matches the input type.

## Syntax

The syntax for using the `DATE_TRUNC()` function is as follows:

<CodeGroup>
  ```sql Without time_zone theme={null}
  DATE_TRUNC(field, source)
  ```

  ```sql With time_zone theme={null}
  DATE_TRUNC(field, source, time_zone)
  ```
</CodeGroup>

## Parameters

* `field`: The unit of time used to truncate the `source` value. It accepts `text` inputs and is case-insensitive
* `source`: The value you want to truncate. It can be `INTERVAL`, `TIMESTAMP` or `TIMESTAMP WITH TIME ZONE`
* `time_zone` *(applicable for the second syntax option)*: The time zone for the operation. It accepts `text` input

## Fields

Below is a list of supported values to specify the fields param in `DATE_TRUNC()` syntax.

* `microseconds `
* `milliseconds`
* `second`
* `minute`
* `hour`
* `day`
* `week`
* `month`
* `quarter`
* `year`
* `decade`
* `century`
* `millennium`

<Note>
  Some fields like `microseconds` and `milliseconds` are supported only for interval types.
</Note>

## Examples

### Truncating to Year

This example truncates the timestamp to the year level.

```sql  theme={null}
select DATE_TRUNC('year', '1911-12-02 19:40:00'::timestamp);
```

The timestamp \*\*“1911-12-02 19:40:00” \*\*has been truncated to 1911, with the month and day set to January 1st.&#x20;

```sql  theme={null}
         date_trunc         
----------------------------
 1911-01-01 00:00:00.000000
```

### Truncating to Day

This query truncates the timestamp **"1911-12-02 19:40:00"** to the day level.

```sql  theme={null}
select DATE_TRUNC('day', '1911-12-02 19:40:00'::timestamp);
```

The timestamp has been truncated to the same day, year, month, and day components.&#x20;

```sql  theme={null}
        date_trunc         
----------------------------
 1911-12-02 00:00:00.000000
```

### Truncating to Week

This query truncates the timestamp **"1911-12-02 19:40:00"** to the week level.

```sql  theme={null}
select DATE_TRUNC('week', '1911-12-02 19:40:00'::timestamp);
```

The timestamp has been truncated to the start of the week containing the date, which is Monday, November 27, 1911, at 00:00:00.

```sql  theme={null}
        date_trunc         
----------------------------
 1911-11-27 00:00:00.000000
```

### Truncating to Quarter

This query truncates the timestamp **"1911-12-02 19:40:00"** to the quarter level.

```sql  theme={null}
select DATE_TRUNC('quarter', '1911-12-02 19:40:00'::timestamp);
```

The timestamp is truncated to the start of the quarter. The month and day are set to the first month and first day of the quarter,
with time components reset to zero.

```sql  theme={null}
        date_trunc         
----------------------------
 1911-10-01 00:00:00.000000
```

### Truncating to Hour

This query truncates the interval **"15 hours 10 minutes"** to the hour precision.

```sql  theme={null}
select DATE_TRUNC('hour', '15 hour 10 minutes'::interval);
```

The minutes and seconds components are set to zero, resulting in an interval of exactly 15 hours.

```sql  theme={null}
   date_trunc    
-----------------
 15:00:00.000000
```

### Truncating to Quarter (Interval)

This query truncates the interval **"16 years 4 months"** to the quarter-year level.

```sql  theme={null}
select DATE_TRUNC('quarter', '16 years 4 months'::interval);
```

The interval is truncated to the nearest quarter-year unit.
The months components is adjusted to the start of the quarter. Since each quarter consists of 3 months,
4 months is truncated down to 3 months, resulting in:

```sql  theme={null}
   date_trunc    
-----------------
 16 years 3 mons
```
