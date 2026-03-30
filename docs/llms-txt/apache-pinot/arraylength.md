# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/arraylength.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/arraylength.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/arraylength.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/arraylength.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/arraylength.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/arraylength.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/arraylength.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/arraylength.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/arraylength.md

# Source: https://docs.pinot.apache.org/functions-1/arraylength.md

# ARRAYLENGTH

Returns the length of a multi-value column

## Signature

> ARRAYLENGTH('colName')

## Usage Examples

These examples are based on the [Hybrid Quick Start](https://docs.pinot.apache.org/basics/getting-started/quick-start#hybrid).

```sql
select ARRAYLENGTH(RandomAirports) AS length, count(*) 
from airlineStats 
GROUP BY length
ORDER BY count(*) DESC
LIMIT 5
```

| length | count(\*) |
| ------ | --------- |
| 1      | 5382      |
| 37     | 267       |
| 33     | 223       |
| 17     | 166       |
| 22     | 160       |

{% hint style="info" %}
The `count(*)` values will increase each time we execute the query as data is constantly being ingested by the Hybrid Quick Start.
{% endhint %}
