# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/extract.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/extract.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/extract.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/extract.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/extract.md

# Source: https://docs.pinot.apache.org/functions-1/extract.md

# Extract

Returns the selected field from the DATETIME expression.

### Signature

> EXTRACT(field FROM expression)

### Usage Examples

```sql
select EXTRACT(MONTH FROM '2017-06-15')
```

| value |
| ----- |
| 06    |

```sql
select EXTRACT(YEAR FROM '2017-06-15 09:34:21')
```

| value |
| ----- |
| 2017  |
