# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/replace.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/replace.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/replace.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/replace.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/replace.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/replace.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/replace.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/replace.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/replace.md

# Source: https://docs.pinot.apache.org/functions-1/replace.md

# replace

replace all instances of `find` with `replace` in input

## Signature

> REPLACE(col, find, replace)

## Usage Examples

```sql
SELECT REPLACE('Hello, World', 'Hello', 'Goodbye') AS value
FROM ignoreMe
```

| value          |
| -------------- |
| Goodbye, World |

```sql
SELECT REPLACE('Hello, World', 'Hellow', 'Goodbye') AS value
FROM ignoreMe
```

| value        |
| ------------ |
| Hello, World |
