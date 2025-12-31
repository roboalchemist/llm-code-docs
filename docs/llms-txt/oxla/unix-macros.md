# Source: https://docs.oxla.com/sql-reference/sql-functions/timestamp-functions/unix-macros.md

# UNIX_MICROS

## Overview

The `UNIX_MICROS()` function returns a given timestamp into a UNIX timestamp in microseconds, from 1970-01-01 00:00:00-00 (can be negative). Its syntax is illustrated below:

```sql  theme={null}
SELECT UNIX_MICRO(TIMESTAMP)
```

Its input type is a TIMESTAMP expression, and the return data type is `BIGINT` representing time in microseconds.

## Examples

### Case #1: Basic `UNIX_MICROS()` function

The below example uses the `UNIX_MICROS()` function to convert a given timestamp into a UNIX timestamp in microseconds:

```sql  theme={null}
SELECT UNIX_MICRO(TIMESTAMP "2022-12-25 13:30:00+00") AS unix_microsvalues;
```

The final output will be as follows:

```sql  theme={null}
+-----------------------------+
| unix_microsvalues           |
+-----------------------------+
| 1671975000000000.000000     |
+-----------------------------+
```

### Case #2: `UNIX_MICROS()` function using columns

Let’s suppose we have a table named **time\_example** with the following timestamp values:

```sql  theme={null}
CREATE TABLE time_example (
  time_stamp timestamp
);

INSERT INTO time_example VALUES 
('2022-12-25 13:30:00'),
('2021-10-02 06:30:00'),
('2020-09-25 07:25:00');
```

```sql  theme={null}
SELECT * FROM time_example;
```

The above query will show the following table:

```sql  theme={null}
+-------------------------+
| time_example            | 
+-------------------------+
| 2022-12-25 13:30:00     |
| 2021-10-02 06:30:00     |
| 2020-09-25 07:25:00     |
+-------------------------+
```

We want to convert all timestamp values into UNIX timestamp values in microseconds. To do that, we have to run the following query:

```sql  theme={null}
SELECT time_stamp, UNIX_MICROS(time_stamp)
AS time_micros
FROM time_example;
```

The output displays all the timestamp entries in the **time\_stamp** column and the converted UNIX timestamps in microseconds in the column **time\_micros**.

```sql  theme={null}
+-------------------------+--------------------------+
| time_stamp               | time_micros              |
+-------------------------+--------------------------+
| 2022-12-25 13:30:00     | 1671975000000000.000000  |
| 2021-10-02 06:30:00     | 1633156200000000.000000  |
| 2020-09-25 07:25:00     | 1601018700000000.000000  |
+-------------------------+--------------------------+
```
