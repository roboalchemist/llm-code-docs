# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/millisecond.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/millisecond.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/millisecond.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/millisecond.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/millisecond.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/millisecond.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/millisecond.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/millisecond.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/millisecond.md

# Source: https://docs.pinot.apache.org/functions-1/millisecond.md

# millisecond

Returns the millisecond of the second from the given epoch millis in UTC or specified timezone. The value ranges from 0 to 999.

## Signature

> millisecond(tsInMillis)
>
> millisecond(tsInMillis, timeZoneId)

## Usage Examples

```sql
select millisecond(1639351800000) AS millisecond
FROM ignoreMe
```

| millisecond |
| ----------- |
| 0           |

```sql
select millisecond(1639351800000, 'America/St_Johns') AS millisecond
FROM ignoreMe
```

| millisecond |
| ----------- |
| 0           |
