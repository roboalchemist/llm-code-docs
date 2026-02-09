# Source: https://docs.oxla.com/sql-reference/sql-functions/timestamp-functions/extract.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# EXTRACT

## Overview

The `EXTRACT()` function retrieves a specified part (field) from a given date/time or interval value.
It is commonly used to obtain components such as year, month, day, hour, etc., from timestamps or dates.

## Syntax

```sql  theme={null}
EXTRACT (field FROM source)
```

## Parameters

* `field`: string or identifier specifying the part of the date / time to extract
* `source`: date / time value from which to extract the specifed field

The table below shows the supported input and corresponding return types for the `EXTRACT()` function:

| Input Type: `source` | Supported `field` values                           | Return Type        |
| -------------------- | -------------------------------------------------- | ------------------ |
| `TIMESTAMP`          | `YEAR`, `MONTH`, `DAY`, `HOUR`, `MINUTE`, `SECOND` | `DOUBLE PRECISION` |
| `TIMESTAMPTZ`        | `YEAR`, `MONTH`, `DAY`, `HOUR`, `MINUTE`, `SECOND` | `DOUBLE PRECISION` |
| `DATE`               | `YEAR`, `MONTH`, `DAY`                             | `INTEGER`          |

<Note>
  The SECOND field returns a fractional value as DOUBLE PRECISION to include fractional seconds, not an integer type
</Note>

## Examples

### EXTRACT() with Timestamp - Year

The below example uses the `EXTRACT()` function to extract a given timestamp’s **YEAR**:

```sql  theme={null}
SELECT EXTRACT(YEAR FROM TIMESTAMP '2025-12-31 13:30:15.123456');
```

The final output will be as follows:

```sql  theme={null}
+----------+
| extract  |
+----------+
| 2025     |
+----------+
```

### EXTRACT() with Timestamp - Month

Here we will use the `EXTRACT()` function to extract a given timestamp’s **MONTH:**

```sql  theme={null}
SELECT EXTRACT(MONTH FROM TIMESTAMP '2025-12-31 13:30:15.123456');
```

The final output will take the month’s part of a given timestamp:

```sql  theme={null}
+----------+
| extract  |
+----------+
| 12       |
+----------+
```

### EXTRACT() with Timestamp - Seconds (including fractional seconds)

Here we will use the `EXTRACT()` function to extract a given timestamp's **SECONDS**:

```sql  theme={null}
SELECT EXTRACT(SECOND FROM TIMESTAMP '2025-12-31 13:30:15.123456');
```

The final output will take the seconds' part of a given timestamp:

```sql  theme={null}
+----------+
| extract  |
+----------+
| 15.123456|
+----------+
```
