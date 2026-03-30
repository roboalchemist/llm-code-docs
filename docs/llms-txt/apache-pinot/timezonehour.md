# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/timezonehour.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/timezonehour.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/timezonehour.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/timezonehour.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/timezonehour.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/timezonehour.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/timezonehour.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/timezonehour.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/timezonehour.md

# Source: https://docs.pinot.apache.org/functions-1/timezonehour.md

# timezoneHour

Returns the hour of the time zone offset. The timezoneId provided should be in [Joda Time format](https://www.joda.org/joda-time/timezones.html).

## Signature

> timezoneHour(timezoneId)

## Usage Examples

```sql
SELECT timezoneHour('America/Toronto') AS hour
FROM ignoreMe
```

| hour |
| ---- |
| 19   |

```sql
SELECT timezoneHour('UTC') AS hour
FROM ignoreMe
```

| hour |
| ---- |
| 0    |

```sql
SELECT timezoneHour('Europe/Rome') AS hour
FROM ignoreMe
```

| hour |
| ---- |
| 1    |
