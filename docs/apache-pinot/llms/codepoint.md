# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/codepoint.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/codepoint.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/codepoint.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/codepoint.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/codepoint.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/codepoint.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/codepoint.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/codepoint.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/codepoint.md

# Source: https://docs.pinot.apache.org/functions-1/codepoint.md

# codepoint

the Unicode codepoint of the first character of the string

## Signature

> CODEPOINT(col)

## Usage Examples

```sql
SELECT CODEPOINT('Apache Pinot') AS value
FROM ignoreMe
```

| value |
| ----- |
| 65    |
