# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/minute.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/minute.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/minute.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/minute.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/minute.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/minute.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/minute.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/minute.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/minute.md

# Source: https://docs.pinot.apache.org/functions-1/minute.md

# minute

Returns the minute of the hour from the given epoch millis in UTC or specified timezone. The value ranges from 0 to 59.

## Signature

> minute(tsInMillis)
>
> minute(tsInMillis, timeZoneId)

## Usage Examples

```sql
select minute(1639351800000) AS minute
FROM ignoreMe
```

| minute |
| ------ |
| 30     |

```sql
select minute(1639351800000, 'America/St_Johns') AS minute
FROM ignoreMe
```

| minute |
| ------ |
| 0      |
