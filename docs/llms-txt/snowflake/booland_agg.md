# Source: https://docs.snowflake.com/en/sql-reference/functions/booland_agg.md

Categories:
:   [Aggregate functions](../functions-aggregation.md) (Boolean) , [Window functions](../functions-window.md) , [Conditional expression functions](../expressions-conditional.md)

# BOOLAND_AGG

Returns TRUE if all non-NULL Boolean records in a group evaluate to TRUE.

If all records in the group are NULL, or if the group is empty, the function returns NULL.

See also:
:   [BOOLAND](booland.md) , [BOOLOR_AGG](boolor_agg.md) , [BOOLXOR_AGG](boolxor_agg.md)

## Syntax

**Aggregate function**

```sqlsyntax
BOOLAND_AGG( <expr> )
```

**Window function**

```sqlsyntax
BOOLAND_AGG( <expr> )  OVER ( [ PARTITION BY <partition_expr> ] )
```

## Arguments

`expr`
:   The input expression must be an expression that can be evaluated to a boolean or converted to a boolean.

`partition_expr`
:   This column or expression specifies how to separate the input into partitions (sub-windows).

## Returns

This function returns a value of type BOOLEAN.

## Usage notes

* [Numeric](../data-types-numeric.md) values are converted to `TRUE` if they are non-zero.
* [String and binary](../data-types-text.md) values aren’t supported because they can’t be converted to Boolean values.

* When this function is called as a window function, it does not support:

  * An ORDER BY clause within the OVER clause.
  * Explicit window frames.

## Examples

**Aggregate function**

The following example shows that booland_agg returns true when all of the input values are true.

Create and load the table:

```sqlexample
CREATE OR REPLACE TABLE test_boolean_agg (
  id INTEGER,
  c1 BOOLEAN,
  c2 BOOLEAN,
  c3 BOOLEAN,
  c4 BOOLEAN
);

INSERT INTO test_boolean_agg (id, c1, c2, c3, c4) VALUES
  (1, TRUE, TRUE,  TRUE,  FALSE),
  (2, TRUE, FALSE, FALSE, FALSE),
  (3, TRUE, TRUE,  FALSE, FALSE),
  (4, TRUE, FALSE, FALSE, FALSE);
```

Display the data:

```sqlexample
SELECT *
  FROM test_boolean_agg;
```

```output
+----+------+-------+-------+-------+
| ID | C1   | C2    | C3    | C4    |
|----+------+-------+-------+-------|
|  1 | True | True  | True  | False |
|  2 | True | False | False | False |
|  3 | True | True  | False | False |
|  4 | True | False | False | False |
+----+------+-------+-------+-------+
```

Query the data:

```sqlexample
SELECT BOOLAND_AGG(c1), BOOLAND_AGG(c2), BOOLAND_AGG(c3), BOOLAND_AGG(c4)
  FROM test_boolean_agg;
```

```output
+-----------------+-----------------+-----------------+-----------------+
| BOOLAND_AGG(C1) | BOOLAND_AGG(C2) | BOOLAND_AGG(C3) | BOOLAND_AGG(C4) |
|-----------------+-----------------+-----------------+-----------------|
| True            | False           | False           | False           |
+-----------------+-----------------+-----------------+-----------------+
```

**Window function**

This example is similar to the previous example, but it shows usage as a window function, with the input rows
split into two partitions (one for IDs greater than 0 and one for IDs less than or equal to 0). Additional data was
added to the table.

Add rows to the table:

```sqlexample
INSERT INTO test_boolean_agg (id, c1, c2, c3, c4) VALUES
  (-4, FALSE, FALSE, FALSE, TRUE),
  (-3, FALSE, TRUE,  TRUE,  TRUE),
  (-2, FALSE, FALSE, TRUE,  TRUE),
  (-1, FALSE, TRUE,  TRUE,  TRUE);
```

Display the data:

```sqlexample
SELECT *
  FROM test_boolean_agg
  ORDER BY id;
```

```output
+----+-------+-------+-------+-------+
| ID | C1    | C2    | C3    | C4    |
|----+-------+-------+-------+-------|
| -4 | False | False | False | True  |
| -3 | False | True  | True  | True  |
| -2 | False | False | True  | True  |
| -1 | False | True  | True  | True  |
|  1 | True  | True  | True  | False |
|  2 | True  | False | False | False |
|  3 | True  | True  | False | False |
|  4 | True  | False | False | False |
+----+-------+-------+-------+-------+
```

Query the data:

```sqlexample
SELECT
    id,
    BOOLAND_AGG(c1) OVER (PARTITION BY (id > 0)),
    BOOLAND_AGG(c2) OVER (PARTITION BY (id > 0)),
    BOOLAND_AGG(c3) OVER (PARTITION BY (id > 0)),
    BOOLAND_AGG(c4) OVER (PARTITION BY (id > 0))
  FROM test_boolean_agg
  ORDER BY id;
```

```output
+----+----------------------------------------------+----------------------------------------------+----------------------------------------------+----------------------------------------------+
| ID | BOOLAND_AGG(C1) OVER (PARTITION BY (ID > 0)) | BOOLAND_AGG(C2) OVER (PARTITION BY (ID > 0)) | BOOLAND_AGG(C3) OVER (PARTITION BY (ID > 0)) | BOOLAND_AGG(C4) OVER (PARTITION BY (ID > 0)) |
|----+----------------------------------------------+----------------------------------------------+----------------------------------------------+----------------------------------------------|
| -4 | False                                        | False                                        | False                                        | True                                         |
| -3 | False                                        | False                                        | False                                        | True                                         |
| -2 | False                                        | False                                        | False                                        | True                                         |
| -1 | False                                        | False                                        | False                                        | True                                         |
|  1 | True                                         | False                                        | False                                        | False                                        |
|  2 | True                                         | False                                        | False                                        | False                                        |
|  3 | True                                         | False                                        | False                                        | False                                        |
|  4 | True                                         | False                                        | False                                        | False                                        |
+----+----------------------------------------------+----------------------------------------------+----------------------------------------------+----------------------------------------------+
```

**Error example**

If this function is passed strings that can’t be converted to Boolean, the function returns an error:

```sqlsyntax
select booland_agg('invalid type');

100037 (22018): Boolean value 'invalid_type' is not recognized
```
