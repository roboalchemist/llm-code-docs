# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/substr.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/substr.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/substr.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/substr.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/substr.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/substr.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/substr.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/substr.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/substr.md

# Source: https://docs.pinot.apache.org/functions-1/substr.md

# substr

Get substring of the input string from start to endIndex. Index begins at 0. Set endIndex to -1 to calculate till end of the string

## Signature

> SUBSTR(col, startIndex, endIndex)

## Usage Examples

```sql
select SUBSTR('Pinot', 1, -1) AS name
FROM ignoreMe
```

| name |
| ---- |
| inot |

```sql
select SUBSTR('Pinot', 0, 2) AS name
FROM ignoreMe
```

| name |
| ---- |
| Pi   |
