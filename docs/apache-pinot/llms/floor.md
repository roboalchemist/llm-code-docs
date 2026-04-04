# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/floor.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/floor.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/floor.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/floor.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/floor.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/floor.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/floor.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/floor.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/floor.md

# Source: https://docs.pinot.apache.org/functions-1/floor.md

# FLOOR

Rounded down to the nearest integer.

## Signature

> FLOOR(col1)

## Usage Examples

```sql
select FLOOR(12.1) AS value
from ignoreMe
```

| value |
| ----- |
| 12    |

```sql
select FLOOR(-12.1) AS value
from ignoreMe
```

| value |
| ----- |
| -13   |
