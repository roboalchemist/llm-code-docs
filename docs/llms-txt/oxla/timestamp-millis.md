# Source: https://docs.oxla.com/sql-reference/sql-functions/timestamp-functions/timestamp-millis.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# TIMESTAMP_MILLIS

## Overview

The `TIMESTAMP_MILLIS()` function converts a given UNIX timestamp value in milliseconds since 1970-01-01 00:00:00 UTC into a timestamp. Its syntax can be seen below:

```sql  theme={null}
SELECT TIMESTAMP_MILLIS(BIGINT)
```

Its input type is a `BIGINT` expression which represents a UNIX timestamp in milliseconds and the return data type is a timestamp.

## Examples

### Case #1: Basic `TIMESTAMP_MILLIS()` function

The below example uses the `TIMESTAMP_MILLIS()` function to convert a given UNIX timestamp in milliseconds into a timestamp without a timezone.

```sql  theme={null}
SELECT TIMESTAMP_MILLIS(1671975000000) AS timestamp_millisvalues;
```

The final output will be as follows:

```sql  theme={null}
+-----------------------------+
| timestamp_millisvalues      |
+-----------------------------+
| 2022-12-25 13:30:00         |
+-----------------------------+
```

### Case #2: `TIMESTAMP_MILLIS()` function using columns

Let's suppose we have a table named \*\*unix\_example \*\*with the following UNIX time values in milliseconds in the **unix\_timestamp** column:

```sql  theme={null}
CREATE TABLE unix_example (
  unix_timestamp long
);

INSERT INTO unix_timestamp VALUES 
('171472000000'),
('1671975000000'),
('153276000000');
```

```sql  theme={null}
SELECT * FROM unix_example;
```

The above query will show the following table:

```sql  theme={null}
+----------------+
| unix_timestamp | 
+----------------+
| 171472000000   |
| 1671975000000  |
| 153276000000   |
+----------------+
```

We want to convert all UNIX timestamp values in milliseconds to timestamp values. To do that, we have to run the following query:

```sql  theme={null}
SELECT unix_timestamp, TIMESTAMP_MILLIS(unix_timestamp)
AS timestamp_value
FROM unix_example;
```

The output displays all the entries in the table in UNIX timestamp format (in milliseconds) in the **unix\_timestamp **column and in the timestamp format in the column** timestamp\_value** without timezone.

```sql  theme={null}
+-------------------------+-----------------------+
| unix_timestamp          | timestamp_value       |
+-------------------------+-----------------------+
|171472000000             | 1975-06-08 15:06:40   |
|1671975000000            | 2022-12-25 13:30:00   |
|153276000000             | 1974-11-10 00:40:00   |
+-------------------------+-----------------------+
```
