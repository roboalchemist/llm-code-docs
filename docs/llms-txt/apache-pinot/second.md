# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/second.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/second.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/second.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/second.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/second.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/second.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/second.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/second.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/second.md

# Source: https://docs.pinot.apache.org/functions-1/second.md

# second

Returns the second of the minute from the given epoch millis in UTC or specified timezone. The value ranges from 0 to 59.

## Signature

> second(tsInMillis)
>
> second(tsInMillis, timeZoneId)

## Usage Examples

```sql
select second(1639351800000) AS second
FROM ignoreMe
```

| second |
| ------ |
| 0      |

```sql
select second(1639351800000, 'America/St_Johns') AS second
FROM ignoreMe
```

| second |
| ------ |
| 0      |
