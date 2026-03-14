# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/fromdatetime.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/fromdatetime.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/fromdatetime.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/fromdatetime.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/fromdatetime.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/fromdatetime.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/fromdatetime.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/fromdatetime.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/fromdatetime.md

# Source: https://docs.pinot.apache.org/functions-1/fromdatetime.md

# FromDateTime

Converts a formatted date-time string to milliseconds, based on the provided [Joda-Time pattern](https://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html).

## Signature

> FromDateTime(dateTimeString, pattern)

## Usage Examples

```sql
SELECT FromDateTime('2019-08-07', 'yyyy-MM-dd') AS epochMillis
FROM ignoreMe
```

| epochMillis   |
| ------------- |
| 1565136000000 |

```sql
SELECT FromDateTime(
    '2019-08-07 3:12:13 PM', 
    'yyyy-MM-dd hh:mm:ss a'
    ) AS epochMillis
FROM ignoreMe
```

| epochMillis   |
| ------------- |
| 1565190733000 |

```sql
SELECT FromDateTime(
    '2019-08-07T15:12:13', 
    'yyyy-MM-dd''T''HH:mm:ss'
    ) AS epochMillis
FROM ignoreMe
```

| epochMillis   |
| ------------- |
| 1565190733000 |

```sql
SELECT FromDateTime(
    '2019-08-07T07:12:13-0800', 
    'yyyy-MM-dd''T''HH:mm:ssZ'
    ) AS epochMillis
FROM ignoreMe
```

| epochMillis   |
| ------------- |
| 1565190733000 |
