# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/ceil.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/ceil.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/ceil.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/ceil.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/ceil.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/ceil.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/ceil.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/ceil.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/ceil.md

# Source: https://docs.pinot.apache.org/functions-1/ceil.md

# ceil

Rounded up to the nearest integer.

## Signature

> CEIL(col1)

## Usage Examples

```sql
select CEIL(12.1) AS value
from ignoreMe
```

| value |
| ----- |
| 13    |

```sql
select CEIL(-12.1) AS value
from ignoreMe
```

| value |
| ----- |
| -12   |
