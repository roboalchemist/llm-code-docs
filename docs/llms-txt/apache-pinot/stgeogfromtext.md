# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/stgeogfromtext.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/stgeogfromtext.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/stgeogfromtext.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/stgeogfromtext.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/stgeogfromtext.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/stgeogfromtext.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/stgeogfromtext.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/stgeogfromtext.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/stgeogfromtext.md

# Source: https://docs.pinot.apache.org/functions-1/stgeogfromtext.md

# ST\_GeogFromText

Return a specified geography value from [Well-Known Text representation or extended (WKT)](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry)

## Signature

> ST\_GeogFromText(wkt)

## Usage Examples

```sql
select ST_GeogFromText('POINT (30 10)') AS value
from ignoreMe 
```

| value                              |
| ---------------------------------- |
| 80403e0000000000004024000000000000 |

```sql
select ST_GeogFromText('LINESTRING (30 10, 10 30, 40 40)') AS value
from ignoreMe 
```

| value                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------- |
| 82000000010000000300000000403e00000000000040240000000000004024000000000000403e00000000000040440000000000004044000000000000 |

```sql
select ST_GeogFromText('POLYGON ((30 10, 40 40, 20 40, 10 20, 30 10))') AS value
from ignoreMe 
```

| value                                                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 84000000010000000500000000403e0000000000004024000000000000402400000000000040340000000000004034000000000000404400000000000040440000000000004044000000000000403e0000000000004024000000000000 |
