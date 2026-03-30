# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/lpad.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/lpad.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/lpad.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/lpad.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/lpad.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/lpad.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/lpad.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/lpad.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/lpad.md

# Source: https://docs.pinot.apache.org/functions-1/lpad.md

# lpad

string padded from the left side with `pad` to reach final `size`

## Signature

> LPAD(col, size, pad)

## Usage Examples

```sql
SELECT LPAD('Hello, World', '20', '*') AS value
FROM ignoreMe
```

| value                        |
| ---------------------------- |
| \*\*\*\*\*\*\*\*Hello, World |
