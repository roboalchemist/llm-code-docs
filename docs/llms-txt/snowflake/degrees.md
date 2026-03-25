# Source: https://docs.snowflake.com/en/sql-reference/functions/degrees.md

Categories:
:   [Numeric functions](../functions-numeric.md) (Trigonometric)

# DEGREES

Converts radians to degrees.

## Syntax

```sqlsyntax
DEGREES( <input_expr> )
```

## Arguments

`input_expr`
:   The value or expression to operate on. The data type must be FLOAT.

## Returns

This function returns a value of type FLOAT.

## Examples

Show the number of degrees for 1/3 of a radian, 1 radian, and 3 radians:

```sqlexample
SELECT DEGREES(PI()/3), DEGREES(PI()), DEGREES(3 * PI()), DEGREES(1);
```

```output
+-----------------+---------------+-------------------+--------------+
| DEGREES(PI()/3) | DEGREES(PI()) | DEGREES(3 * PI()) |   DEGREES(1) |
|-----------------+---------------+-------------------+--------------|
|              60 |           180 |               540 | 57.295779513 |
+-----------------+---------------+-------------------+--------------+
```
