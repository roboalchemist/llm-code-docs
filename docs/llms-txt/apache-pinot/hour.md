# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/hour.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/hour.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/hour.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/hour.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/hour.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/hour.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/hour.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/hour.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/hour.md

# Source: https://docs.pinot.apache.org/functions-1/hour.md

# hour

Returns the hour of the day from the given epoch millis in UTC or specified timezone. The value ranges from 0 to 23.

## Signature

> hour(tsInMillis)
>
> hour(tsInMillis, timeZoneId)

## Usage Examples

```sql
select hour(1639351800000) AS hour
FROM ignoreMe
```

| hour |
| ---- |
| 23   |

```sql
select hour(1639351800000, 'CET') AS hour
FROM ignoreMe
```

| hour |
| ---- |
| 0    |
