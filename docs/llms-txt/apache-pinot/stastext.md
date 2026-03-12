# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/stastext.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/stastext.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/stastext.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/stastext.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/stastext.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/stastext.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/stastext.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/stastext.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/stastext.md

# Source: https://docs.pinot.apache.org/functions-1/stastext.md

# ST\_AsText

Returns the WKT representation of the geometry/geography.

## Signature

> ST\_AsText(geometryObject)

## Usage Examples

```sql
select stAsText(
    STPOINT(-122, 37)
) AS value
from ignoreMe 
```

| value           |
| --------------- |
| POINT (-122 37) |

```sql
select stAsText(
    ST_GeogFromText('LINESTRING (30 10, 10 30, 40 40)')
) AS value
from ignoreMe 
```

| value                            |
| -------------------------------- |
| LINESTRING (30 10, 10 30, 40 40) |
