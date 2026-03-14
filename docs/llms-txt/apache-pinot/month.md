# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/month.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/month.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/month.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/month.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/month.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/month.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/month.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/month.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/month.md

# Source: https://docs.pinot.apache.org/functions-1/month.md

# month

Returns the month of the year from the given epoch millis in UTC or specified timezone. The value ranges from 1 to 12.

## Signature

> month(tsInMillis)
>
> month(tsInMillis, timeZoneId)

## Usage Examples

```sql
select month(1633046399000, 'UTC') AS month
FROM ignoreMe
```

| month |
| ----- |
| 9     |

```sql
select month(1633046399000, 'CET') AS month
FROM ignoreMe
```

| month |
| ----- |
| 10    |
