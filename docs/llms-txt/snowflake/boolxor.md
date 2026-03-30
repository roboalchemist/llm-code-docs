# Source: https://docs.snowflake.com/en/sql-reference/functions/boolxor.md

Categories:
:   [Conditional expression functions](../expressions-conditional.md)

# BOOLXOR

Computes the Boolean XOR of two numeric expressions; that is, one of the expressions, but not both expressions,
is true. In accordance with Boolean semantics:

* Non-zero values, including negative numbers, are regarded as true.
* Zero values are regarded as false.

As a result, the function returns:

* `True` if one expression is non-zero and the other expression is zero.
* `False` if both expressions are non-zero or both expressions are zero.
* `NULL` if one or both expressions are NULL.

See also:
:   [BOOLAND](booland.md) , [BOOLNOT](boolnot.md) , [BOOLOR](boolor.md)

## Syntax

```sqlsyntax
BOOLXOR( <expr1> , <expr2> )
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

For examples of this behavior and workarounds, see Compute Boolean XOR results for floating-point numbers.

## Examples

The following examples use the BOOLXOR function.

### Compute Boolean XOR results for integers and NULL values

The following query computes Boolean XOR results for integers and NULL values:

```sqlexample
SELECT BOOLXOR(2, 0),
       BOOLXOR(1, -1),
       BOOLXOR(0, 0),
       BOOLXOR(NULL, 3),
       BOOLXOR(NULL, 0),
       BOOLXOR(NULL, NULL);
```

```output
+---------------+----------------+---------------+------------------+------------------+---------------------+
| BOOLXOR(2, 0) | BOOLXOR(1, -1) | BOOLXOR(0, 0) | BOOLXOR(NULL, 3) | BOOLXOR(NULL, 0) | BOOLXOR(NULL, NULL) |
|---------------+----------------+---------------+------------------+------------------+---------------------|
| True          | False          | False         | NULL             | NULL             | NULL                |
+---------------+----------------+---------------+------------------+------------------+---------------------+
```

### Compute Boolean XOR results for floating-point numbers

The following examples demonstrate how the function might return unexpected results for floating-point
numbers that round to zero.

For the following queries, a result of `False` might be expected for the following function calls, but they return
`True` because the function rounds non-zero floating-point values to zero:

```sqlexample
SELECT BOOLXOR(2, 0.3);
```

```output
+-----------------+
| BOOLXOR(2, 0.3) |
|-----------------|
| True            |
+-----------------+
```

```sqlexample
SELECT BOOLXOR(-0.4, 5);
```

```output
+------------------+
| BOOLXOR(-0.4, 5) |
|------------------|
| True             |
+------------------+
```

Similarly, a result of `True` might be expected for the following function calls, but they return
`False`:

```sqlexample
SELECT BOOLXOR(0, 0.3);
```

```output
+-----------------+
| BOOLXOR(0, 0.3) |
|-----------------|
| False           |
+-----------------+
```

```sqlexample
SELECT BOOLXOR(-0.4, 0);
```

```output
+------------------+
| BOOLXOR(-0.4, 0) |
|------------------|
| False            |
+------------------+
```

If required, you can work around this rounding behavior for positive floating-point values by using the
[CEIL](ceil.md) function. For example, the following query returns `False`:

```sqlexample
SELECT BOOLXOR(2, CEIL(0.3));
```

```output
+-----------------------+
| BOOLXOR(2, CEIL(0.3)) |
|-----------------------|
| False                 |
+-----------------------+
```

For negative floating-point values, you can work around this rounding behavior by using the
[FLOOR](floor.md) function. For example, the following query returns `False`:

```sqlexample
SELECT BOOLXOR(FLOOR(-0.4), 5);
```

```output
+-------------------------+
| BOOLXOR(FLOOR(-0.4), 5) |
|-------------------------|
| False                   |
+-------------------------+
```
