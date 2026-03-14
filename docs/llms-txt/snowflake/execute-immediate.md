# Source: https://docs.snowflake.com/en/sql-reference/sql/execute-immediate.md

# EXECUTE IMMEDIATE

Executes a string that contains a SQL statement or a
[Snowflake Scripting statement](../../developer-guide/snowflake-scripting/blocks.md).

You can use EXECUTE IMMEDIATE to do the following:

* In a Snowflake Scripting block, execute dynamic SQL, where parts of the SQL statement aren’t known
  until runtime. For examples, see Executing dynamic SQL in a Snowflake Scripting block.
* Set a session variable to a SQL statement, and reference the session variable to run the SQL statement.
  For an example, see Setting a session variable to a statement and executing it.
* If you are using SnowSQL or Snowsight, run a Snowflake Scripting anonymous block.
  For an example, see Running an anonymous block in SnowSQL or Snowsight.

## Syntax

```sqlsyntax
EXECUTE IMMEDIATE '<string_literal>'
    [ USING ( <bind_variable> [ , <bind_variable> ... ] ) ]

EXECUTE IMMEDIATE <variable>
    [ USING ( <bind_variable> [ , <bind_variable> ... ] ) ]

EXECUTE IMMEDIATE $<session_variable>
    [ USING ( <bind_variable> [ , <bind_variable> ... ] ) ]
```

## Required parameters

`'string_literal'` or . `variable` or . `session_variable`
:   A string literal, Snowflake Scripting [variable](../../developer-guide/snowflake-scripting/variables.md), or
    [session variable](../session-variables.md) that contains a statement. A statement can be any of the following:

    * A single SQL statement
    * A stored procedure call
    * A control-flow statement (for example, [looping](../../developer-guide/snowflake-scripting/loops.md) or
      [branching](../../developer-guide/snowflake-scripting/branch.md) statement)
    * A [block](../../developer-guide/snowflake-scripting/blocks.md)

    If you use a session variable, the length of the statement must not exceed the
    [maximum size of a session variable (256 bytes)](../session-variables.md).

## Optional parameters

`USING ( bind_variable [ , bind_variable ... ] )`
:   Specifies one or more bind variables that hold values to be used in the cursor’s query definition (for example,
    in a WHERE clause).

## Returns

EXECUTE IMMEDIATE returns the result of the executed statement. For example, if the string or variable contained a SELECT
statement, the result set of the SELECT statement is returned.

## Usage notes

* The `string_literal`, `variable`, or `session_variable` must contain only one statement.
  (A [block](../../developer-guide/snowflake-scripting/blocks.md) is considered one statement, even if the body of the block
  contains multiple statements.)
* A `session_variable` must be preceded by a dollar sign (`$`).
* A local `variable` must not be preceded by a dollar sign (`$`).

## Examples

The following are examples that use the EXECUTE IMMEDIATE command.

### Executing dynamic SQL in a Snowflake Scripting block

The following examples execute dynamic SQL in a Snowflake Scripting block.

#### Executing statements that contain variables

This example executes statements that are defined in two local variables in a
[Snowflake Scripting stored procedure](../../developer-guide/stored-procedure/stored-procedures-snowflake-scripting.md).
This example also demonstrates that EXECUTE IMMEDIATE works not only with a string literal, but also
with an expression that evaluates to a string (VARCHAR).

```sqlexample
CREATE PROCEDURE execute_immediate_local_variable()
RETURNS VARCHAR
AS
DECLARE
  v1 VARCHAR DEFAULT 'CREATE TABLE temporary1 (i INTEGER)';
  v2 VARCHAR DEFAULT 'INSERT INTO temporary1 (i) VALUES (76)';
  result INTEGER DEFAULT 0;
BEGIN
  EXECUTE IMMEDIATE v1;
  EXECUTE IMMEDIATE v2  ||  ',(80)'  ||  ',(84)';
  result := (SELECT SUM(i) FROM temporary1);
  RETURN result::VARCHAR;
END;
```

Note: If you use [Snowflake CLI](../../developer-guide/snowflake-cli/index.md), [SnowSQL](../../user-guide/snowsql.md), the Classic Console, or the
`execute_stream` or `execute_string` method in [Python Connector](../../developer-guide/python-connector/python-connector.md)
code, use this example instead (see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](../../developer-guide/snowflake-scripting/running-examples.md)):

```sqlexample
CREATE PROCEDURE execute_immediate_local_variable()
RETURNS VARCHAR
AS
$$
DECLARE
  v1 VARCHAR DEFAULT 'CREATE TABLE temporary1 (i INTEGER)';
  v2 VARCHAR DEFAULT 'INSERT INTO temporary1 (i) VALUES (76)';
  result INTEGER DEFAULT 0;
BEGIN
  EXECUTE IMMEDIATE v1;
  EXECUTE IMMEDIATE v2  ||  ',(80)'  ||  ',(84)';
  result := (SELECT SUM(i) FROM temporary1);
  RETURN result::VARCHAR;
END;
$$;
```

Call the stored procedure:

```sqlexample
CALL execute_immediate_local_variable();
```

```output
+----------------------------------+
| EXECUTE_IMMEDIATE_LOCAL_VARIABLE |
|----------------------------------|
| 240                              |
+----------------------------------+
```

#### Executing a statement that contains bind variables

This example uses EXECUTE IMMEDIATE to execute a SELECT statement that contains bind variables
in the USING parameter in a Snowflake Scripting stored procedure. First create the table and insert
the data:

```sqlexample
CREATE OR REPLACE TABLE invoices (id INTEGER, price NUMBER(12, 2));

INSERT INTO invoices (id, price) VALUES
  (1, 11.11),
  (2, 22.22);
```

Create the stored procedure:

```sqlexample
CREATE OR REPLACE PROCEDURE min_max_invoices_sp(
    minimum_price NUMBER(12,2),
    maximum_price NUMBER(12,2))
  RETURNS TABLE (id INTEGER, price NUMBER(12, 2))
  LANGUAGE SQL
AS
DECLARE
  rs RESULTSET;
  query VARCHAR DEFAULT 'SELECT * FROM invoices WHERE price > ? AND price < ?';
BEGIN
  rs := (EXECUTE IMMEDIATE :query USING (minimum_price, maximum_price));
  RETURN TABLE(rs);
END;
```

Note: If you use [Snowflake CLI](../../developer-guide/snowflake-cli/index.md), [SnowSQL](../../user-guide/snowsql.md), the Classic Console, or the
`execute_stream` or `execute_string` method in [Python Connector](../../developer-guide/python-connector/python-connector.md)
code, use this example instead (see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](../../developer-guide/snowflake-scripting/running-examples.md)):

```sqlexample
CREATE OR REPLACE PROCEDURE min_max_invoices_sp(
    minimum_price NUMBER(12,2),
    maximum_price NUMBER(12,2))
  RETURNS TABLE (id INTEGER, price NUMBER(12, 2))
  LANGUAGE SQL
AS
$$
DECLARE
  rs RESULTSET;
  query VARCHAR DEFAULT 'SELECT * FROM invoices WHERE price > ? AND price < ?';
BEGIN
  rs := (EXECUTE IMMEDIATE :query USING (minimum_price, maximum_price));
  RETURN TABLE(rs);
END;
$$
;
```

Call the stored procedure:

```sqlexample
CALL min_max_invoices_sp(20, 30);
```

```output
+----+-------+
| ID | PRICE |
|----+-------|
|  2 | 22.22 |
+----+-------+
```

### Setting a session variable to a statement and executing it

This example executes a statement defined in a session variable:

```sqlexample
SET stmt =
$$
    SELECT PI();
$$
;
```

```sqlexample
EXECUTE IMMEDIATE $stmt;
```

```output
+-------------+
|        PI() |
|-------------|
| 3.141592654 |
+-------------+
```

### Running an anonymous block in SnowSQL or Snowsight

When you run a [Snowflake Scripting](../../developer-guide/snowflake-scripting/index.md) anonymous block
in [SnowSQL](../../user-guide/snowsql.md) or [Snowsight](../../user-guide/ui-snowsight-gs.md), you must specify the block as
a string literal (delimited by single quotes or double dollar signs), and you must pass the
block to the EXECUTE IMMEDIATE command. For more information, see
[Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](../../developer-guide/snowflake-scripting/running-examples.md).

This example runs an anonymous block passed to the EXECUTE IMMEDIATE command:

```sqlexample
EXECUTE IMMEDIATE $$
DECLARE
  radius_of_circle FLOAT;
  area_of_circle FLOAT;
BEGIN
  radius_of_circle := 3;
  area_of_circle := PI() * radius_of_circle * radius_of_circle;
  RETURN area_of_circle;
END;
$$
;
```

```output
+-----------------+
| anonymous block |
|-----------------|
|    28.274333882 |
+-----------------+
```
