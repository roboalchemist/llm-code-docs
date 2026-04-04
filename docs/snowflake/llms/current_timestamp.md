# Source: https://docs.snowflake.com/en/sql-reference/functions/current_timestamp.md

Categories:
:   [Context functions](../functions-context.md) (General)

# CURRENT_TIMESTAMP

Returns the current timestamp for the system in the local time zone.

Aliases:
:   [LOCALTIMESTAMP](localtimestamp.md) , [GETDATE](getdate.md) , [SYSTIMESTAMP](systimestamp.md)

## Syntax

```sqlsyntax
CURRENT_TIMESTAMP( [ <fract_sec_precision> ] )

CURRENT_TIMESTAMP
```

## Arguments

`fract_sec_precision`
:   This optional argument indicates the precision with which to report the
    time. For example, a value of 3 says to use 3 digits after the decimal
    point (that is, to specify the time with a precision of milliseconds).

    The default precision is 9 (nanoseconds).

    Valid values range from 0 - 9. However, most platforms do not support true
    nanosecond precision; the precision that you get might be less than the
    precision you specify. In practice, precision is usually approximately
    milliseconds (3 digits) at most.

    > **Note:**
    >
    > Fractional seconds are only displayed if they have been explicitly set in the [TIMESTAMP_OUTPUT_FORMAT](../parameters.md) parameter for the session (e.g. `'YYYY-MM-DD HH24:MI:SS.FF'`).

## Returns

Returns the current system time. The data type of the returned value is
[TIMESTAMP_LTZ](../data-types-datetime.md).

## Usage notes

* The setting of the [TIMEZONE](../parameters.md) parameter affects the return value. The returned timestamp is in the time zone for the session.
* The setting of the [TIMESTAMP_TYPE_MAPPING](../parameters.md) parameter does not affect the return value.
* Do not use the returned value for precise time ordering between concurrent queries (processed by the same virtual warehouse) because the queries might be serviced by different compute resources (in the warehouse).

* To comply with the ANSI standard, this function can be called without parentheses in SQL statements.

  However, if you are setting a [Snowflake Scripting variable](../../developer-guide/snowflake-scripting/variables.md)
  to an expression that calls the function (for example, `my_var := CURRENT_TIMESTAMP();`), you must include the
  parentheses. For more information, see [the usage notes for context functions](../functions-context.md).
* The aliases SYSTIMESTAMP and GETDATE differ from CURRENT_TIMESTAMP in the following ways:

  * They do not support the `fract_sec_precision` argument.
  * These functions must be called with parentheses.

## Examples

The examples in this section use the timestamp output format `YYYY-MM-DD HH24:MI:SS.FF`. To configure
your session to use the same output format, run the following statement:

```sqlexample
ALTER SESSION SET TIMESTAMP_OUTPUT_FORMAT = 'YYYY-MM-DD HH24:MI:SS.FF';
```

### Call the CURRENT_TIMESTAMP function with different precision values

Return the current timestamp with fractional seconds precision set to `2`:

```sqlexample
SELECT CURRENT_TIMESTAMP(2);
```

```output
+------------------------+
| CURRENT_TIMESTAMP(2)   |
|------------------------|
| 2024-04-17 15:41:38.29 |
+------------------------+
```

Return the current timestamp with fractional seconds precision set to `4`:

```sqlexample
SELECT CURRENT_TIMESTAMP(4);
```

```output
+--------------------------+
| CURRENT_TIMESTAMP(4)     |
|--------------------------|
| 2024-04-17 15:42:14.2100 |
+--------------------------+
```

Return the current timestamp with fractional seconds precision set to the default (`9`):

```sqlexample
SELECT CURRENT_TIMESTAMP;
```

```output
+-------------------------------+
| CURRENT_TIMESTAMP             |
|-------------------------------|
| 2024-04-17 15:42:55.130000000 |
+-------------------------------+
```

### Call the CURRENT_TIMESTAMP function with different TIMEZONE settings

Set the [TIMEZONE](../parameters.md) parameter to `America/New_York` and call the CURRENT_TIMESTAMP function:

```sqlexample
ALTER SESSION SET TIMEZONE = 'America/New_York';

SELECT CURRENT_TIMESTAMP(2);
```

```output
+------------------------+
| CURRENT_TIMESTAMP(2)   |
|------------------------|
| 2025-08-11 14:16:43.57 |
+------------------------+
```

Set the TIMEZONE parameter to `America/Los_Angeles` and call the CURRENT_TIMESTAMP function:

```sqlexample
ALTER SESSION SET TIMEZONE = 'America/Los_Angeles';

SELECT CURRENT_TIMESTAMP(2);
```

```output
+------------------------+
| CURRENT_TIMESTAMP(2)   |
|------------------------|
| 2025-08-11 11:17:18.19 |
+------------------------+
```
