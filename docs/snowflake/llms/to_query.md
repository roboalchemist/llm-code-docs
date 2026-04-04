# Source: https://docs.snowflake.com/en/sql-reference/functions/to_query.md

Categories:
:   [Table functions](../functions-table.md)

# TO_QUERY

Returns a result set based on SQL text and an optional set of arguments that are passed to the SQL text if
it is parameterized. The function compiles the SQL text as the definition of a subquery in the FROM clause.
When writing an application or a stored procedure, you can call this function to construct a SQL statement.

> **Note:**
>
> This function can include user input in query statements, which has potential security risks, such as
> SQL injection. If inputs to the function come from external sources, make sure they are validated.
> For more information, see [SQL injection](../../developer-guide/stored-procedure/stored-procedures-usage.md).

See also:
:   [Constructing SQL at runtime](../../user-guide/querying-construct-at-runtime.md)

## Syntax

```sqlsyntax
TO_QUERY( SQL => '<string>' [ , <arg> => '<value>' [, <arg> => '<value>' ...] ] )
```

## Arguments

**Required**

`SQL => 'string'`
:   String representation of the subquery.

**Optional**

`arg => 'value'`
:   [Bind variables](../bind-variables.md) passed to the SQL `string`.

## Returns

Returns the result set produced by the execution of the specified SQL text or NULL. If any argument is NULL,
the function returns NULL without reporting any error.

## Usage notes

* All arguments must be one of the following:

  * Constant strings.
  * [SQL variables](../session-variables.md) or
    [Snowflake Scripting variables](../../developer-guide/snowflake-scripting/variables.md) that resolve to strings.
* If you need to convert a string passed in an argument to a different data type, you can use a
  [conversion function](../functions-conversion.md) in the SQL `string` to
  convert the string to another data type.
* The set of columns defining the result set is derived from the SELECT list of the compiled SQL statement.
* The function is valid only in the FROM clause of a SQL statement.

## Examples

Create a table and insert data into it.

```sqlexample
CREATE OR REPLACE TABLE to_query_example (
  deptno NUMBER(2),
  dname  VARCHAR(14),
  loc    VARCHAR(13))
AS SELECT
  column1,
  column2,
  column3
FROM
  VALUES
    (10, 'ACCOUNTING', 'NEW YORK'),
    (20, 'RESEARCH',   'DALLAS'  ),
    (30, 'SALES',      'CHICAGO' ),
    (40, 'OPERATIONS', 'BOSTON'  );
```

The examples use the data in this table.

### Using TO_QUERY in SQL statements

First, set a session variable (SQL variable) for the table name:

```sqlexample
SET table_name = 'to_query_example';
```

The examples use the session variable and [IDENTIFIER()](../identifier-literal.md) to
identify the table.

Using IDENTIFIER() to identify database objects is a best practice because it can make
code more reusable and help to prevent [SQL injection](../../developer-guide/stored-procedure/stored-procedures-usage.md) risks.

The following example uses the TO_QUERY function to return all of the data in the `to_query_example` table:

```sqlexample
SELECT * FROM TABLE(TO_QUERY('SELECT * FROM IDENTIFIER($table_name)'));
```

```output
+--------+------------+----------+
| DEPTNO | DNAME      | LOC      |
|--------+------------+----------|
|     10 | ACCOUNTING | NEW YORK |
|     20 | RESEARCH   | DALLAS   |
|     30 | SALES      | CHICAGO  |
|     40 | OPERATIONS | BOSTON   |
+--------+------------+----------+
```

The following example uses the TO_QUERY function to return all of the values in the `deptno` column of
the `to_query_example` table:

```sqlexample
SELECT deptno FROM TABLE(TO_QUERY('SELECT * FROM IDENTIFIER($table_name)'));
```

```output
+--------+
| DEPTNO |
|--------|
|     10 |
|     20 |
|     30 |
|     40 |
+--------+
```

The following example uses the TO_QUERY function to pass an argument to a SQL statement so that it returns the row
where `deptno` equals `10` in the `to_query_example` table:

```sqlexample
SELECT * FROM TABLE(
  TO_QUERY(
    'SELECT * FROM IDENTIFIER($table_name)
    WHERE deptno = TO_NUMBER(:dno)', dno => '10'
    )
  );
```

```output
+--------+------------+----------+
| DEPTNO | DNAME      | LOC      |
|--------+------------+----------|
|     10 | ACCOUNTING | NEW YORK |
+--------+------------+----------+
```

The following example is the same as the previous example, but it uses a session variable to pass
the `deptno` value to the TO_QUERY function:

```sqlexample
SET dept = '10';

SELECT * FROM TABLE(
  TO_QUERY(
    'SELECT * FROM IDENTIFIER($table_name)
    WHERE deptno = TO_NUMBER(:dno)', dno => $dept
    )
  );
```

```output
+--------+------------+----------+
| DEPTNO | DNAME      | LOC      |
|--------+------------+----------|
|     10 | ACCOUNTING | NEW YORK |
+--------+------------+----------+
```

The following example uses the TO_QUERY function to pass two arguments to a SQL statement so that it returns the rows
where `deptno` equals `10` or `dname` equals `SALES` in the `to_query_example` table:

```sqlexample
SELECT * FROM TABLE(
  TO_QUERY(
    'SELECT * FROM IDENTIFIER($table_name)
    WHERE deptno = TO_NUMBER(:dno) OR dname = :dnm',
    dno => '10', dnm => 'SALES'
    )
  );
```

```output
+--------+------------+----------+
| DEPTNO | DNAME      | LOC      |
|--------+------------+----------|
|     10 | ACCOUNTING | NEW YORK |
|     30 | SALES      | CHICAGO  |
+--------+------------+----------+
```

### Using TO_QUERY in stored procedures

The following example uses the TO_QUERY function in a stored procedure:

```sqlexample
CREATE OR REPLACE PROCEDURE get_num_results_tq(query VARCHAR)
RETURNS TABLE ()
LANGUAGE SQL
AS
DECLARE
  res RESULTSET DEFAULT (SELECT COUNT(*) FROM TABLE(TO_QUERY(:query)));
BEGIN
  RETURN TABLE(res);
END;
```

Note: If you use [Snowflake CLI](../../developer-guide/snowflake-cli/index.md), [SnowSQL](../../user-guide/snowsql.md), the Classic Console, or the
`execute_stream` or `execute_string` method in [Python Connector](../../developer-guide/python-connector/python-connector.md)
code, use this example instead (see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](../../developer-guide/snowflake-scripting/running-examples.md)):

```sqlexample
CREATE OR REPLACE PROCEDURE get_num_results_tq(query VARCHAR)
RETURNS TABLE ()
LANGUAGE SQL
AS
$$
DECLARE
  res RESULTSET DEFAULT (SELECT COUNT(*) FROM TABLE(TO_QUERY(:query)));
BEGIN
  RETURN TABLE(res);
END;
$$
;
```

Call the stored procedure:

```sqlexample
CALL get_num_results_tq('SELECT * FROM to_query_example');
```

```output
+----------+
| COUNT(*) |
|----------|
|        4 |
+----------+
```

```sqlexample
CALL get_num_results_tq('SELECT * FROM to_query_example WHERE deptno = 20');
```

```output
+----------+
| COUNT(*) |
|----------|
|        1 |
+----------+
```

The following example uses the TO_QUERY function in a stored procedure with a bind variable:

```sqlexample
CREATE OR REPLACE PROCEDURE get_results_tqbnd(dno VARCHAR)
RETURNS TABLE ()
LANGUAGE SQL
AS
DECLARE
  res RESULTSET DEFAULT (SELECT * FROM TABLE(
    TO_QUERY(
      'SELECT * FROM to_query_example
      WHERE deptno = TO_NUMBER(:dnoval)', dnoval => :dno
    )
  ));
BEGIN
  RETURN TABLE(res);
END;
```

Note: If you use [Snowflake CLI](../../developer-guide/snowflake-cli/index.md), [SnowSQL](../../user-guide/snowsql.md), the Classic Console, or the
`execute_stream` or `execute_string` method in [Python Connector](../../developer-guide/python-connector/python-connector.md)
code, use this example instead (see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](../../developer-guide/snowflake-scripting/running-examples.md)):

```sqlexample
CREATE OR REPLACE PROCEDURE get_results_tqbnd(dno VARCHAR)
RETURNS TABLE ()
LANGUAGE SQL
AS
$$
DECLARE
  res RESULTSET DEFAULT (SELECT * FROM TABLE(
    TO_QUERY(
      'SELECT * FROM to_query_example
      WHERE deptno = TO_NUMBER(:dnoval)', dnoval => :dno
    )
  ));
BEGIN
  RETURN TABLE(res);
END;
$$
;
```

Call the stored procedure:

```sqlexample
CALL get_results_tqbnd('40');
```

```output
+--------+------------+--------+
| DEPTNO | DNAME      | LOC    |
|--------+------------+--------|
|     40 | OPERATIONS | BOSTON |
+--------+------------+--------+
```

Call the stored procedure using a session variable:

```sqlexample
SET dept = '20';

CALL get_results_tqbnd($dept);
```

```output
+--------+----------+--------+
| DEPTNO | DNAME    | LOC    |
|--------+----------+--------|
|     20 | RESEARCH | DALLAS |
+--------+----------+--------+
```
