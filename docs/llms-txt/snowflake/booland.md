# Source: https://docs.snowflake.com/en/sql-reference/functions/booland.md

Categories:
:   [Conditional expression functions](../expressions-conditional.md)

# BOOLAND

Computes the Boolean AND of two numeric expressions. In accordance with Boolean semantics:

* Non-zero values, including negative numbers, are regarded as true.
* Zero values are regarded as false.

As a result, the function returns:

* `True` if both expressions are non-zero.
* `False` if both expressions are zero or one expression is zero and the other expression is non-zero or NULL.
* `NULL` if both expressions are NULL or one expression is NULL and the other expression is non-zero.

See also:
:   [BOOLNOT](boolnot.md) , [BOOLOR](boolor.md) , [BOOLXOR](boolxor.md)

## Syntax

```sqlsyntax
BOOLAND( <expr1> , <expr2> )
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

For examples of this behavior and workarounds, see Compute Boolean AND results for floating-point numbers.

## Examples

The following examples use the BOOLAND function.

### Compute Boolean AND results for integers and NULL values

The following query computes Boolean AND results for integers and NULL values:

```sqlexample
SELECT BOOLAND(1, -2),
       BOOLAND(0, 0),
       BOOLAND(0, NULL),
       BOOLAND(NULL, 3),
       BOOLAND(NULL, NULL);
```

```output
+----------------+---------------+------------------+------------------+---------------------+
| BOOLAND(1, -2) | BOOLAND(0, 0) | BOOLAND(0, NULL) | BOOLAND(NULL, 3) | BOOLAND(NULL, NULL) |
|----------------+---------------+------------------+------------------+---------------------|
| True           | False         | False            | NULL             | NULL                |
+----------------+---------------+------------------+------------------+---------------------+
```

### Compute Boolean AND results for floating-point numbers

The following examples show how the function might return unexpected results for floating-point
numbers that round to zero.

For the following queries, a result of `True` might be expected for the following function calls,
but they return `False` because the function rounds non-zero floating-point values to zero:

```sqlexample
SELECT BOOLAND(2, 0.3);
```

```output
+-----------------+
| BOOLAND(2, 0.3) |
|-----------------|
| False           |
+-----------------+
```

```sqlexample
SELECT BOOLAND(-0.4, 5);
```

```output
+------------------+
| BOOLAND(-0.4, 5) |
|------------------|
| False            |
+------------------+
```

If required, you can work around this rounding behavior for floating-point values by using
the [AND logical operator](../operators-logical.md) instead of the function.
For example, the following query returns `True`:

```sqlexample
SELECT 2 AND 0.3;
```

```output
+-----------+
| 2 AND 0.3 |
|-----------|
| True      |
+-----------+
```
