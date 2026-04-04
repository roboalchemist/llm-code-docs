# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/firstwithtime.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/firstwithtime.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/firstwithtime.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/firstwithtime.md

# Source: https://docs.pinot.apache.org/functions-1/firstwithtime.md

# FIRSTWITHTIME

Returns the value of `dataColumn` with the smallest `timeColumn` value where:

* `timeColumn` is used to define the time of `dataColumn`, which can be of type `TIMESTAMP`, `INT`, `LONG`
* `dataType` specifies the type for `dataColumn`, which can be `BOOLEAN`, `INT`, `LONG`, `FLOAT`, `DOUBLE`, `STRING`

## Signature

> FIRSTWITHTIME(dataColumn, timeColumn, 'dataType')

## Example

This example is based on the [Streaming Quick Start](https://docs.pinot.apache.org/basics/getting-started/quick-start#streaming).

```sql
select FIRSTWITHTIME(group_name, __metadata$recordTimestamp, 'STRING')
from meetupRsvp 
```

| value                 |
| --------------------- |
| group\_name1016303453 |
