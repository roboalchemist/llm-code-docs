# Source: https://docs.oxla.com/sql-reference/sql-functions/timestamp-functions/timestamp-seconds.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# TIMESTAMP_SECONDS

## Overview

The `TIMESTAMP_SECONDS()` function converts a given UNIX timestamp value in seconds from 1970-01-01 00:00:00 UTC into a timestamp. Its syntax can be seen below:

```sql  theme={null}
SELECT TIMESTAMP_SECONDS(Int64)
```

Its input type is an `int64` expression representing a UNIX timestamp in seconds, and the return data type is a timestamp.

## Examples

### #Case 1: Basic `TIMESTAMP_SECONDS()` function

The below example uses the `TIMESTAMP_SECONDS()` function to convert a given UNIX timestamp in seconds into a timestamp:

```sql  theme={null}
SELECT TIMESTAMP_SECONDS(1671975000) AS timestamp_secondsvalue;
```

The final output will be as follows:

```sql  theme={null}
+-----------------------------+
| timestamp_secondsvalue      |
+-----------------------------+
| 2022-12-25 13:30:00         |
+-----------------------------+
```

### Case #2: `TIMESTAMP_SECONDS()` function using columns

Let's suppose we have a table named \*\*unix\_time \*\*with the following UNIX time values in seconds:

```sql  theme={null}
CREATE TABLE unix_time (
  unix_time int
);

INSERT INTO unix_time VALUES 
('982384720'),
('1671975000'),
('171472000');
```

```sql  theme={null}
SELECT * FROM unix_time;
```

The above query will show the following table:

```sql  theme={null}
+-------------+
| unix_time   | 
+-------------+
| 982384720   |
| 1671975000  |
| 171472000   |
+-------------+
```

We want to convert all UNIX timestamp values in seconds to timestamp values. To do that, we have to run the following query:

```sql  theme={null}
SELECT unix_time, TIMESTAMP_SECONDS(unix_time)
AS timestamp_value
FROM unix_time ;
```

The output displays all the entries in the table in UNIX timestamp format (in seconds) in the **unix\_time **column** **and in the timestamp format without timezone in the column** timestamp\_value**.

```sql  theme={null}
+-------------------------+-----------------------+
| unix_time               | timestamp_value       |
+-------------------------+-----------------------+
| 982384720               | 2001-02-17 04:38:40   |
| 1671975000              | 2022-12-25 13:30:00   |
| 171472000               | 1975-06-08 15:06:40   |
+-------------------------+-----------------------+
```
