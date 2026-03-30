# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/ago.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/ago.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/ago.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/ago.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/ago.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/ago.md

# Source: https://docs.pinot.apache.org/functions-1/ago.md

# ago

Return time as epoch millis before the given period in ISO-8601 duration format (PnDTnHnMn.nS with days considered to be exactly 24 hours).

Examples:

* "PT20.345S" -- parses as "20.345 seconds"
* "PT15M" -- parses as "15 minutes" (where a minute is 60 seconds)
* "PT10H" -- parses as "10 hours" (where an hour is 3600 seconds)
* "P2D" -- parses as "2 days" (where a day is 24 hours or 86400 seconds)
* "P2DT3H4M" -- parses as "2 days, 3 hours and 4 minutes"
* "P-6H3M" -- parses as "-6 hours and +3 minutes"
* "-P6H3M" -- parses as "-6 hours and -3 minutes"
* "-P-6H+3M" -- parses as "+6 hours and -3 minutes"

## Signature

> ago()

## Usage Examples

```sql
select ago('P1D') AS oneDayAgo
FROM ignoreMe
```

| oneDayAgo     |
| ------------- |
| 1639150454255 |

This function is typically used in the predicate to filter on timestamps for recent data. e.g. filter data on recent 1 day.

```sql
SELECT * 
FROM tableName
WHERE tsInMillis > ago('P1D')
```
