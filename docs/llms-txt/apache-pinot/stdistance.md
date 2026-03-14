# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/stdistance.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/stdistance.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/stdistance.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/stdistance.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/stdistance.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/stdistance.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/stdistance.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/stdistance.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/stdistance.md

# Source: https://docs.pinot.apache.org/functions-1/stdistance.md

# ST\_Distance

For geometry type, returns the 2-dimensional cartesian minimum distance (based on spatial ref) between two geometries in projected units. For geography, returns the great-circle distance in meters between two SphericalGeography points. Note that g1, g2 shall have the same type.

## Signature

> ST\_Distance(geography/geometry, geography/geometry)

## Usage Examples

These examples are based on the [Streaming Quick Start](https://docs.pinot.apache.org/basics/getting-started/quick-start#streaming).

```sql
select group_city, 
       STASTEXT(location) AS locationString, 
       ST_Distance(location, ST_POINT(2.154007,41.390205, 1)) AS distanceInMetres
from meetupRsvp 
LIMIT 1
```

| group\_city | locationString      | distanceInMetres  |
| ----------- | ------------------- | ----------------- |
| Madrid      | POINT (-3.71 40.42) | 504376.5534398629 |
