# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/todatetime.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/todatetime.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/todatetime.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/todatetime.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/todatetime.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/todatetime.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/todatetime.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/todatetime.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/todatetime.md

# Source: https://docs.pinot.apache.org/functions-1/todatetime.md

# ToDateTime

Converts from milliseconds to a formatted date-time string, based on the provided [Joda-Time pattern](https://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html).

## Signature

> ToDate(millis, pattern)&#x20;
>
> ToDate(millis, pattern, timezoneId)

## Usage Examples

```sql
SELECT ToDateTime(1639137263000, 'yyyy-MM-dd') AS dateTimeString
FROM ignoreMe
```

| dateTimeString |
| -------------- |
| 2021-12-10     |

```sql
SELECT ToDateTime(
    1639137263000, 
    'yyyy-MM-dd hh:mm:ss a'
    ) AS dateTimeString
FROM ignoreMe
```

| dateTimeString         |
| ---------------------- |
| 2021-12-10 11:54:23 AM |

```sql
SELECT ToDateTime(
    1639137263000, 
    'yyyy-MM-dd HH:mm:ss Z',
    'CET'
    ) AS dateTimeString
FROM ignoreMe
```

| dateTimeString            |
| ------------------------- |
| 2021-12-10 12:54:23 +0100 |
