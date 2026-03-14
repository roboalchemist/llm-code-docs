# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/stgeomfromwkb.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/stgeomfromwkb.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/stgeomfromwkb.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/stgeomfromwkb.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/stgeomfromwkb.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/stgeomfromwkb.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/stgeomfromwkb.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/stgeomfromwkb.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/stgeomfromwkb.md

# Source: https://docs.pinot.apache.org/functions-1/stgeomfromwkb.md

# ST\_GeomFromWKB

Returns a geometry type object from WKB representation.

## Signature

> ST\_GeomFromWKB(wkb)

## Usage Examples

```sql
select STPOINT(-122, 37) AS point,
       ST_GeomFromWKB(
         ST_AsBinary(STPOINT(-122, 37))
       ) AS value
from ignoreMe 
```

| point                              | value                              |
| ---------------------------------- | ---------------------------------- |
| 00c05e8000000000004042800000000000 | 00c05e8000000000004042800000000000 |

{% hint style="info" %}
You can create geometry objects in the WKB format using the [ST\_AsBinary](https://docs.pinot.apache.org/functions-1/stasbinary) function.
{% endhint %}
