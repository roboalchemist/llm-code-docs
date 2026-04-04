# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/countmv.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/countmv.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/countmv.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/countmv.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/countmv.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/countmv.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/countmv.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/countmv.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/countmv.md

# Source: https://docs.pinot.apache.org/functions-1/countmv.md

# COUNTMV

Get the count of rows in a group

## Signature

> COUNTMV(colName)

## Usage Examples

These examples are based on the [Hybrid Quick Start](https://docs.pinot.apache.org/basics/getting-started/quick-start#hybrid).

The following query returns the documents that have a `DivTailNums` with more than one value:

```sql
select DivTailNums
from airlineStats 
where arraylength(DivTailNums) > 1
```

| DivTailNums   |
| ------------- |
| N7713A,N7713A |
| N344AA,N344AA |
| N344AA,N344AA |
| N7713A,N7713A |

You can count the number of items in these rows by running the following query:

```sql
select COUNTMV(DivTailNums) AS value
from airlineStats 
where arraylength(DivTailNums) > 1
```

| value |
| ----- |
| 8     |
