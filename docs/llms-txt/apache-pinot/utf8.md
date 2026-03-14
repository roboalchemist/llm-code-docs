# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/utf8.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/utf8.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/utf8.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/utf8.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/utf8.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/utf8.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/utf8.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/utf8.md

# Source: https://docs.pinot.apache.org/functions-1/utf8.md

# UTF8

* `fromUtf8` returns UTF8 encoded string of input binary data (`bytes` type).
* `toUtf8` returns binary data (represented as a Hex string) from a UTF8 encoded string.

## Signature

> fromUtf8(bytesCol)
>
> toUtf8(string)

## Usage Examples

```sql
SELECT bytesCol1, fromUtf8(bytesCol1) AS utf8Str
FROM testTable
LIMIT 1
```

| bytesCol1    | utf8Str |
| ------------ | ------- |
| 68656c6c6f21 | hello!  |

```sql
SELECT toUtf8('hello!') AS binaryOutput
FROM ignoreMe
```

| binaryOutput |
| ------------ |
| 68656c6c6f21 |
