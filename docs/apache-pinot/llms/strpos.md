# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/strpos.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/strpos.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/strpos.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/strpos.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/strpos.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/strpos.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/strpos.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/strpos.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/strpos.md

# Source: https://docs.pinot.apache.org/functions-1/strpos.md

# strpos

Find Nth instance of find string in input. Returns 0 if input string is empty. Returns -1 if the Nth instance is not found or input string is null.

## Signature

> STRPOS(col, find, N)

## Usage Examples

```sql
SELECT STRPOS('Apache Pinot is a column-oriented, open-source, distributed data store written in Java', 'o', 1) AS value
FROM ignoreMe
```

| value |
| ----- |
| 10    |

```sql
SELECT STRPOS('Apache Pinot is a column-oriented, open-source, distributed data store written in Java', 'o', 2) AS value
FROM ignoreMe
```

| value |
| ----- |
| 19    |

```sql
SELECT STRPOS('Apache Pinot is a column-oriented, open-source, distributed data store written in Java', 'z', 1) AS value
FROM ignoreMe
```

| value |
| ----- |
| -1    |
