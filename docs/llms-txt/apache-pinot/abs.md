# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/abs.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/abs.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/abs.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/abs.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/abs.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/abs.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/abs.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/abs.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/abs.md

# Source: https://docs.pinot.apache.org/functions-1/abs.md

# ABS

Absolute of a value

## Signature

> ABS(col1)

## Usage Examples

```sql
select ABS(-12.1) AS value
from ignoreMe
```

| value |
| ----- |
| 12.1  |

```sql
select ABS(12.1) AS value
from ignoreMe
```

| value |
| ----- |
| 12.1  |
