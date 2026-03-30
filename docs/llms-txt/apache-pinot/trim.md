# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/trim.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/trim.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/trim.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/trim.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/trim.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/trim.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/trim.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/trim.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/trim.md

# Source: https://docs.pinot.apache.org/functions-1/trim.md

# trim

trim spaces from both side of the string

## Signature

> TRIM(col)

## Usage Examples

```sql
SELECT ' Pinot with spaces  ' AS notTrimmed,
       trim(' Pinot with spaces ') AS trimmed
FROM ignoreMe
```

| notTrimmed              | trimmed               |
| ----------------------- | --------------------- |
| `" Pinot with spaces "` | `"Pinot with spaces"` |
