# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/ltrim.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/ltrim.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/ltrim.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/ltrim.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/ltrim.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/ltrim.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/ltrim.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/ltrim.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/ltrim.md

# Source: https://docs.pinot.apache.org/functions-1/ltrim.md

# ltrim

trim spaces from left side of the string

## Signature

> LTRIM(col)

## Usage Examples

```sql
SELECT ' Pinot with spaces  ' AS notTrimmed,
       ltrim(' Pinot with spaces ') AS trimmed
FROM ignoreMe
```

| notTrimmed              | trimmed                |
| ----------------------- | ---------------------- |
| `" Pinot with spaces "` | `"Pinot with spaces "` |
