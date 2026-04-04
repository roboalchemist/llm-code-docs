# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/toepoch.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/toepoch.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/toepoch.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/toepoch.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/toepoch.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/toepoch.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/toepoch.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/toepoch.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/toepoch.md

# Source: https://docs.pinot.apache.org/functions-1/toepoch.md

# ToEpoch

Convert epoch milliseconds to epoch . The following time units are supported:

* SECONDS
* MINUTES
* HOURS
* DAYS

## Signature

> ToEpoch\<TIME\_UNIT>(timeInMillis)

## Usage Examples

```sql
select ToEpochSeconds(1613472303000) AS epochSeconds
FROM ignoreMe
```

| epochSeconds |
| ------------ |
| 1613472303   |

```sql
select ToEpochMinutes(1613472303000) AS epochMins
FROM ignoreMe
```

| epochMins |
| --------- |
| 26891205  |

```sql
select ToEpochHours(1613472303000) AS epochHours
FROM ignoreMe
```

| epochHours |
| ---------- |
| 448186     |

```sql
select ToEpochDays(1613472303000) AS epochDays
FROM ignoreMe
```

| epochDays |
| --------- |
| 18674     |
