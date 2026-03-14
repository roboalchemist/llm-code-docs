# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/regexpextract.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/regexpextract.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/regexpextract.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/regexpextract.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/regexpextract.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/regexpextract.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/regexpextract.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/regexpextract.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/regexpextract.md

# Source: https://docs.pinot.apache.org/functions-1/regexpextract.md

# regexpExtract

Extracts values that match the provided regular expression

## Signature

> regexpExtract(value, regexp)
>
> regexpExtract(value, regexp, group)
>
> regexpExtract(value, regexp, group, defaultValue)

## Usage Examples

```sql
select regexpExtract('foo', '.*') AS value
from ignoreMe
```

| value |
| ----- |
| foo   |

```sql
select regexpExtract('foo123', '[0-9]+') AS value
from ignoreMe
```

| value |
| ----- |
| 123   |

```sql
select regexpExtract('foo123', '[^0-9]+') AS value
from ignoreMe
```

| value |
| ----- |
| foo   |

```sql
select regexpExtract('foo bar baz', '(\w+) (\w+)', 0) AS value
from ignoreMe
```

| value   |
| ------- |
| foo bar |

```sql
select regexpExtract('foo bar baz', '(\w+) (\w+)', 2) AS value
from ignoreMe
```

| value |
| ----- |
| bar   |

```sql
select regexpExtract('foo123', 'bar', 0, 'defaultValue') AS value
from ignoreMe
```

| value        |
| ------------ |
| defaultValue |
