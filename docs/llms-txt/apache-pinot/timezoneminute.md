# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/timezoneminute.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/timezoneminute.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/timezoneminute.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/timezoneminute.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/timezoneminute.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/timezoneminute.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/timezoneminute.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/timezoneminute.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/timezoneminute.md

# Source: https://docs.pinot.apache.org/functions-1/timezoneminute.md

# timezoneMinute

Returns the minute of the time zone offset. The timezoneId provided should be in [Joda Time format](https://www.joda.org/joda-time/timezones.html).

## Signature

> timezoneMinute(timezoneId)

## Usage Examples

```sql
SELECT timezoneMinute('America/Toronto') AS minute
FROM ignoreMe
```

| minute |
| ------ |
| 0      |

```sql
SELECT timezoneMinute('Asia/Colombo') AS minute
FROM ignoreMe
```

| minute |
| ------ |
| 30     |

```sql
SELECT timezoneMinute('Asia/Kathmandu') AS minute
FROM ignoreMe
```

| minute |
| ------ |
| 45     |
