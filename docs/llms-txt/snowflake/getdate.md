# Source: https://docs.snowflake.com/en/sql-reference/functions/getdate.md

Categories:
:   [Context functions](../functions-context.md) (General)

# GETDATE

Returns the current timestamp for the system in the local time zone.

Alias for [CURRENT_TIMESTAMP](current_timestamp.md).

## Syntax

```sqlsyntax
GETDATE()
```

## Arguments

None. This function must be called with parentheses.

## Returns

Returns the current system time. The data type of the returned value is
[TIMESTAMP_LTZ](../data-types-datetime.md).

## Usage notes

* The setting of the [TIMEZONE](../parameters.md) parameter affects the return value. The returned timestamp is in the time zone for the session.
* The setting of the [TIMESTAMP_TYPE_MAPPING](../parameters.md) parameter does not affect the return value.
* Do not use the returned value for precise time ordering between concurrent queries (processed by the same virtual warehouse) because the queries might be serviced by different compute resources (in the warehouse).

* This function does not support the `fract_sec_precision` argument that is supported by
  the [CURRENT_TIMESTAMP](current_timestamp.md) function.

## Examples

Show the current system timestamp:

```sqlexample
SELECT GETDATE();
```

```output
+-------------------------------+
| GETDATE()                     |
|-------------------------------|
| 2024-04-17 15:44:20.960000000 |
+-------------------------------+
```
