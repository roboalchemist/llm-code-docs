# Source: https://docs.snowflake.com/en/migrations/sma-docs/translation-reference/spark-sql/spark-sql-dml/select/values.md

# Source: https://docs.snowflake.com/en/sql-reference/constructs/values.md

Categories:
:   [Query syntax](../constructs.md)

# VALUES

In the SELECT statement, the VALUES subclause of the FROM clause lets you
specify a set of constants to form a finite set of rows.

For information about the VALUES clause in the INSERT statement, see
the documentation for the [INSERT](../sql/insert.md) statement.

## Syntax

```sqlsyntax
SELECT ...
FROM ( VALUES ( <expr> [ , <expr> [ , ... ] ] ) [ , ( ... ) ] )
  [ [ AS ] <table_alias> [ ( <column_alias> [ , ... ] ) ] ]
[ ... ]
```

## Parameters

`expr`
:   Each expression must be a constant, or an expression that can be evaluated as a constant during compilation of the
    SQL statement.

    Most simple arithmetic expressions and string functions can be evaluated at compile time, but most other expressions
    can’t.

`table_alias`
:   An optional alias to give the set of rows a name, as though the set of rows were a table.

`column_alias`
:   Optional column aliases can specify the columns names.

## Usage notes

* Inside a [FROM](from.md) clause, a VALUES clause can’t contain the `DEFAULT` keyword. This limitation is in contrast
  to a VALUES clause in an [INSERT](../sql/insert.md) statement, which supports the use
  of `DEFAULT`; for example, `INSERT INTO table VALUES (10, DEFAULT, 'Name') ...`.
* When the VALUES clause includes multiple numeric values for the same column, and the values differ significantly in scale
  or precision, Snowflake might return an `out of range` error. The error might be returned even if each individual value
  wouldn’t result in an error for the target column’s data type.

  The error occurs because Snowflake determines a common, numeric data type that can encompass all of the numeric literals
  provided in a VALUES clause, and some values might be out of range for the determined common data type.

  For example, the following statement returns an `out of range` error:

  ```sqlexample
  SELECT column1 FROM VALUES
    (3.469446951953614e-18),
    (115898.73);
  ```

  ```output
  100039 (22003): Numeric value '115898.73' is out of range
  ```

  You can avoid this type of error by making the following changes:

  * Separate the values in the VALUES clause into multiple SQL statements.
  * Cast values to a data type with a wider range of values, such as FLOAT. However, casting might result in less numeric precision.
  * Specify the values as text strings in quotation marks, and then convert the values to numeric values as needed.
* The VALUES clause is limited to 200,000 rows.

## Examples

The following examples use the VALUES clause to generate a fixed, known set of rows:

```sqlexample
SELECT * FROM (VALUES (1, 'one'), (2, 'two'), (3, 'three'));
```

```output
+---------+---------+
| COLUMN1 | COLUMN2 |
|---------+---------|
|       1 | one     |
|       2 | two     |
|       3 | three   |
+---------+---------+
```

You can reference values either by column name (implicit) or column position. The following
example references the second column by column position:

```sqlexample
SELECT column1, $2 FROM (VALUES (1, 'one'), (2, 'two'), (3, 'three'));
```

```output
+---------+-------+
| COLUMN1 | $2    |
|---------+-------|
|       1 | one   |
|       2 | two   |
|       3 | three |
+---------+-------+
```

The following example distinguishes multiple VALUES clauses by using aliases:

```sqlexample
SELECT v1.$2, v2.$2
  FROM (VALUES (1, 'one'), (2, 'two')) AS v1
        INNER JOIN (VALUES (1, 'One'), (3, 'three')) AS v2
  WHERE v2.$1 = v1.$1;
```

You can also specify aliases for the column names, as shown in the following example:

```sqlexample
SELECT c1, c2
  FROM (VALUES (1, 'one'), (2, 'two')) AS v1 (c1, c2);
```
