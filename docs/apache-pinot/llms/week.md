# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/week.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/week.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/week.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/week.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/week.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/week.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/week.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/week.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/week.md

# Source: https://docs.pinot.apache.org/functions-1/week.md

# week

Returns the ISO week of the year from the given epoch millis in UTC or specified timezone. The value ranges from 1 to 53.

## Signature

> week(tsInMillis)
>
> week(tsInMillis, timeZoneId)
>
> weekOfYear(tsInMillis)
>
> weekOfYear(tsInMillis, timeZoneId)

## Usage Examples

```sql
select week(1639351800000) AS week
FROM ignoreMe
```

| week |
| ---- |
| 49   |

```sql
select week(1639351800000, 'CET') AS week
FROM ignoreMe
```

| week |
| ---- |
| 50   |

```sql
select weekOfYear(1639351800000) AS week
FROM ignoreMe
```

| week |
| ---- |
| 49   |

```sql
select weekOfYear(1639351800000, 'CET') AS week
FROM ignoreMe
```

| week |
| ---- |
| 50   |
