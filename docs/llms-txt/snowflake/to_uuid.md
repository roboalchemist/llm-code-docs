# Source: https://docs.snowflake.com/en/sql-reference/functions/to_uuid.md

Categories:
:   [Conversion functions](../functions-conversion.md)

# TO_UUID

Converts the input expression to a [UUID](../data-types-uuid.md) value.

See also:

* [TRY_TO_UUID](try_to_uuid.md)

## Syntax

```sqlsyntax
TO_UUID( <string_expr> )
```

## Arguments

`string_expr`
:   A string expression in UUID format.

## Returns

The return type is [UUID](../data-types-uuid.md).

For NULL input, the output is NULL.

## Examples

The following example converts a string to a UUID value:

```sqlexample
SELECT TO_UUID('c73d9175-0a1d-48c6-8d30-df165461328b');
```

```output
+-------------------------------------------------+
| TO_UUID('C73D9175-0A1D-48C6-8D30-DF165461328B') |
|-------------------------------------------------|
| c73d9175-0a1d-48c6-8d30-df165461328b            |
+-------------------------------------------------+
```
