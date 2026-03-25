# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/remove.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/remove.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/remove.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/remove.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/remove.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/remove.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/remove.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/remove.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/remove.md

# Source: https://docs.pinot.apache.org/functions-1/remove.md

# remove

Removes all instances of search from string

## Signature

> remove(input, search)

## Usage Examples

```sql
select remove('foo bar foo sheep', 'foo') AS value
from ignoreMe
```

| value     |
| --------- |
| bar sheep |
