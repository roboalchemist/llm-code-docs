# Source: https://docs.snowflake.com/en/sql-reference/functions/try_to_boolean.md

Categories:
:   [Conversion functions](../functions-conversion.md)

# TRY_TO_BOOLEAN

A special version of [TO_BOOLEAN](to_boolean.md) that performs the same operation
(that is, converts an input expression to a Boolean value), but with error-handling
support. If the conversion can’t be performed, TRY_TO_BOOLEAN returns a NULL value
instead of raising an error.

For more information, see [Error-handling conversion functions](../functions-conversion.md).

## Syntax

```sqlsyntax
TRY_TO_BOOLEAN( <string_expr> )
```

## Arguments

`string_expr`
:   A string expression that can be evaluated to a BOOLEAN value.

## Returns

This function returns a value of type [BOOLEAN](../data-types-logical.md).

## Usage notes

The input argument must be a string expression. The function evaluates the string expression
in the following way:

* `'true'`, `'t'`, `'yes'`, `'y'`, `'on'`, `'1'` return TRUE.
* `'false'`, `'f'`, `'no'`, `'n'`, `'off'`, `'0'` return FALSE.
* All other strings return NULL.

The evaluations of the strings are case-insensitive.

## Examples

This example uses the TRY_TO_BOOLEAN function:

```sqlexample
SELECT TRY_TO_BOOLEAN('True')  AS "T",
       TRY_TO_BOOLEAN('False') AS "F",
       TRY_TO_BOOLEAN('Not valid')  AS "N";
```

```output
+------+-------+------+
| T    | F     | N    |
|------+-------+------|
| True | False | NULL |
+------+-------+------+
```

For more examples, see [TO_BOOLEAN](to_boolean.md).
