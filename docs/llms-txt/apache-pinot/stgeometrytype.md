# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/stgeometrytype.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/stgeometrytype.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/stgeometrytype.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/stgeometrytype.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/stgeometrytype.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/stgeometrytype.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/stgeometrytype.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/stgeometrytype.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/stgeometrytype.md

# Source: https://docs.pinot.apache.org/functions-1/stgeometrytype.md

# ST\_GeometryType

Returns the type of the geometry as a string

## Signature

> ST\_GeometryType(geometry)

## Usage Examples

These examples are based on the [Streaming Quick Start](https://docs.pinot.apache.org/basics/getting-started/quick-start#streaming).

```sql
select location, ST_GeometryType(location) AS type
from meetupRsvp 
LIMIT 1
```

| location                           | type  |
| ---------------------------------- | ----- |
| 80c00dae147ae147ae404435c28f5c28f6 | Point |
