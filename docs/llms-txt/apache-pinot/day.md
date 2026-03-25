# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/day.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/day.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/day.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/day.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/day.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/day.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/day.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/day.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/day.md

# Source: https://docs.pinot.apache.org/functions-1/day.md

# day

Returns the day of the month from the given epoch millis in UTC or specified timezone. The value ranges from 1 to 31.

## Signature

> day(tsInMillis)
>
> day(tsInMillis, timeZoneId)
>
> dayOfMonth(tsInMillis)
>
> dayOfMonth(tsInMillis, timeZoneId)

## Usage Examples

```sql
select day(1639351800000) AS day
FROM ignoreMe
```

| day |
| --- |
| 12  |

```sql
select day(1639351800000, 'CET') AS day
FROM ignoreMe
```

| day |
| --- |
| 13  |

```sql
select dayOfMonth(1639351800000) AS day
FROM ignoreMe
```

| day |
| --- |
| 12  |

```sql
select dayOfMonth(1639351800000, 'CET') AS day
FROM ignoreMe
```

| day |
| --- |
| 13  |
