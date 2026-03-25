# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/round.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/round.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/round.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/round.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/round.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/round.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/round.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/round.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/round.md

# Source: https://docs.pinot.apache.org/functions-1/round.md

# round

Round the given time value to nearest bucket start value.

## Signature

> round(timeValue, bucketSize)

## Usage Examples

Round seconds epoch value to the start value of the 30 seconds bucket to which it belongs.

```sql
select round(1639144274, 30) AS rounded
FROM ignoreMe
```

| rounded    |
| ---------- |
| 1639144260 |

Round milliseconds epoch value to the start value of the 5,000 milliseconds bucket to which it belongs.

```sql
select round(1639144274000, 5000) AS rounded
FROM ignoreMe
```

| rounded       |
| ------------- |
| 1639144270000 |
