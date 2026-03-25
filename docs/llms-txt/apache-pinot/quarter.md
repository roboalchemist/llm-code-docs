# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/quarter.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/quarter.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/quarter.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/quarter.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/quarter.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/quarter.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/quarter.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/quarter.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/quarter.md

# Source: https://docs.pinot.apache.org/functions-1/quarter.md

# quarter

Returns the quarter of the year from the given epoch millis in UTC or specified timezone. The value ranges from 1 to 4

## Signature

> quarter(tsInMillis)
>
> quarter(tsInMillis, timeZoneId)

## Usage Examples

```sql
select quarter(1633046399000) AS quarter
FROM ignoreMe
```

| quarter |
| ------- |
| 3       |

```sql
select quarter(1633046399000, 'UTC') AS quarter
FROM ignoreMe
```

| quarter |
| ------- |
| 3       |

```sql
select quarter(1633046399000, 'CET') AS quarter
FROM ignoreMe
```

| quarter |
| ------- |
| 4       |
