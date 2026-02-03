# Source: https://docs.oxla.com/sql-reference/sql-functions/timestamp-functions/unix-millis.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# UNIX_MILLIS

## Overview

The `UNIX_MILLIS()` function returns a given timestamp to a UNIX timestamp in milliseconds from 1970-01-01 00:00:00-00 (can be negative). Its syntax is illustrated below:

```sql  theme={null}
SELECT UNIX_MILLIS(TIMESTAMP)
```

Its input type is a TIMESTAMP expression, and the return data type is `BIGINT` representing time in milliseconds.

## Examples

### Case #1: Basic `UNIX_MILLIS()` function

The below example uses the `UNIX_MILLIS()` function to convert a given timestamp into a UNIX timestamp in milliseconds:

```sql  theme={null}
SELECT UNIX_MILLIS(TIMESTAMP "1996-5-02 7:15:00+00") AS unix_millisvalues;
```

The final output will be as follows:

```sql  theme={null}
+-----------------------------+
| unix_millisvalues           |
+-----------------------------+
| 831021300000.000000         |
+-----------------------------+
```

### Case #2: `UNIX_MILLIS()` function using columns

Let’s suppose we have a table named **time\_example **with the following timestamp values in the** time\_stamp** column:

```sql  theme={null}
CREATE TABLE time_example (
  time_stamp timestamp
);

INSERT INTO time_example VALUES 
('2004-07-23 11:30:00+00'),
('2011-02-12 04:45:00+00'),
('1975-08-03 07:50:00+00');
```

```sql  theme={null}
SELECT * FROM time_example;
```

The above query will show the following table:

```sql  theme={null}
+-------------------------+
| time_example            | 
+-------------------------+
| 2004-07-23 11:30:00     |
| 2011-02-12 04:45:00     |
| 1975-08-03 07:50:00     |
+-------------------------+
```

We want to convert all timestamp values into UNIX timestamp values in milliseconds. To do that, we have to run the following query:

```sql  theme={null}
SELECT time_stamp, UNIX_MILLIS(time_stamp) AS time_millis FROM time_example;
```

The output displays all the timestamp entries of the table in the \*\*time\_stamp \*\*column and the converted UNIX milliseconds timestamp entries in the column **time\_millis**.

```sql  theme={null}
+-------------------------+-----------------------+
| time_stamp              | time_millis           |
+-------------------------+-----------------------+
| 2004-07-23 11:30:00     | 1090582200000.000000  |
| 2011-02-12 04:45:00     | 1297485900000.000000  |
| 1975-08-03 07:50:00     | 176284200000.000000   |
+-------------------------+-----------------------+
```
