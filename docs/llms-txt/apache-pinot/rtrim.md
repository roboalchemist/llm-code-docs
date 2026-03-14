# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/rtrim.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/rtrim.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/rtrim.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/rtrim.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/rtrim.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/rtrim.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/rtrim.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/rtrim.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/rtrim.md

# Source: https://docs.pinot.apache.org/functions-1/rtrim.md

# rtrim

rtrim spaces from right side of the string

## Signature

> RTRIM(col)

## Usage Examples

```sql
SELECT ' Pinot with spaces  ' AS notTrimmed,
       rtrim(' Pinot with spaces ') AS trimmed
FROM ignoreMe
```

| notTrimmed              | trimmed                |
| ----------------------- | ---------------------- |
| `" Pinot with spaces "` | `" Pinot with spaces"` |
