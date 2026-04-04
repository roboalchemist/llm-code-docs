# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/togeometry.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/togeometry.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/togeometry.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/togeometry.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/togeometry.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/togeometry.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/togeometry.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/togeometry.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/togeometry.md

# Source: https://docs.pinot.apache.org/functions-1/togeometry.md

# toGeometry

Converts a spherical geographical object to a Geometry object.

## Signature

> toGeometry(geographyObject)

## Usage Examples

```sql
select toGeometry(
    STPOINT(-122, 37, 1)
) AS value
from ignoreMe 
```

| value                              |
| ---------------------------------- |
| 00c05e8000000000004042800000000000 |

{% hint style="info" %}
You can create geographical objects using the [STPOINT](https://docs.pinot.apache.org/functions-1/stpoint) and [ST\_GeogFromText](https://docs.pinot.apache.org/functions-1/stgeogfromtext) functions.
{% endhint %}
