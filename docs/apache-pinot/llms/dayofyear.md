# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/dayofyear.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/dayofyear.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/dayofyear.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/dayofyear.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/dayofyear.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/dayofyear.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/dayofyear.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/dayofyear.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/dayofyear.md

# Source: https://docs.pinot.apache.org/functions-1/dayofyear.md

# dayOfYear

Returns the day of the year from the given epoch millis in UTC or specified timezone. The value ranges from 1 to 366.

## Signature

> dayOfYear(tsInMillis)
>
> dayOfYear(tsInMillis, timeZoneId)
>
> doy(tsInMillis)
>
> doy(tsInMillis, timeZoneId)

## Usage Examples

```sql
select dayOfYear(1639351800000) AS dayOfYear
FROM ignoreMe
```

| dayOfYear |
| --------- |
| 346       |

```sql
select dayOfYear(1639351800000, 'CET') AS dayOfYear
FROM ignoreMe
```

| dayOfYear |
| --------- |
| 347       |

```sql
select doy(1639351800000) AS dayOfYear
FROM ignoreMe
```

| dayOfYear |
| --------- |
| 346       |

```sql
select doy(1639351800000, 'CET') AS dayOfYear
FROM ignoreMe
```

| dayOfYear |
| --------- |
| 347       |
