# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/arrayconcatdouble.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/arrayconcatdouble.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/arrayconcatdouble.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/arrayconcatdouble.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/arrayconcatdouble.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/arrayconcatdouble.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/arrayconcatdouble.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/arrayconcatdouble.md

# Source: https://docs.pinot.apache.org/functions-1/arrayconcatdouble.md

# arrayConcatDouble

Concatenates two arrays of doubles.

## Signature

> arrayConcatDouble('colName1', 'colName2')

## Usage Examples

This example assumes the multiValueTable columns mvCol1 and mvCol2 are both of type DOUBLE with singleValueField in the table schema set to false.

```sql
select mvCol1, 
       arrayConcatDouble(mvCol1, mvCol2) AS concatDoubles
from multiValueTable
WHERE arraylength(mvCol1) >= 2
limit 5
```
