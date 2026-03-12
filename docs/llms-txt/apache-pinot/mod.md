# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/mod.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/mod.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/mod.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/mod.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/mod.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/mod.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/mod.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/mod.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/mod.md

# Source: https://docs.pinot.apache.org/functions-1/mod.md

# MOD

Modulo of two values

## Signature

> MOD(col1, col2)

## Usage Examples

```sql
select MOD(12, 5) AS value
from ignoreMe
```

| value |
| ----- |
| 2     |

```sql
select MOD(12, 2) AS value
from ignoreMe
```

| value |
| ----- |
| 0     |
