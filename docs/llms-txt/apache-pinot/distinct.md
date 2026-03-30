# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/distinct.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/distinct.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/distinct.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/distinct.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/distinct.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/distinct.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/distinct.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/distinct.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/distinct.md

# Source: https://docs.pinot.apache.org/functions-1/distinct.md

# DISTINCT

Returns the distinct row values in a group

## Signature

> DISTINCT(colName)

## Usage Examples

These examples are based on the [Batch Quick Start](https://docs.pinot.apache.org/basics/getting-started/quick-start#batch).

```sql
select DISTINCT league AS value
from baseballStats 
```

| value |
| ----- |
| NL    |
| UA    |
| AL    |
| NA    |
| PL    |
| AA    |
| FL    |

```sql
select DISTINCT(league) AS value
from baseballStats 
```

| value |
| ----- |
| NL    |
| UA    |
| AL    |
| NA    |
| PL    |
| AA    |
| FL    |
