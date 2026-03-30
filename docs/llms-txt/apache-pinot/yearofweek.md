# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/yearofweek.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/yearofweek.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/yearofweek.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/yearofweek.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/yearofweek.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/yearofweek.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/yearofweek.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/yearofweek.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/yearofweek.md

# Source: https://docs.pinot.apache.org/functions-1/yearofweek.md

# yearOfWeek

Returns the year of the ISO week from the given epoch millis and timezone id. Alias `yow`is also supported.

## Signature

> yearOfWeek(tsInMillis)
>
> yearOfWeek(tsInMillis, timeZoneId)

> yow(tsInMillis)
>
> yow(tsInMillis, timeZoneId)

## Usage Examples

```sql
select yearOfWeek(1609731386000) AS year
FROM ignoreMe
```

| year |
| ---- |
| 2021 |

```sql
select yearOfWeek(1609731386000, 'America/Toronto') AS year
FROM ignoreMe
```

| year |
| ---- |
| 2020 |

```sql
select yow(1609731386000) AS year
FROM ignoreMe
```

| year |
| ---- |
| 2021 |

```sql
select yow(1609731386000, 'America/Toronto') AS year
FROM ignoreMe
```

| year |
| ---- |
| 2020 |
