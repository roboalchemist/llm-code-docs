# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/arrayconcatint.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/arrayconcatint.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/arrayconcatint.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/arrayconcatint.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/arrayconcatint.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/arrayconcatint.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/arrayconcatint.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/arrayconcatint.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/arrayconcatint.md

# Source: https://docs.pinot.apache.org/functions-1/arrayconcatint.md

# arrayConcatInt

Concatenates two arrays of ints.

## Signature

> arrayConcatInt('colName1', 'colName2')

## Usage Examples

These examples are based on the [Hybrid Quick Start](https://docs.pinot.apache.org/basics/getting-started/quick-start#hybrid).

```sql
select DivWheelsOffs, 
       arrayConcatInt(DivWheelsOffs, DivWheelsOns) AS concatIds
from airlineStats 
WHERE arraylength(DivWheelsOffs) >= 2
limit 5
```

| DivWheelsOffs | concatIds           |
| ------------- | ------------------- |
| 1453,1731     | 1453,1731,1415,1623 |
| 1908,1758     | 1908,1758,1339,2310 |
| 1453,1731     | 1453,1731,1415,1623 |
| 1908,1758     | 1908,1758,1339,2310 |
