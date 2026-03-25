# Source: https://docs.snowflake.com/en/sql-reference/operators-expansion.md

# Expansion operators

Expansion operators expand a query expression that represents a list into the individual values in
the list. Currently, the spread operator (`**`) is the only expansion operator supported by Snowflake.

## Spread

The spread operator expands an [array](data-types-semistructured.md) into a list of individual values. This
operator is useful for the following use cases:

* Queries containing [IN clauses](functions/in.md).
* Calls to system-defined functions that take a list of values as arguments, such as
  [COALESCE](functions/coalesce.md), [GREATEST](functions/greatest.md), and
  [LEAST](functions/least.md).
* SQL user-defined [functions](../developer-guide/udf/sql/udf-sql-introduction.md) that use an argument
  to provide an array of values.
* Snowflake Scripting [stored procedures](../developer-guide/stored-procedure/stored-procedures-snowflake-scripting.md)
  that use a bind variable to provide an array of values. For more information about using bind variables
  in Snowflake Scripting, see [Using a variable in a SQL statement (binding)](../developer-guide/snowflake-scripting/variables.md) and
  [Using an argument in a SQL statement (binding)](../developer-guide/stored-procedure/stored-procedures-snowflake-scripting.md).

For more information about these use cases, see the
[Snowflake Introduces SQL Spread Operator (\*\*)](https://www.snowflake.com/en/engineering-blog/sql-spread-operator/)
blog post.

### Syntax

```sqlsyntax
** <array>
```

### Limitations

* The input must be an array of constant values, which can be an array of literal values or a bind variable that represents
  an array of literal values.
* Each value in a semi-structured array is of type [VARIANT](data-types-semistructured.md). A VARIANT value can
  contain a value of any other data type. The spread operator supports the following data types for the value
  stored in the VARIANT value:

  * [Numeric](data-types-numeric.md) (for example, INTEGER and NUMERIC)
  * [String & binary](data-types-text.md) (for example, VARCHAR and BINARY)
  * [Logical](data-types-logical.md) (for example, BOOLEAN)
  * [Date & time](data-types-datetime.md) (for example, DATE, TIME, and TIMESTAMP)
* User-defined functions and stored procedures written in languages other than SQL can’t use the
  spread operator.
* Expanding very large arrays with the spread operator might degrade performance.

### Examples

Some of the examples use the data the following table:

Create a table and insert data:

```sqlexample
CREATE OR REPLACE TABLE spread_demo (col1 INT, col2 VARCHAR);

INSERT INTO spread_demo VALUES
  (1, 'a'),
  (2, 'b'),
  (3, 'c'),
  (4, 'd'),
  (5, 'e');

SELECT * FROM spread_demo;
```

```output
+------+------+
| COL1 | COL2 |
|------+------|
|    1 | a    |
|    2 | b    |
|    3 | c    |
|    4 | d    |
|    5 | e    |
+------+------+
```

The following examples use the spread operator.

* Expand an array of literal values in an IN clause
* Expand an array of literal values in a system-defined function call
* Use the spread operator with a bind variable in a SQL user-defined function
* Use the spread operator with a bind variable in a Snowflake Scripting stored procedure

#### Expand an array of literal values in an IN clause

Expand an array of numbers using the spread operator in a query on the `spread_demo` table
created previously:

```sqlexample
SELECT * FROM spread_demo
  WHERE col1 IN (** [3, 4])
  ORDER BY col1;
```

```output
+------+------+
| COL1 | COL2 |
|------+------|
|    3 | c    |
|    4 | d    |
+------+------+
```

Expand an array of strings using the spread operator:

```sqlexample
SELECT * FROM spread_demo
  WHERE col2 IN (** ['b', 'd'])
  ORDER BY col1;
```

```output
+------+------+
| COL1 | COL2 |
|------+------|
|    2 | b    |
|    4 | d    |
+------+------+
```

Use an IN clause in a query with a mix of INTEGER values and expanded array values:

```sqlexample
SELECT * FROM spread_demo
  WHERE col1 IN (** [1, 2], 4, 5)
  ORDER BY col1;
```

```output
+------+------+
| COL1 | COL2 |
|------+------|
|    1 | a    |
|    2 | b    |
|    4 | d    |
|    5 | e    |
+------+------+
```

#### Expand an array of literal values in a system-defined function call

Expand an array of strings in a call to the COALESCE function:

```sqlexample
SELECT COALESCE(** [NULL, NULL, 'my_string_1', 'my_string_2']) AS first_non_null;
```

```output
+----------------+
| FIRST_NON_NULL |
|----------------|
| my_string_1    |
+----------------+
```

Expand an array of numbers in a call to the GREATEST function:

```sqlexample
SELECT GREATEST(** [1, 2, 5, 4, 5]) AS greatest_value;
```

```output
+----------------+
| GREATEST_VALUE |
|----------------|
|              5 |
+----------------+
```

#### Use the spread operator with a bind variable in a SQL user-defined function

Create a SQL user-defined function that uses the spread operator. The function takes an array as
an argument and then expands the array values to query the `spread_demo` table
created previously:

```sqlexample
CREATE OR REPLACE FUNCTION spread_function_demo(col_1_values ARRAY)
  RETURNS TABLE(
    col1 INT,
    col2 VARCHAR)
AS
$$
   SELECT * FROM spread_demo
     WHERE col1 IN (** col_1_values)
     ORDER BY col1
$$;
```

Query the table using the function:

```sqlexample
SELECT * FROM TABLE(spread_function_demo([1, 3, 5]));
```

```output
+------+------+
| COL1 | COL2 |
|------+------|
|    1 | a    |
|    3 | c    |
|    5 | e    |
+------+------+
```

#### Use the spread operator with a bind variable in a Snowflake Scripting stored procedure

Create a Snowflake Scripting stored procedure that uses the spread operator. The stored procedure takes
an array as an argument and then expands the array values in a bind variable to query the `spread_demo`
table created previously:

```sqlexample
CREATE OR REPLACE PROCEDURE spread_sp_demo(col_1_values ARRAY)
  RETURNS TABLE(
    col1 INT,
    col2 VARCHAR)
  LANGUAGE SQL
AS
$$
DECLARE
  res RESULTSET;
BEGIN
  res := (SELECT * FROM spread_demo
     WHERE col1 IN (** :col_1_values)
     ORDER BY col1);
  RETURN TABLE(res);
END;
$$;
```

Call the stored procedure:

```sqlexample
CALL spread_sp_demo([2, 4]);
```

```output
+------+------+
| COL1 | COL2 |
|------+------|
|    2 | b    |
|    4 | d    |
+------+------+
```
