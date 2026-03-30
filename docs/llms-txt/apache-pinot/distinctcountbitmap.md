# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/distinctcountbitmap.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/distinctcountbitmap.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/distinctcountbitmap.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/distinctcountbitmap.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/distinctcountbitmap.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/distinctcountbitmap.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/distinctcountbitmap.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/distinctcountbitmap.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/distinctcountbitmap.md

# Source: https://docs.pinot.apache.org/functions-1/distinctcountbitmap.md

# DISTINCTCOUNTBITMAP

Returns the count of distinct row values in a group. This function is accurate for *INT* column, but approximate for other cases where hash codes are used in distinct counting and there may be hash collisions.\
For accurate distinct counting on all column types, see [DISTINCTCOUNT](https://docs.pinot.apache.org/functions-1/distinctcount).

## Signature

> DISTINCTCOUNTBITMAP(colName)

## Usage Examples

These examples are based on the [Batch Quick Start](https://docs.pinot.apache.org/basics/getting-started/quick-start#batch).

```sql
select DISTINCTCOUNTBITMAP(league) AS value
from baseballStats 
```

| value |
| ----- |
| 7     |

```sql
select DISTINCTCOUNTBITMAP(teamID) AS value
from baseballStats 
```

| value |
| ----- |
| 148   |
