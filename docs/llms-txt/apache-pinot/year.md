# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/year.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/year.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/year.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/year.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/year.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/year.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/year.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/year.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/year.md

# Source: https://docs.pinot.apache.org/functions-1/year.md

# year

Returns the year from the given epoch millis in UTC timezone.

## Signature

> year(tsInMillis)
>
> year(tsInMillis, timeZoneId)

## Usage Examples

```sql
select year(1609472186000) AS year
FROM ignoreMe
```

| year |
| ---- |
| 2021 |

```sql
select year(1609472186000, 'America/Toronto') AS year
FROM ignoreMe
```

| year |
| ---- |
| 2020 |
