# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/dayofweek.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/dayofweek.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/dayofweek.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/dayofweek.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/dayofweek.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/dayofweek.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/dayofweek.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/dayofweek.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/dayofweek.md

# Source: https://docs.pinot.apache.org/functions-1/dayofweek.md

# dayOfWeek

Returns the day of the week from the given epoch millis in UTC timezone. The value ranges from 1(Monday) to 7(Sunday).

## Signature

> dayOfWeek(tsInMillis)
>
> dayOfWeek(tsInMillis, timeZoneId)
>
> dow(tsInMillis)
>
> dow(tsInMillis, timeZoneId)

## Usage Examples

```sql
select dayOfWeek(1639351800000) AS dayOfWeek
FROM ignoreMe
```

| dayOfWeek |
| --------- |
| 7         |

```sql
select dayOfWeek(1639351800000, 'CET') AS dayOfWeek
FROM ignoreMe
```

| dayOfWeek |
| --------- |
| 1         |

```sql
select dow(1639351800000) AS dayOfWeek
FROM ignoreMe
```

| dayOfWeek |
| --------- |
| 7         |

```sql
select dow(1639351800000, 'CET') AS dayOfWeek
FROM ignoreMe
```

| dayOfWeek |
| --------- |
| 1         |
