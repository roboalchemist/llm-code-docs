# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/stpoint.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/stpoint.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/stpoint.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/stpoint.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/stpoint.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/stpoint.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/stpoint.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/stpoint.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/stpoint.md

# Source: https://docs.pinot.apache.org/functions-1/stpoint.md

# STPOINT

Returns a geometry or geography type point object with the given coordinate values.

## Signature

> STPOINT(x, y)
>
> STPOINT(x, y, isGeography)
>
> ST\_POINT(x, y)
>
> ST\_POINT(x, y, isGeography)

## Usage Examples

```sql
select STPOINT(-122, 37) AS value
from ignoreMe 
```

| value                              |
| ---------------------------------- |
| 00c05e8000000000004042800000000000 |

```sql
select STPOINT(-122, 37, 0) AS value
from ignoreMe 
```

| value                              |
| ---------------------------------- |
| 00c05e8000000000004042800000000000 |

```sql
select STPOINT(-122, 37, 1) AS value
from ignoreMe 
```

| value                              |
| ---------------------------------- |
| 80c05e8000000000004042800000000000 |

```sql
select ST_POINT(-122, 37, 1) AS value
from ignoreMe 
```

| value                              |
| ---------------------------------- |
| 80c05e8000000000004042800000000000 |
