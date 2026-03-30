# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/startswith.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/startswith.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/startswith.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/startswith.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/startswith.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/startswith.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/startswith.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/startswith.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/startswith.md

# Source: https://docs.pinot.apache.org/functions-1/startswith.md

# startswith

returns true if columns starts with prefix string.

## Signature

> STARTSWITH(col, prefix)

## Usage Examples

```sql
SELECT STARTSWITH('Apache Pinot', 'Apache') AS value
FROM ignoreMe
```

| value |
| ----- |
| true  |

```sql
SELECT STARTSWITH('Apache Pinot', 'Pinot') AS value
FROM ignoreMe
```

| value |
| ----- |
| false |
