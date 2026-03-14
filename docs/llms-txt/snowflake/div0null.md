# Source: https://docs.snowflake.com/en/sql-reference/functions/div0null.md

Categories:
:   [Numeric functions](../functions-numeric.md)

# DIV0NULL

Performs division like the division operator (`/`), but returns 0 when the divisor is 0 or NULL (rather than reporting an
error or returning NULL).

See also:
:   [DIV0](div0.md)

## Syntax

```sqlsyntax
DIV0NULL( <dividend> , <divisor> )
```

## Arguments

`dividend`
:   Numeric expression that evaluates to the value that you want to divide.

`divisor`
:   Numeric expression that evaluates to the value that you want to divide by.

## Returns

The quotient. If the divisor is 0 or NULL, the function returns 0.

## Examples

As shown in the following example, the DIV0NULL function performs division like the division operator (`/`):

```sqlexample
SELECT 1/2;

+----------+
|      1/2 |
|----------|
| 0.500000 |
+----------+
```

```sqlexample
SELECT DIV0NULL(1, 2);

+----------------+
| DIV0NULL(1, 2) |
|----------------|
|       0.500000 |
+----------------+
```

Unlike the division operator, DIV0NULL returns a 0 (rather than reporting an error or returning NULL) when the divisor is 0 or
NULL.

```sqlexample
SELECT 1/0;
100051 (22012): Division by zero
```

```sqlexample
SELECT DIV0NULL(1, 0);

+----------------+
| DIV0NULL(1, 0) |
|----------------|
|       0.000000 |
+----------------+
```

```sqlexample
SELECT 1/NULL;

+--------+
| 1/NULL |
|--------|
|   NULL |
+--------+
```

```sqlexample
SELECT DIV0NULL(1, NULL);

+-------------------+
| DIV0NULL(1, NULL) |
|-------------------|
|          0.000000 |
+-------------------+
```
