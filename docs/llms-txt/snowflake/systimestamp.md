# Source: https://docs.snowflake.com/en/sql-reference/functions/systimestamp.md

Categories:
:   [Context functions](../functions-context.md) (General)

# SYSTIMESTAMP

Returns the current timestamp for the system.

See also:
:   [CURRENT_TIMESTAMP](current_timestamp.md)

## Syntax

```sqlsyntax
SYSTIMESTAMP()
```

## Arguments

None. This function must be called with parentheses.

## Returns

Returns the current system time in the local time zone. The data type of the returned value is
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
SELECT SYSTIMESTAMP();
```

```output
+--------------------------+
| SYSTIMESTAMP()           |
|--------------------------|
| 2024-04-17 15:49:34.0800 |
+--------------------------+
```
