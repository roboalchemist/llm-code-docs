# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/toepochbucket.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/toepochbucket.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/toepochbucket.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/toepochbucket.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/toepochbucket.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/toepochbucket.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/toepochbucket.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/toepochbucket.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/toepochbucket.md

# Source: https://docs.pinot.apache.org/functions-1/toepochbucket.md

# ToEpochBucket

Convert epoch milliseconds to epoch , and divided by bucket size (Bucket size is defined in ). The following time units are supported:

* SECONDS
* MINUTES
* HOURS
* DAYS

## Signature

> ToEpoch\<TIME\_UNIT>Bucket(timeInMillis, bucketSize)

## Usage Examples

```sql
select ToEpochSecondsBucket(1613472303000, 1000) AS bucket
FROM ignoreMe
```

| bucket  |
| ------- |
| 1613472 |

```sql
select ToEpochMinutesBucket(1613472303000, 10) AS bucket
FROM ignoreMe
```

| bucket  |
| ------- |
| 2689120 |

```sql
select ToEpochHoursBucket(1613472303000, 5) AS bucket
FROM ignoreMe
```

| bucket |
| ------ |
| 89637  |

```sql
select ToEpochDaysBucket(1613472303000, 10) AS bucket
FROM ignoreMe
```

| bucket |
| ------ |
| 1867   |
