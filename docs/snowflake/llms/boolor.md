# Source: https://docs.snowflake.com/en/sql-reference/functions/boolor.md

Categories:
:   [Conditional expression functions](../expressions-conditional.md)

# BOOLOR

Computes the Boolean OR of two numeric expressions. In accordance with Boolean semantics:

* Non-zero values, including negative numbers, are regarded as true.
* Zero values are regarded as false.

As a result, the function returns:

* `True` if both expressions are non-zero or one expression is non-zero and the other expression is zero or NULL.
* `False` if both expressions are zero.
* `NULL` if both expressions are NULL or one expression is NULL and the other expression is zero.

See also:
:   [BOOLAND](booland.md) , [BOOLNOT](boolnot.md) , [BOOLXOR](boolxor.md)

## Syntax

```sqlsyntax
BOOLOR( <expr1> , <expr2> )
```

## Arguments

`expr1`
:   A numeric expression.

`expr2`
:   A numeric expression.

## Returns

This function returns a value of type BOOLEAN or NULL.

## Usage notes

This function rounds [floating-point numbers](../data-types-numeric.md).
Therefore, it might return unexpected results when it rounds non-zero floating-point numbers
to zero.

For examples of this behavior and workarounds, see Compute Boolean OR results for floating-point numbers.

## Examples

The following examples use the BOOLOR function.

### Compute Boolean OR results for integers and NULL values

The following query computes Boolean OR results for integers and NULL values:

```sqlexample
SELECT BOOLOR(1, 2),
       BOOLOR(0, 2),
       BOOLOR(3, NULL),
       BOOLOR(0, 0),
       BOOLOR(NULL, 0),
       BOOLOR(NULL, NULL);
```

```output
+--------------+--------------+-----------------+--------------+-----------------+--------------------+
| BOOLOR(1, 2) | BOOLOR(0, 2) | BOOLOR(3, NULL) | BOOLOR(0, 0) | BOOLOR(NULL, 0) | BOOLOR(NULL, NULL) |
|--------------+--------------+-----------------+--------------+-----------------+--------------------|
| True         | True         | True            | False        | NULL            | NULL               |
+--------------+--------------+-----------------+--------------+-----------------+--------------------+
```

### Compute Boolean OR results for floating-point numbers

The following examples demonstrate how the function might return unexpected results for floating-point
numbers that round to zero.

For the following queries, a result of `True` might be expected for the following function calls, but they return
`False` because the function rounds non-zero floating-point values to zero:

```sqlexample
SELECT BOOLOR(0.4, 0.3);
```

```output
+------------------+
| BOOLOR(0.4, 0.3) |
|------------------|
| False            |
+------------------+
```

```sqlexample
SELECT BOOLOR(-0.4, 0.3);
```

```output
+-------------------+
| BOOLOR(-0.4, 0.3) |
|-------------------|
| False             |
+-------------------+
```

For the following queries, a result of `True` might be expected for the following function calls, but they return
`NULL`:

```sqlexample
SELECT BOOLOR(0.4, NULL);
```

```output
+-------------------+
| BOOLOR(0.4, NULL) |
|-------------------|
| NULL              |
+-------------------+
```

```sqlexample
SELECT BOOLOR(-0.4, NULL);
```

```output
+--------------------+
| BOOLOR(-0.4, NULL) |
|--------------------|
| NULL               |
+--------------------+
```

If required, you can work around this rounding behavior for floating-point values by using the
[OR logical operator](../operators-logical.md) instead of the function. For example,
the following query returns `True`:

```sqlexample
SELECT 0.4 OR 0.3;
```

```output
+------------+
| 0.4 OR 0.3 |
|------------|
| True       |
+------------+
```
