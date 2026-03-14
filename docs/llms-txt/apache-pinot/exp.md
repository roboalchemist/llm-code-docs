# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/exp.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/exp.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/exp.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/exp.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/exp.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/exp.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/exp.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/exp.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/exp.md

# Source: https://docs.pinot.apache.org/functions-1/exp.md

# exp

Euler’s number(e) raised to the power of col.

## Signature

> EXP(col1)

## Usage Examples

```sql
select EXP(1) AS value
from ignoreMe
```

| value             |
| ----------------- |
| 2.718281828459045 |

```sql
select EXP(12) AS value
from ignoreMe
```

| value              |
| ------------------ |
| 162754.79141900392 |
