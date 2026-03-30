# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/now.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/now.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/now.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/now.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/now.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/now.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/now.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/now.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/now.md

# Source: https://docs.pinot.apache.org/functions-1/now.md

# now

Return current time as epoch millis.

## Signature

> now()

## Usage Examples

```sql
select now() AS now
FROM ignoreMe
```

| now           |
| ------------- |
| 1639150454255 |

This function is typically used in predicate to filter on timestamp for recent data. e.g. filter data on recent 1 day(86400 seconds)

```sql
SELECT * 
FROM tableName
WHERE tsInMillis > now() - 86400000
```
