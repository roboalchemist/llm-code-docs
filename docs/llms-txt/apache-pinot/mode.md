# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/mode.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/mode.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/mode.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/mode.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/mode.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/mode.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/mode.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/mode.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/mode.md

# Source: https://docs.pinot.apache.org/functions-1/mode.md

# mode

Get the most frequent value in a group. When multiple modes are present it gives the minimum of all the modes. This behavior can be overridden to get the maximum or the average mode.

## Signature

> MODE(colName, \[reducerType])

## Usage Examples

These examples are based on the [Batch Quick Start](https://docs.pinot.apache.org/basics/getting-started/quick-start#batch).

```sql
select mode(yearID) AS value
from baseballStats 
WHERE AtBatting != 0 AND yearID > 2001
```

| value |
| ----- |
| 2008  |

```sql
select mode(yearID, 'AVG') AS value
from baseballStats 
WHERE AtBatting != 0 AND yearID > 2001
```

| value |
| ----- |
| 2010  |

```sql
select mode(yearID, 'MIN') AS value
from baseballStats 
WHERE AtBatting != 0 AND yearID > 2001
```

| value |
| ----- |
| 2008  |

```sql
select mode(yearID, 'MAX') AS value
from baseballStats 
WHERE AtBatting != 0 AND yearID > 2001
```

| value |
| ----- |
| 2012  |
