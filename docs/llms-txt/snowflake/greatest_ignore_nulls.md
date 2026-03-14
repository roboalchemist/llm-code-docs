# Source: https://docs.snowflake.com/en/sql-reference/functions/greatest_ignore_nulls.md

Categories:
:   [Conditional expression functions](../expressions-conditional.md)

# GREATEST_IGNORE_NULLS

Returns the largest non-NULL value from a list of expressions. GREATEST_IGNORE_NULLS supports all data types,
including VARIANT.

See also:
:   [GREATEST](greatest.md)

## Syntax

```sqlsyntax
GREATEST_IGNORE_NULLS( <expr1> [ , <expr2> ... ] )
```

## Arguments

`exprN`
:   The arguments must include at least one expression. All the expressions
    should be of the same type or compatible types.

## Returns

The first argument determines the return type:

* If the first type is numeric, then the return type is ‘widened’
  according to the numeric types in the list of all arguments.
* If the first type is not numeric, then all other arguments must be
  convertible to the first type.

If all arguments are NULL, returns NULL.

## Collation details

* The [collation specifications](../collation.md) of all input arguments must be compatible.
* The comparisons follow the collation based on the input arguments’ collations and precedences.
* The collation of the result of the function is the highest-[precedence](../collation.md) collation of the inputs.

## Examples

Create a table and insert some values:

```sqlexample
CREATE TABLE test_greatest_ignore_nulls (
  col_1 INTEGER,
  col_2 INTEGER,
  col_3 INTEGER,
  col_4 FLOAT);

INSERT INTO test_greatest_ignore_nulls (col_1, col_2, col_3, col_4) VALUES
  (1, 2,    3,  4.25),
  (2, 4,   -1,  NULL),
  (3, 6, NULL,  -2.75);
```

Run a SELECT statement that returns the greatest non-null value in each row of the table:

```sqlexample
SELECT col_1,
       col_2,
       col_3,
       col_4,
       GREATEST_IGNORE_NULLS(col_1, col_2, col_3, col_4) AS greatest_ignore_nulls
 FROM test_greatest_ignore_nulls
 ORDER BY col_1;
```

```output
+-------+-------+-------+-------+-----------------------+
| COL_1 | COL_2 | COL_3 | COL_4 | GREATEST_IGNORE_NULLS |
|-------+-------+-------+-------+-----------------------|
|     1 |     2 |     3 |  4.25 |                  4.25 |
|     2 |     4 |    -1 |  NULL |                  4    |
|     3 |     6 |  NULL | -2.75 |                  6    |
+-------+-------+-------+-------+-----------------------+
```
