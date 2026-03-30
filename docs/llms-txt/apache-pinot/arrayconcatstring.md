# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/arrayconcatstring.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/arrayconcatstring.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/arrayconcatstring.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/arrayconcatstring.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/arrayconcatstring.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/arrayconcatstring.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/arrayconcatstring.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/arrayconcatstring.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/arrayconcatstring.md

# Source: https://docs.pinot.apache.org/functions-1/arrayconcatstring.md

# arrayConcatString

Concatenates two arrays of strings.

## Signature

> arrayConcatString('colName1', 'colName2')

## Usage Examples

These examples are based on the [Hybrid Quick Start](https://docs.pinot.apache.org/basics/getting-started/quick-start#hybrid).

```sql
select DivTailNums, 
       arrayConcatString(DivTailNums, DivTailNums) AS concatIds
from airlineStats 
WHERE arraylength(DivTailNums) >= 2
limit 5
```

| DivTailNums   | concatIds                   |
| ------------- | --------------------------- |
| N7713A,N7713A | N7713A,N7713A,N7713A,N7713A |
| N344AA,N344AA | N344AA,N344AA,N344AA,N344AA |
| N344AA,N344AA | N344AA,N344AA,N344AA,N344AA |
| N7713A,N7713A | N7713A,N7713A,N7713A,N7713A |
