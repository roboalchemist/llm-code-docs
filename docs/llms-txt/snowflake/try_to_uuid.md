# Source: https://docs.snowflake.com/en/sql-reference/functions/try_to_uuid.md

Categories:
:   [Conversion functions](../functions-conversion.md)

# TRY_TO_UUID

A special version of [TO_UUID](to_uuid.md) that performs the same operation
— that is, converts an input expression to a [UUID](../data-types-uuid.md) value —
but with error handling support. If the conversion can’t be performed, it returns a NULL value
instead of raising an error.

For more information, see the following topics:

* [Error-handling conversion functions](../functions-conversion.md)
* [TO_UUID](to_uuid.md)

## Syntax

```sqlsyntax
TRY_TO_UUID( <string_expr> )
```

## Arguments

`string_expr`
:   A string expression in UUID format.

## Returns

Returns a value of type [UUID](../data-types-uuid.md) or NULL when
TO_UUID would return an error.

## Examples

The following example returns NULL because the input string isn’t a UUID:

```sqlexample
SELECT TRY_TO_UUID('not a uuid');
```

```output
+--------------------------------------+
| TRY_TO_UUID('NOT A UUID')            |
|--------------------------------------|
| NULL                                 |
+--------------------------------------+
```

For examples that convert an input expression to a UUID value, see [TO_UUID](to_uuid.md).
