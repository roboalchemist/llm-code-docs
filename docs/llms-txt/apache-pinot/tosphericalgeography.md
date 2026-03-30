# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/tosphericalgeography.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/tosphericalgeography.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/tosphericalgeography.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/tosphericalgeography.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/tosphericalgeography.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/tosphericalgeography.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/tosphericalgeography.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/tosphericalgeography.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/tosphericalgeography.md

# Source: https://docs.pinot.apache.org/functions-1/tosphericalgeography.md

# toSphericalGeography

Converts a Geometry object to a spherical geography object.

## Signature

> toSphericalGeography(geometryObject)

## Usage Examples

```sql
select toSphericalGeography(
    STPOINT(-122, 37)
) AS value
from ignoreMe 
```

| value                              |
| ---------------------------------- |
| 80c05e8000000000004042800000000000 |

{% hint style="info" %}
You can create geometry objects using the [STPOINT](https://docs.pinot.apache.org/functions-1/stpoint) and [ST\_GeomFromText](https://docs.pinot.apache.org/functions-1/stgeomfromtext) functions.
{% endhint %}
