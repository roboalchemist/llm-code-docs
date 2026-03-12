# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/fromepoch.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/fromepoch.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/fromepoch.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/fromepoch.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/fromepoch.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/fromepoch.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/fromepoch.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/fromepoch.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/fromepoch.md

# Source: https://docs.pinot.apache.org/functions-1/fromepoch.md

# FromEpoch

Convert epoch to epoch milliseconds. The following time units are supported:

* SECONDS
* MINUTES
* HOURS
* DAYS

## Signature

> FromEpoch\<TIME\_UNIT>(timeIn\<Time\_UNIT>)

## Usage Examples

```sql
select FromEpochSeconds(1613472303) AS epochMillis
FROM ignoreMe
```

| epochMillis   |
| ------------- |
| 1613472303000 |

```sql
select FromEpochMinutes(26891205) AS epochMillis
FROM ignoreMe
```

| epochMillis   |
| ------------- |
| 1613472300000 |

```sql
select FromEpochHours(448186) AS epochMillis
FROM ignoreMe
```

| epochMillis   |
| ------------- |
| 1613469600000 |

```sql
select FromEpochDays(18674) AS epochMillis
FROM ignoreMe
```

| epochMillis   |
| ------------- |
| 1613433600000 |
