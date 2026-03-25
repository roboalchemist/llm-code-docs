# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/sha.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/sha.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/sha.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/sha.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/sha.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/sha.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/sha.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/sha.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/sha.md

# Source: https://docs.pinot.apache.org/functions-1/sha.md

# sha

Return SHA-1 digest of binary column(`bytes` type) as hex string

## Signature

> SHA(bytesCol)

## Usage Examples

These examples are based on the [Real time Quick Start](https://docs.pinot.apache.org/basics/getting-started/quick-start#realtime).

```sql
select event_id, location, SHA(location) AS hash
from meetupRsvp 
limit 1
```

| event\_id | location                           | hash                                     |
| --------- | ---------------------------------- | ---------------------------------------- |
| 282776561 | 80406178a3d70a3d714041d5c28f5c28f6 | b914583284ac29d2bd3c9d097245b031d99d687d |

{% hint style="info" %}
The row returned will be different if you run this example as the data is ingested in real-time.
{% endhint %}
