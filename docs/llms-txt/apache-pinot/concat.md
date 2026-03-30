# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/concat.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/concat.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/concat.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/concat.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/concat.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/concat.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/concat.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/concat.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/concat.md

# Source: https://docs.pinot.apache.org/functions-1/concat.md

# concat

Concatenate two input strings using the seperator

## Signature

> CONCAT(col1, col2, seperator)

## Usage Examples

```sql
SELECT concat('Apache', 'Pinot', ' ') AS value
FROM ignoreMe
```

| value        |
| ------------ |
| Apache Pinot |

```sql
SELECT concat('real-time', 'analytics', '__') AS value
FROM ignoreMe
```

| value                  |
| ---------------------- |
| real-time\_\_analytics |
