# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/arrayconcatfloat.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/arrayconcatfloat.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/arrayconcatfloat.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/arrayconcatfloat.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/arrayconcatfloat.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/arrayconcatfloat.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/arrayconcatfloat.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/arrayconcatfloat.md

# Source: https://docs.pinot.apache.org/functions-1/arrayconcatfloat.md

# arrayConcatFloat

Concatenates two arrays of floats.

## Signature

> arrayConcatFloat('colName1', 'colName2')

## Usage Examples

This example assumes the multiValueTable columns mvCol1 and mvCol2 are both of type FLOAT with singleValueField in the table schema set to false.

```sql
select mvCol1, 
       arrayConcatFloat(mvCol1, mvCol2) AS concatFloats
from multiValueTable
WHERE arraylength(mvCol1) >= 2
limit 5
```
