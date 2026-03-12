# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/rpad.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/rpad.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/rpad.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/rpad.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/rpad.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/rpad.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/rpad.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/rpad.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/rpad.md

# Source: https://docs.pinot.apache.org/functions-1/rpad.md

# rpad

string padded from the right side with `pad` to reach final `size`

## Signature

> RPAD(col, size, pad)

## Usage Examples

```sql
SELECT RPAD('Hello, World', '20', '*') AS value
FROM ignoreMe
```

| value                        |
| ---------------------------- |
| Hello, World\*\*\*\*\*\*\*\* |
