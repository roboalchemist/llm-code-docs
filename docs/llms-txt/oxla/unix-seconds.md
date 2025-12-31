# Source: https://docs.oxla.com/sql-reference/sql-functions/timestamp-functions/unix-seconds.md

# UNIX_SECONDS

## Overview

The `UNIX_SECONDS()` function returns a given timestamp to a UNIX timestamp in seconds, from 1970-01-01 00:00:00-00. Its syntax is illustrated below:

```sql  theme={null}
SELECT UNIX_SECONDS(TIMESTAMP)
```

Its input type is a TIMESTAMP expression, and the return data type is `BIGINT` representing time in seconds.

## Examples

### Case #1: Basic `UNIX_SECONDS()` function

The below example uses the `UNIX_SECONDS()` function to convert a given timestamp into a UNIX timestamp in seconds:

```sql  theme={null}
SELECT UNIX_SECONDS(TIMESTAMP "2008-12-25 15:30:00+00") AS unix_secondsvalues;
```

The final output will be as follows:

```sql  theme={null}
+-----------------------------+
| unix_secondsvalues          |
+-----------------------------+
| 1230219000.000000           |
+-----------------------------+
```

### Case #2: `UNIX_SECONDS()` function using columns

Let’s suppose we have a table named \*\*time\_example \*\*with the following timestamp values in the **time\_stampvalues** column:

```sql  theme={null}
CREATE TABLE time_example (
  time_stampvalues timestamp
);

INSERT INTO time_example VALUES 
('2022-12-25 13:30:00'),
('2020-09-25 07:25:00'),
('2008-12-25 15:30:00'),
('2021-10-02 06:30:00');
```

```sql  theme={null}
SELECT * FROM time_example;
```

The above query will return the following table:

```sql  theme={null}
+-------------------------+
| time_stampvalues        | 
+-------------------------+
| 2022-12-25 13:30:00     |
| 2020-09-25 07:25:00     |
| 2008-12-25 15:30:00     |
| 2021-10-02 06:30:00     | 
+-------------------------+
```

1. We want to convert all timestamp values into UNIX timestamp values in seconds. To do that, we have to run the following query:

```sql  theme={null}
SELECT time_stampvalues, UNIX_SECONDS(time_stampvalues)
AS time_secondsvalues
FROM time_example;
```

2. The output displays all the timestamp entries of the table in the **time\_stampvalues** column and the converted UNIX seconds timestamp entries in the column **time\_secondsvalues**.

```sql  theme={null}
+-------------------------+-----------------------+
| time_stampvalues        | time_secondsvalues    |
+-------------------------+-----------------------+
| 2022-12-25 13:30:00     | 1671975000.000000     |
| 2020-09-25 07:25:00     | 1601018700.000000     |
| 2008-12-25 15:30:00     | 1230219000.000000     |
| 2021-10-02 06:30:00     | 1633156200.000000     |
+-------------------------+-----------------------+
```
