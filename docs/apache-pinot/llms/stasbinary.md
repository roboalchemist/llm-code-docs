# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/stasbinary.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/stasbinary.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/stasbinary.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/stasbinary.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/stasbinary.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/stasbinary.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/stasbinary.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/stasbinary.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/stasbinary.md

# Source: https://docs.pinot.apache.org/functions-1/stasbinary.md

# ST\_AsBinary

Returns the WKB representation of the geometry.

## Signature

> ST\_AsBinary(geometryObject)

## Usage Examples

```sql
select ST_AsBinary(
    STPOINT(-122, 37)
) AS value
from ignoreMe 
```

| value                                      |
| ------------------------------------------ |
| 0000000001c05e8000000000004042800000000000 |

```sql
select ST_AsBinary(
    ST_GeogFromText('LINESTRING (30 10, 10 30, 40 40)')
) AS value
from ignoreMe 
```

| value                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------ |
| 000000000200000003403e00000000000040240000000000004024000000000000403e00000000000040440000000000004044000000000000 |
