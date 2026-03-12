# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/ln.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/ln.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/ln.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/ln.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/ln.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/ln.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/ln.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/ln.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/ln.md

# Source: https://docs.pinot.apache.org/functions-1/ln.md

# ln

Natural log of value i.e. ln(col1)

## Signature

> LN(col1)

## Usage Examples

```sql
select ln(1) AS value
from ignoreMe
```

| value |
| ----- |
| 0     |

```sql
select ln(12) AS value
from ignoreMe
```

| value              |
| ------------------ |
| 2.4849066497880004 |
