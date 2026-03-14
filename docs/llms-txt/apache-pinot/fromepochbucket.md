# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/fromepochbucket.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/fromepochbucket.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/fromepochbucket.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/fromepochbucket.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/fromepochbucket.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/fromepochbucket.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/fromepochbucket.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/fromepochbucket.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/fromepochbucket.md

# Source: https://docs.pinot.apache.org/functions-1/fromepochbucket.md

# FromEpochBucket

Convert epoch to epoch milliseconds. e.g. 10 seconds since epoch or 5 minutes since Epoch. The following time units are supported:

* SECONDS
* MINUTES
* HOURS
* DAYS

## Signature

> FromEpoch\<TIME\_UNIT>Bucket(timeInMillis, bucketSize)

## Usage Examples

```sql
select FromEpochSecondsBucket(1613472303, 1) AS bucket
FROM ignoreMe
```

| bucket        |
| ------------- |
| 1613472303000 |

```sql
select FromEpochSecondsBucket(1613472303, 2) AS bucket
FROM ignoreMe
```

| bucket        |
| ------------- |
| 3226944606000 |

```sql
select FromEpochMinutesBucket(2689120, 10) AS bucket
FROM ignoreMe
```

| bucket        |
| ------------- |
| 1613472000000 |

```sql
select FromEpochHoursBucket(89637, 5) AS bucket
FROM ignoreMe
```

| bucket        |
| ------------- |
| 1613466000000 |

```sql
select FromEpochDaysBucket(1867, 10) AS bucket
FROM ignoreMe
```

| bucket        |
| ------------- |
| 1613088000000 |
