# Source: https://docs.snowflake.com/en/developer-guide/stored-procedure/stored-procedures-snowflake-scripting.md

# Writing stored procedures in Snowflake Scripting

This topic provides an introduction to writing a stored procedure in SQL by using Snowflake Scripting.
For more information about Snowflake Scripting, see the [Snowflake Scripting Developer Guide](../snowflake-scripting/index.md).

## Introduction

To write a stored procedure that uses Snowflake Scripting:

* Use the [CREATE PROCEDURE](../../sql-reference/sql/create-procedure.md) or [WITH … CALL …](../../sql-reference/sql/call-with.md) command with
  LANGUAGE SQL.
* In the body of the stored procedure (the AS clause), you use a
  [Snowflake Scripting block](../snowflake-scripting/blocks.md).

  > **Note:**
  >
  > If you are creating a Snowflake Scripting procedure in [SnowSQL](../../user-guide/snowsql.md) or [Snowsight](../../user-guide/ui-snowsight-gs.md), you must use
  > [string literal delimiters](../../sql-reference/data-types-text.md) (`'` or `$$`) around the body of the stored procedure.
  >
  > For details, see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](../snowflake-scripting/running-examples.md).

Snowflake limits the maximum size of the source code in the body of a Snowflake Scripting stored procedure. Snowflake
recommends limiting the size to 100 KB. (The code is stored in a compressed form, and the exact limit depends on the
compressibility of the code.)

You can capture log and trace data as your handler code executes. For more information, see
[Logging, tracing, and metrics](../logging-tracing/logging-tracing-overview.md).

> **Note:**
>
> * The same rules around [caller’s rights vs. owner’s rights](stored-procedures-rights.md) apply to these stored procedures.
> * The same considerations and guidelines in [Working with stored procedures](stored-procedures-usage.md) apply to Snowflake Scripting stored procedures.

The following is an example of a simple stored procedure that returns the value of the argument that is passed in:

```sqlexample
CREATE OR REPLACE PROCEDURE output_message(message VARCHAR)
RETURNS VARCHAR NOT NULL
LANGUAGE SQL
AS
BEGIN
  RETURN message;
END;
```

Note: If you use [Snowflake CLI](../snowflake-cli/index.md), [SnowSQL](../../user-guide/snowsql.md), the Classic Console, or the
`execute_stream` or `execute_string` method in [Python Connector](../python-connector/python-connector.md)
code, use this example instead (see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](../snowflake-scripting/running-examples.md)):

```sqlexample
CREATE OR REPLACE PROCEDURE output_message(message VARCHAR)
RETURNS VARCHAR NOT NULL
LANGUAGE SQL
AS
$$
BEGIN
  RETURN message;
END;
$$
;
```

The following is an example of calling the stored procedure:

```sqlexample
CALL output_message('Hello World');
```

The following is an example of creating and calling an anonymous stored procedure by using the
[WITH … CALL …](../../sql-reference/sql/call-with.md) command:

```sqlexample
WITH anonymous_output_message AS PROCEDURE (message VARCHAR)
  RETURNS VARCHAR NOT NULL
  LANGUAGE SQL
  AS
  $$
  BEGIN
    RETURN message;
  END;
  $$
CALL anonymous_output_message('Hello World');
```

Note that in an anonymous stored procedure, you must use [string literal delimiters](../../sql-reference/data-types-text.md) (`'`
or `$$`) around the body of the procedure.

## Using arguments passed to a stored procedure

If you pass in any arguments to your stored procedure, you can refer to those arguments by name in any Snowflake Scripting
expression. Snowflake Scripting stored procedures support input (IN) and output (OUT) arguments.

When you specify an output argument in the definition of a Snowflake Scripting stored procedure, the stored procedure
can return the current value of the output argument to a calling program, such as an anonymous block or a different
stored procedure. The stored procedure takes an initial value for the output argument, saves the value to
a variable in the procedure body, and optionally performs operations to change the value of the variable, before
returning the updated value to the calling program.

For example, a salesperson’s user identifier and a sales quarter can be passed to a stored procedure named
`emp_quarter_calling_sp_demo`. This stored procedure calls a different stored procedure named
`sales_total_out_sp_demo`. The `sales_total_out_sp_demo` stored procedure has an output argument that
performs operations to return the salesperson’s total sales for the quarter to the calling stored procedure
`emp_quarter_calling_sp_demo`. For an example of this scenario, see
Using an output argument to return the total sales for an employee in a quarter.

When there is a mismatch between the data type of the value being passed in and the data type of the output argument,
supported coercions are performed automatically. For an example, see Using an output argument with a different data type than the input value from a calling procedure.
For information about which coercions Snowflake can perform automatically, see [Data types that can be cast](../../sql-reference/data-type-conversion.md).

The [GET_DDL](../../sql-reference/functions/get_ddl.md) function and the [SHOW PROCEDURES](../../sql-reference/sql/show-procedures.md) command show the
type (either `IN` or `OUT`) of a stored procedure’s arguments in output. Other commands and views that show
metadata about stored procedures don’t show the type of the arguments, such as the [DESCRIBE PROCEDURE](../../sql-reference/sql/desc-procedure.md)
command, the Information Schema [PROCEDURES view](../../sql-reference/info-schema/procedures.md), and the Account Usage
[PROCEDURES view](../../sql-reference/account-usage/procedures.md).

A stored procedure can’t be overloaded by specifying different argument types in the signature. For example, assume a stored
procedure has this signature:

```sqlexample
CREATE PROCEDURE test_overloading(a IN NUMBER)
```

The following CREATE PROCEDURE command fails with an error stating that the procedure already exists, because it tries to create
a new stored procedure that differs from the previous example only in the argument type:

```sqlexample
CREATE PROCEDURE test_overloading(a OUT NUMBER)
```

### Syntax

Use the following syntax to specify an argument in a Snowflake Scripting stored procedure definition:

```sqlsyntax
<arg_name> [ { IN | INPUT | OUT | OUTPUT } ] <arg_data_type>
```

Where:

`arg_name`
:   The name of the argument. The name must follow the naming rules for [Object identifiers](../../sql-reference/identifiers.md).

`{ IN | INPUT | OUT | OUTPUT }`
:   Optional keyword that specifies whether the argument is an input argument or an output argument.

    * `IN` or `INPUT` - The argument is initialized with the supplied value, and this value is assigned to a stored procedure
      variable. The variable can be modified in the stored procedure body, but its final value can’t be passed to a calling
      program.

      `IN` and `INPUT` are synonymous.
    * `OUT` or `OUTPUT` - The argument is initialized with the supplied value, and this value is assigned to a stored procedure
      variable. The variable can be modified in the stored procedure body, and its final value can be passed to a calling
      program. In a stored procedure body, output arguments can only be assigned values by using variables.

      Output arguments can also be passed uninitialized variables. When the associated variable is unassigned, the output
      argument returns NULL.

      `OUT` and `OUTPUT` are synonymous.

    Default: `IN`

`arg_data_type`
:   A [SQL data type](../../sql-reference-data-types.md).

### Limitations

* Output arguments must be specified in a stored procedure’s definition.
* Output arguments can’t be specified as [optional arguments](../udf-stored-procedure-arguments.md). That is,
  output arguments can’t be specified using the DEFAULT keyword.
* In the body of a stored procedure, variables must be used to assign values to output arguments.
* The same variable can’t be used for multiple output arguments.
* Session variables can’t be passed to output arguments.
* User-defined functions (UDFs) don’t support output arguments.
* Stored procedures written in languages other than SQL don’t support output arguments.
* Output arguments can’t be used in [asynchronous child jobs](../snowflake-scripting/asynchronous-child-jobs.md).
* Stored procedures are limited to 500 arguments, including both input and output arguments.

### Examples

* Simple example of using arguments passed to a stored procedure
* Using an argument in a SQL statement (binding)
* Using an argument as an object identifier
* Using an argument when building a string for a SQL statement
* Using an output argument to return a single value
* Using output arguments to return several values for multiple calls to a stored procedure
* Using an output argument with a different data type than the input value from a calling procedure
* Using an output argument to return the total sales for an employee in a quarter

#### Simple example of using arguments passed to a stored procedure

The following stored procedure uses the values of the arguments in [IF](../../sql-reference/snowflake-scripting/if.md) and
[RETURN](../../sql-reference/snowflake-scripting/return.md) statements.

```sqlexample
CREATE OR REPLACE PROCEDURE return_greater(number_1 INTEGER, number_2 INTEGER)
RETURNS INTEGER NOT NULL
LANGUAGE SQL
AS
BEGIN
  IF (number_1 > number_2) THEN
    RETURN number_1;
  ELSE
    RETURN number_2;
  END IF;
END;
```

Note: If you use [Snowflake CLI](../snowflake-cli/index.md), [SnowSQL](../../user-guide/snowsql.md), the Classic Console, or the
`execute_stream` or `execute_string` method in [Python Connector](../python-connector/python-connector.md)
code, use this example instead (see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](../snowflake-scripting/running-examples.md)):

```sqlexample
CREATE OR REPLACE PROCEDURE return_greater(number_1 INTEGER, number_2 INTEGER)
RETURNS INTEGER NOT NULL
LANGUAGE SQL
AS
$$
BEGIN
  IF (number_1 > number_2) THEN
    RETURN number_1;
  ELSE
    RETURN number_2;
  END IF;
END;
$$
;
```

The following is an example of calling the stored procedure:

```sqlexample
CALL return_greater(2, 3);
```

#### Using an argument in a SQL statement (binding)

As is the case with Snowflake Scripting variables, if you need to use an argument in a SQL statement, put a colon (`:`) in front
of the argument name. For more information, see [Using a variable in a SQL statement (binding)](../snowflake-scripting/variables.md).

The following sections contain examples that use bind variables in stored procedures:

* Example that uses a bind variable in a WHERE clause
* Example of using a bind variable to set the value of a property
* Example that uses bind variables to set parameters in a command
* Examples that use a bind variable for an array

##### Example that uses a bind variable in a WHERE clause

The following stored procedure uses the `id` argument in the WHERE clause of a SELECT statement. In the WHERE
clause, the argument is specified as `:id`.

```sqlexample
CREATE OR REPLACE PROCEDURE find_invoice_by_id(id VARCHAR)
RETURNS TABLE (id INTEGER, price NUMBER(12,2))
LANGUAGE SQL
AS
DECLARE
  res RESULTSET DEFAULT (SELECT * FROM invoices WHERE id = :id);
BEGIN
  RETURN TABLE(res);
END;
```

Note: If you use [Snowflake CLI](../snowflake-cli/index.md), [SnowSQL](../../user-guide/snowsql.md), the Classic Console, or the
`execute_stream` or `execute_string` method in [Python Connector](../python-connector/python-connector.md)
code, use this example instead (see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](../snowflake-scripting/running-examples.md)):

```sqlexample
CREATE OR REPLACE PROCEDURE find_invoice_by_id(id VARCHAR)
RETURNS TABLE (id INTEGER, price NUMBER(12,2))
LANGUAGE SQL
AS
$$
DECLARE
  res RESULTSET DEFAULT (SELECT * FROM invoices WHERE id = :id);
BEGIN
  RETURN TABLE(res);
END;
$$
;
```

The following is an example of calling the stored procedure:

```sqlexample
CALL find_invoice_by_id('2');
```

In addition, the [TO_QUERY](../../sql-reference/functions/to_query.md) function provides a simple syntax for accepting a SQL string
directly in the FROM clause of a SELECT statement. For a comparison of the TO_QUERY function with dynamic SQL,
see [Constructing SQL at runtime](../../user-guide/querying-construct-at-runtime.md).

##### Example of using a bind variable to set the value of a property

The following stored procedure uses the `comment` argument to add a comment for a table in a
CREATE TABLE statement. In the statement, the argument is specified as `:comment`.

```sqlexample
CREATE OR REPLACE PROCEDURE test_bind_comment(comment VARCHAR)
RETURNS STRING
LANGUAGE SQL
AS
BEGIN
  CREATE OR REPLACE TABLE test_table_with_comment(a VARCHAR, n NUMBER) COMMENT = :comment;
END;
```

Note: If you use [Snowflake CLI](../snowflake-cli/index.md), [SnowSQL](../../user-guide/snowsql.md), the Classic Console, or the
`execute_stream` or `execute_string` method in [Python Connector](../python-connector/python-connector.md)
code, use this example instead (see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](../snowflake-scripting/running-examples.md)):

```sqlexample
CREATE OR REPLACE PROCEDURE test_bind_comment(comment VARCHAR)
RETURNS STRING
LANGUAGE SQL
AS
$$
BEGIN
  CREATE OR REPLACE TABLE test_table_with_comment(a VARCHAR, n NUMBER) COMMENT = :comment;
END;
$$
;
```

The following is an example of calling the stored procedure:

```sqlexample
CALL test_bind_comment('My Test Table');
```

View the comment for the table by querying the [TABLES view](../../sql-reference/info-schema/tables.md)
in the INFORMATION_SCHEMA:

```sqlexample
SELECT comment FROM information_schema.tables WHERE table_name='TEST_TABLE_WITH_COMMENT';
```

```output
+---------------+
| COMMENT       |
|---------------|
| My Test Table |
+---------------+
```

You can also view the comment by running a [SHOW TABLES](../../sql-reference/sql/show-tables.md) command.

##### Example that uses bind variables to set parameters in a command

Assume you have a stage named `st` with CSV files:

```sqlexample
CREATE OR REPLACE STAGE st;
PUT file://good_data.csv @st;
PUT file://errors_data.csv @st;
```

You want to load the data in the CSV files into a table named `test_bind_stage_and_load`:

```sqlexample
CREATE OR REPLACE TABLE test_bind_stage_and_load (a VARCHAR, b VARCHAR, c VARCHAR);
```

The following stored procedure uses the FROM, ON_ERROR, and VALIDATION_MODE parameters in
a [COPY INTO <table>](../../sql-reference/sql/copy-into-table.md) statement. In the statement, the parameter values are specified as
`:my_stage_name`, `:on_error`, and `:valid_mode`, respectively.

```sqlexample
CREATE OR REPLACE PROCEDURE test_copy_files_validate(
  my_stage_name VARCHAR,
  on_error VARCHAR,
  valid_mode VARCHAR)
RETURNS STRING
LANGUAGE SQL
AS
BEGIN
  COPY INTO test_bind_stage_and_load
    FROM :my_stage_name
    ON_ERROR=:on_error
    FILE_FORMAT=(type='csv')
    VALIDATION_MODE=:valid_mode;
END;
```

Note: If you use [Snowflake CLI](../snowflake-cli/index.md), [SnowSQL](../../user-guide/snowsql.md), the Classic Console, or the
`execute_stream` or `execute_string` method in [Python Connector](../python-connector/python-connector.md)
code, use this example instead (see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](../snowflake-scripting/running-examples.md)):

```sqlexample
CREATE OR REPLACE PROCEDURE test_copy_files_validate(
  my_stage_name VARCHAR,
  on_error VARCHAR,
  valid_mode VARCHAR)
RETURNS STRING
LANGUAGE SQL
AS
$$
BEGIN
  COPY INTO test_bind_stage_and_load
    FROM :my_stage_name
    ON_ERROR=:on_error
    FILE_FORMAT=(type='csv')
    VALIDATION_MODE=:valid_mode;
END;
$$
;
```

The following is an example of calling the stored procedure:

```sqlexample
CALL test_copy_files_validate('@st', 'skip_file', 'return_all_errors');
```

##### Examples that use a bind variable for an array

You can expand a bind variable that represents an [array](../../sql-reference/data-types-semistructured.md) into a list of individual values
by using the spread operator (`**`). For more information and examples, see [Expansion operators](../../sql-reference/operators-expansion.md).

#### Using an argument as an object identifier

If you need to use an argument to refer to an object (for example, a table name in the FROM clause of a SELECT statement), use the
[IDENTIFIER](../../sql-reference/identifier-literal.md) keyword to indicate that the argument represents an object identifier. For
example:

```sqlexample
CREATE OR REPLACE PROCEDURE get_row_count(table_name VARCHAR)
RETURNS INTEGER NOT NULL
LANGUAGE SQL
AS
DECLARE
  row_count INTEGER DEFAULT 0;
  res RESULTSET DEFAULT (SELECT COUNT(*) AS COUNT FROM IDENTIFIER(:table_name));
  c1 CURSOR FOR res;
BEGIN
  FOR row_variable IN c1 DO
    row_count := row_variable.count;
  END FOR;
  RETURN row_count;
END;
```

Note: If you use [Snowflake CLI](../snowflake-cli/index.md), [SnowSQL](../../user-guide/snowsql.md), the Classic Console, or the
`execute_stream` or `execute_string` method in [Python Connector](../python-connector/python-connector.md)
code, use this example instead (see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](../snowflake-scripting/running-examples.md)):

```sqlexample
CREATE OR REPLACE PROCEDURE get_row_count(table_name VARCHAR)
RETURNS INTEGER NOT NULL
LANGUAGE SQL
AS
$$
DECLARE
  row_count INTEGER DEFAULT 0;
  res RESULTSET DEFAULT (SELECT COUNT(*) AS COUNT FROM IDENTIFIER(:table_name));
  c1 CURSOR FOR res;
BEGIN
  FOR row_variable IN c1 DO
    row_count := row_variable.count;
  END FOR;
  RETURN row_count;
END;
$$
;
```

The following is an example of calling the stored procedure:

```sqlexample
CALL get_row_count('invoices');
```

The following example executes a CREATE TABLE … AS SELECT (CTAS) statement in a stored procedure based on
the table names provided in arguments.

```sqlexample
CREATE OR REPLACE PROCEDURE ctas_sp(existing_table VARCHAR, new_table VARCHAR)
  RETURNS TEXT
  LANGUAGE SQL
AS
BEGIN
  CREATE OR REPLACE TABLE IDENTIFIER(:new_table) AS
    SELECT * FROM IDENTIFIER(:existing_table);
  RETURN 'Table created';
END;
```

Note: If you use [Snowflake CLI](../snowflake-cli/index.md), [SnowSQL](../../user-guide/snowsql.md), the Classic Console, or the
`execute_stream` or `execute_string` method in [Python Connector](../python-connector/python-connector.md)
code, use this example instead (see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](../snowflake-scripting/running-examples.md)):

```sqlexample
CREATE OR REPLACE PROCEDURE ctas_sp(existing_table VARCHAR, new_table VARCHAR)
  RETURNS TEXT
  LANGUAGE SQL
AS
$$
BEGIN
  CREATE OR REPLACE TABLE IDENTIFIER(:new_table) AS
    SELECT * FROM IDENTIFIER(:existing_table);
  RETURN 'Table created';
END;
$$
;
```

Before calling the procedure, create a simple table and insert data:

```sqlexample
CREATE OR REPLACE TABLE test_table_for_ctas_sp (
  id NUMBER(2),
  v  VARCHAR(2))
AS SELECT
  column1,
  column2,
FROM
  VALUES
    (1, 'a'),
    (2, 'b'),
    (3, 'c');
```

Call the stored procedure to create a new table that is based on this table:

```sqlexample
CALL ctas_sp('test_table_for_ctas_sp', 'test_table_for_ctas_sp_backup');
```

#### Using an argument when building a string for a SQL statement

Note that if you are building a SQL statement as a string to be passed to
[EXECUTE IMMEDIATE](../../sql-reference/sql/execute-immediate.md) (see [Assigning a query to a declared RESULTSET](../snowflake-scripting/resultsets.md)), do not prefix the argument with a
colon. For example:

```sqlexample
CREATE OR REPLACE PROCEDURE find_invoice_by_id_via_execute_immediate(id VARCHAR)
RETURNS TABLE (id INTEGER, price NUMBER(12,2))
LANGUAGE SQL
AS
DECLARE
  select_statement VARCHAR;
  res RESULTSET;
BEGIN
  select_statement := 'SELECT * FROM invoices WHERE id = ' || id;
  res := (EXECUTE IMMEDIATE :select_statement);
  RETURN TABLE(res);
END;
```

Note: If you use [Snowflake CLI](../snowflake-cli/index.md), [SnowSQL](../../user-guide/snowsql.md), the Classic Console, or the
`execute_stream` or `execute_string` method in [Python Connector](../python-connector/python-connector.md)
code, use this example instead (see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](../snowflake-scripting/running-examples.md)):

```sqlexample
CREATE OR REPLACE PROCEDURE find_invoice_by_id_via_execute_immediate(id VARCHAR)
RETURNS TABLE (id INTEGER, price NUMBER(12,2))
LANGUAGE SQL
AS
$$
DECLARE
  select_statement VARCHAR;
  res RESULTSET;
BEGIN
  select_statement := 'SELECT * FROM invoices WHERE id = ' || id;
  res := (EXECUTE IMMEDIATE :select_statement);
  RETURN TABLE(res);
END;
$$
;
```

#### Using an output argument to return a single value

The following example creates the stored procedure `simple_out_sp_demo` with the output argument `xout` in
its definition. The stored procedure sets the value of `xout` to `2`.

```sqlexample
CREATE OR REPLACE PROCEDURE simple_out_sp_demo(xout OUT NUMBER)
  RETURNS STRING
  LANGUAGE SQL
AS
BEGIN
  xout := 2;
  RETURN 'Done';
END;
```

Note: If you use [Snowflake CLI](../snowflake-cli/index.md), [SnowSQL](../../user-guide/snowsql.md), the Classic Console, or the
`execute_stream` or `execute_string` method in [Python Connector](../python-connector/python-connector.md)
code, use this example instead (see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](../snowflake-scripting/running-examples.md)):

```sqlexample
CREATE OR REPLACE PROCEDURE simple_out_sp_demo(xout OUT NUMBER)
  RETURNS STRING
  LANGUAGE SQL
AS
$$
BEGIN
  xout := 2;
  RETURN 'Done';
END;
$$
;
```

The following anonymous block sets the value of the `x` variable to `1`. Then, it calls the `simple_out_sp_demo`
stored procedure and specifies the variable as the argument.

```sqlexample
BEGIN
  LET x := 1;
  CALL simple_out_sp_demo(:x);
  RETURN x;
END;
```

Note: If you use [Snowflake CLI](../snowflake-cli/index.md), [SnowSQL](../../user-guide/snowsql.md), the Classic Console, or the
`execute_stream` or `execute_string` method in [Python Connector](../python-connector/python-connector.md)
code, use this example instead (see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](../snowflake-scripting/running-examples.md)):

```sqlexample
EXECUTE IMMEDIATE
$$
BEGIN
  LET x := 1;
  CALL simple_out_sp_demo(:x);
  RETURN x;
END;
$$
;
```

The output shows that the `simple_out_sp_demo` stored procedure performed an operation to set the value of the
output argument to `2` and then returned this value to the anonymous block.

```output
+-----------------+
| anonymous block |
|-----------------|
|               2 |
+-----------------+
```

The following anonymous block calls `simple_out_sp_demo` stored procedure and returns an error, because it tries to
assign a value to the output argument using an expression instead of a variable.

```sqlexample
BEGIN
  LET x := 1;
  CALL simple_out_sp_demo(:x + 2);
  RETURN x;
END;
```

Note: If you use [Snowflake CLI](../snowflake-cli/index.md), [SnowSQL](../../user-guide/snowsql.md), the Classic Console, or the
`execute_stream` or `execute_string` method in [Python Connector](../python-connector/python-connector.md)
code, use this example instead (see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](../snowflake-scripting/running-examples.md)):

```sqlexample
EXECUTE IMMEDIATE
$$
BEGIN
  LET x := 1;
  CALL simple_out_sp_demo(:x + 2);
  RETURN x;
END;
$$
;
```

#### Using output arguments to return several values for multiple calls to a stored procedure

The following example demonstrates the following behavior related to stored procedures and
input and output arguments:

* A stored procedure can have several input and output arguments in its definition.
* A program can call a stored procedure with output arguments multiple times, and the values of the
  output arguments are preserved after each call.
* Input arguments don’t return values to the calling program.

Create the stored procedure `multiple_out_sp_demo` with multiple input and output arguments in its
definition. The stored procedure performs the same operations on the equivalent input and output arguments.
For example, the stored procedure adds `1` to the `p1_in` input argument and to the `p1_out` output
argument.

```sqlexample
CREATE OR REPLACE PROCEDURE multiple_out_sp_demo(
    p1_in NUMBER,
    p1_out OUT NUMBER,
    p2_in VARCHAR(100),
    p2_out OUT VARCHAR(100),
    p3_in BOOLEAN,
    p3_out OUT BOOLEAN)
  RETURNS NUMBER
  LANGUAGE SQL
AS
BEGIN
  p1_in := p1_in + 1;
  p1_out := p1_out + 1;
  p2_in := p2_in || ' hi ';
  p2_out := p2_out || ' hi ';
  p3_in := (NOT p3_in);
  p3_out := (NOT p3_out);
  RETURN 1;
END;
```

Note: If you use [Snowflake CLI](../snowflake-cli/index.md), [SnowSQL](../../user-guide/snowsql.md), the Classic Console, or the
`execute_stream` or `execute_string` method in [Python Connector](../python-connector/python-connector.md)
code, use this example instead (see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](../snowflake-scripting/running-examples.md)):

```sqlexample
CREATE OR REPLACE PROCEDURE multiple_out_sp_demo(
    p1_in NUMBER,
    p1_out OUT NUMBER,
    p2_in VARCHAR(100),
    p2_out OUT VARCHAR(100),
    p3_in BOOLEAN,
    p3_out OUT BOOLEAN)
  RETURNS NUMBER
  LANGUAGE SQL
AS
$$
BEGIN
  p1_in := p1_in + 1;
  p1_out := p1_out + 1;
  p2_in := p2_in || ' hi ';
  p2_out := p2_out || ' hi ';
  p3_in := (NOT p3_in);
  p3_out := (NOT p3_out);
  RETURN 1;
END;
$$
;
```

The following anonymous block assigns values to the variables that correspond to the arguments of the
`multiple_out_sp_demo` stored procedure and then calls the stored procedure multiple times. The first
call uses the variable values specified in the anonymous block, but each subsequent call uses the values
returned by the output arguments in the `multiple_out_sp_demo` stored procedure.

```sqlexample
BEGIN
  LET x_in INT := 1;
  LET x_out INT := 1;
  LET y_in VARCHAR(100) := 'hello';
  LET y_out VARCHAR(100) := 'hello';
  LET z_in BOOLEAN := true;
  LET z_out BOOLEAN := true;

  CALL multiple_out_sp_demo(:x_in, :x_out, :y_in, :y_out, :z_in, :z_out);
  CALL multiple_out_sp_demo(:x_in, :x_out, :y_in, :y_out, :z_in, :z_out);
  CALL multiple_out_sp_demo(:x_in, :x_out, :y_in, :y_out, :z_in, :z_out);
  RETURN [x_in, x_out, y_in, y_out, z_in, z_out];
END;
```

Note: If you use [Snowflake CLI](../snowflake-cli/index.md), [SnowSQL](../../user-guide/snowsql.md), the Classic Console, or the
`execute_stream` or `execute_string` method in [Python Connector](../python-connector/python-connector.md)
code, use this example instead (see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](../snowflake-scripting/running-examples.md)):

```sqlexample
EXECUTE IMMEDIATE
$$
BEGIN
  LET x_in INT := 1;
  LET x_out INT := 1;
  LET y_in VARCHAR(100) := 'hello';
  LET y_out VARCHAR(100) := 'hello';
  LET z_in BOOLEAN := true;
  LET z_out BOOLEAN := true;

  CALL multiple_out_sp_demo(:x_in, :x_out, :y_in, :y_out, :z_in, :z_out);
  CALL multiple_out_sp_demo(:x_in, :x_out, :y_in, :y_out, :z_in, :z_out);
  CALL multiple_out_sp_demo(:x_in, :x_out, :y_in, :y_out, :z_in, :z_out);
  RETURN [x_in, x_out, y_in, y_out, z_in, z_out];
END;
$$
;
```

```output
+------------------------+
| anonymous block        |
|------------------------|
| [                      |
|   1,                   |
|   4,                   |
|   "hello",             |
|   "hello hi  hi  hi ", |
|   true,                |
|   false                |
| ]                      |
+------------------------+
```

#### Using an output argument with a different data type than the input value from a calling procedure

For some use cases, there might be a mismatch between the data type of the value being passed in to a stored
procedure and the data type of the procedure’s output argument. In these cases,
[supported coercions](../../sql-reference/data-type-conversion.md) are performed automatically.

> **Note:**
>
> Although coercion is supported in some cases, it isn’t recommended.

This example demonstrates automatic conversion of a FLOAT value that is passed to an output argument with
a NUMBER data type. The FLOAT value is automatically converted to a NUMBER value and then passed back to the
calling anonymous block.

Create the `sp_out_coercion` stored procedure, which takes an output argument of type NUMBER:

```sqlexample
CREATE OR REPLACE PROCEDURE sp_out_coercion(x OUT NUMBER)
  RETURNS STRING
  LANGUAGE SQL
AS
BEGIN
  x := x * 2;
  RETURN 'Done';
END;
```

Note: If you use [Snowflake CLI](../snowflake-cli/index.md), [SnowSQL](../../user-guide/snowsql.md), the Classic Console, or the
`execute_stream` or `execute_string` method in [Python Connector](../python-connector/python-connector.md)
code, use this example instead (see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](../snowflake-scripting/running-examples.md)):

```sqlexample
CREATE OR REPLACE PROCEDURE sp_out_coercion(x OUT NUMBER)
  RETURNS STRING
  LANGUAGE SQL
AS
$$
BEGIN
  x := x * 2;
  RETURN 'Done';
END;
$$
;
```

Execute an anonymous block that passes a FLOAT value to the `sp_out_coercion` stored procedure:

```sqlexample
BEGIN
  LET a FLOAT := 500.662;
  CALL sp_out_coercion(:a);
  RETURN a || ' (Type ' || SYSTEM$TYPEOF(a) || ')';
END;
```

Note: If you use [Snowflake CLI](../snowflake-cli/index.md), [SnowSQL](../../user-guide/snowsql.md), the Classic Console, or the
`execute_stream` or `execute_string` method in [Python Connector](../python-connector/python-connector.md)
code, use this example instead (see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](../snowflake-scripting/running-examples.md)):

```sqlexample
EXECUTE IMMEDIATE
$$
BEGIN
  LET a FLOAT := 500.662;
  CALL sp_out_coercion(:a);
  RETURN a || ' (Type ' || SYSTEM$TYPEOF(a) || ')';
END;
$$
;
```

The output shows both the returned value and the data type of the returned value, by calling the
[SYSTEM$TYPEOF](../../sql-reference/functions/system_typeof.md) function. Note that the value is coerced from a
NUMBER value back to a FLOAT value after it is returned from the stored procedure:

```output
+---------------------------+
| anonymous block           |
|---------------------------|
| 1002 (Type FLOAT[DOUBLE]) |
+---------------------------+
```

#### Using an output argument to return the total sales for an employee in a quarter

This example uses the following `quarterly_sales` table:

```sqlexample
CREATE OR REPLACE TABLE quarterly_sales(
  empid INT,
  amount INT,
  quarter TEXT)
  AS SELECT * FROM VALUES
    (1, 10000, '2023_Q1'),
    (1, 400, '2023_Q1'),
    (2, 4500, '2023_Q1'),
    (2, 35000, '2023_Q1'),
    (1, 5000, '2023_Q2'),
    (1, 3000, '2023_Q2'),
    (2, 200, '2023_Q2'),
    (2, 90500, '2023_Q2'),
    (1, 6000, '2023_Q3'),
    (1, 5000, '2023_Q3'),
    (2, 2500, '2023_Q3'),
    (2, 9500, '2023_Q3'),
    (3, 2700, '2023_Q3'),
    (1, 8000, '2023_Q4'),
    (1, 10000, '2023_Q4'),
    (2, 800, '2023_Q4'),
    (2, 4500, '2023_Q4'),
    (3, 2700, '2023_Q4'),
    (3, 16000, '2023_Q4'),
    (3, 10200, '2023_Q4');
```

Create the stored procedure `sales_total_out_sp_demo` that takes two input arguments for the
employee identifier and quarter, and one output argument to calculate the sales total for the
given employee and quarter.

```sqlexample
CREATE OR REPLACE PROCEDURE sales_total_out_sp_demo(
    id INT,
    quarter VARCHAR(20),
    total_sales OUT NUMBER(38,0))
  RETURNS STRING
  LANGUAGE SQL
AS
$$
BEGIN
  SELECT SUM(amount) INTO total_sales FROM quarterly_sales
    WHERE empid = :id AND
          quarter = :quarter;
  RETURN 'Done';
END;
$$
;
```

Create the stored procedure `emp_quarter_calling_sp_demo` that calls the `sales_total_out_sp_demo`
stored procedure. This stored procedure also takes two input arguments for the employee identifier and quarter.

```sqlexample
CREATE OR REPLACE PROCEDURE emp_quarter_calling_sp_demo(
    id INT,
    quarter VARCHAR(20))
  RETURNS STRING
  LANGUAGE SQL
AS
BEGIN
  LET x NUMBER(38,0);
  CALL sales_total_out_sp_demo(:id, :quarter, :x);
  RETURN 'Total sales for employee ' || id || ' in quarter ' || quarter || ': ' || x;
END;
```

Note: If you use [Snowflake CLI](../snowflake-cli/index.md), [SnowSQL](../../user-guide/snowsql.md), the Classic Console, or the
`execute_stream` or `execute_string` method in [Python Connector](../python-connector/python-connector.md)
code, use this example instead (see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](../snowflake-scripting/running-examples.md)):

```sqlexample
CREATE OR REPLACE PROCEDURE emp_quarter_calling_sp_demo(
    id INT,
    quarter VARCHAR(20))
  RETURNS STRING
  LANGUAGE SQL
AS
$$
BEGIN
  LET x NUMBER(38,0);
  CALL sales_total_out_sp_demo(:id, :quarter, :x);
  RETURN 'Total sales for employee ' || id || ' in quarter ' || quarter || ': ' || x;
END;
$$
;
```

Call the `emp_quarter_calling_sp_demo` with the arguments `2` (for the employee identifier) and
`'2023_Q4'` (for the quarter).

```sqlexample
CALL emp_quarter_calling_sp_demo(2, '2023_Q4');
```

```output
+-----------------------------------------------------+
| emp_quarter_calling_sp_demo                         |
|-----------------------------------------------------|
| Total sales for employee 2 in quarter 2023_Q4: 5300 |
+-----------------------------------------------------+
```

## Returning tabular data

If you need to return tabular data (for example, data from a RESULTSET) from your stored procedure, specify
RETURNS TABLE(…) in your [CREATE PROCEDURE](../../sql-reference/sql/create-procedure.md) statement.

If you know the [Snowflake data types](../../sql-reference-data-types.md) of the columns in the returned table, specify the column
names and types in the RETURNS TABLE().

```sqlexample
CREATE OR REPLACE PROCEDURE get_top_sales()
RETURNS TABLE (sales_date DATE, quantity NUMBER)
...
```

Otherwise (for example, if you are determining the column types during run time), you can omit the column names and types:

```sqlexample
CREATE OR REPLACE PROCEDURE get_top_sales()
RETURNS TABLE ()
...
```

> **Note:**
>
> Currently, in the `RETURNS TABLE(...)` clause, you can’t specify GEOGRAPHY as a column type. This
> applies whether you are creating a stored or anonymous procedure.
>
> ```sqlexample
> CREATE OR REPLACE PROCEDURE test_return_geography_table_1()
>   RETURNS TABLE(g GEOGRAPHY)
>   ...
> ```
>
> ```sqlexample
> WITH test_return_geography_table_1() AS PROCEDURE
>   RETURNS TABLE(g GEOGRAPHY)
>   ...
> CALL test_return_geography_table_1();
> ```
>
> If you attempt to specify GEOGRAPHY as a column type, calling the stored procedure results in the error:
>
> ```none
> Stored procedure execution error: data type of returned table does not match expected returned table type
> ```
>
> To work around this issue, you can omit the column arguments and types in `RETURNS TABLE()`.
>
> ```sqlexample
> CREATE OR REPLACE PROCEDURE test_return_geography_table_1()
>   RETURNS TABLE()
>   ...
> ```
>
> ```sqlexample
> WITH test_return_geography_table_1() AS PROCEDURE
>   RETURNS TABLE()
>   ...
> CALL test_return_geography_table_1();
> ```

If you need to return the data in a RESULTSET, use TABLE() in your
[RETURN](../../sql-reference/snowflake-scripting/return.md) statement.

For example:

```sqlexample
CREATE OR REPLACE PROCEDURE get_top_sales()
RETURNS TABLE (sales_date DATE, quantity NUMBER)
LANGUAGE SQL
AS
DECLARE
  res RESULTSET DEFAULT (SELECT sales_date, quantity FROM sales ORDER BY quantity DESC LIMIT 10);
BEGIN
  RETURN TABLE(res);
END;
```

Note: If you use [Snowflake CLI](../snowflake-cli/index.md), [SnowSQL](../../user-guide/snowsql.md), the Classic Console, or the
`execute_stream` or `execute_string` method in [Python Connector](../python-connector/python-connector.md)
code, use this example instead (see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](../snowflake-scripting/running-examples.md)):

```sqlexample
CREATE OR REPLACE PROCEDURE get_top_sales()
RETURNS TABLE (sales_date DATE, quantity NUMBER)
LANGUAGE SQL
AS
$$
DECLARE
  res RESULTSET DEFAULT (SELECT sales_date, quantity FROM sales ORDER BY quantity DESC LIMIT 10);
BEGIN
  RETURN TABLE(res);
END;
$$
;
```

The following is an example of calling the stored procedure:

```sqlexample
CALL get_top_sales();
```

## Calling a stored procedure from another stored procedure

In a stored procedure, if you need to call another stored procedure, use one of the following approaches:

* Calling a stored procedure without using the returned value
* Using the value returned from a stored procedure call
* Passing output argument values from a stored procedure to a calling stored procedure

### Calling a stored procedure without using the returned value

Use a [CALL](../../sql-reference/sql/call.md) statement to call the stored procedure (as you normally would).

If you need to pass in any variables or arguments as input arguments in the CALL statement, remember to use a colon (`:`) in
front of the variable name. (See [Using a variable in a SQL statement (binding)](../snowflake-scripting/variables.md).)

The following is an example of a stored procedure that calls another stored procedure but does not depend on the return value.

First, create a table for use in the example:

```sqlexample
-- Create a table for use in the example.
CREATE OR REPLACE TABLE int_table (value INTEGER);
```

Then, create the stored procedure that you will call from another stored procedure:

```sqlexample
-- Create a stored procedure to be called from another stored procedure.
CREATE OR REPLACE PROCEDURE insert_value(value INTEGER)
RETURNS VARCHAR NOT NULL
LANGUAGE SQL
AS
BEGIN
  INSERT INTO int_table VALUES (:value);
  RETURN 'Rows inserted: ' || SQLROWCOUNT;
END;
```

Note: If you use [Snowflake CLI](../snowflake-cli/index.md), [SnowSQL](../../user-guide/snowsql.md), the Classic Console, or the
`execute_stream` or `execute_string` method in [Python Connector](../python-connector/python-connector.md)
code, use this example instead (see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](../snowflake-scripting/running-examples.md)):

```sqlexample
-- Create a stored procedure to be called from another stored procedure.
CREATE OR REPLACE PROCEDURE insert_value(value INTEGER)
RETURNS VARCHAR NOT NULL
LANGUAGE SQL
AS
$$
BEGIN
  INSERT INTO int_table VALUES (:value);
  RETURN 'Rows inserted: ' || SQLROWCOUNT;
END;
$$
;
```

Next, create a second stored procedure that calls the first stored procedure:

```sqlexample
CREATE OR REPLACE PROCEDURE insert_two_values(value1 INTEGER, value2 INTEGER)
RETURNS VARCHAR NOT NULL
LANGUAGE SQL
AS
BEGIN
  CALL insert_value(:value1);
  CALL insert_value(:value2);
  RETURN 'Finished calling stored procedures';
END;
```

Note: If you use [Snowflake CLI](../snowflake-cli/index.md), [SnowSQL](../../user-guide/snowsql.md), the Classic Console, or the
`execute_stream` or `execute_string` method in [Python Connector](../python-connector/python-connector.md)
code, use this example instead (see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](../snowflake-scripting/running-examples.md)):

```sqlexample
CREATE OR REPLACE PROCEDURE insert_two_values(value1 INTEGER, value2 INTEGER)
RETURNS VARCHAR NOT NULL
LANGUAGE SQL
AS
$$
BEGIN
  CALL insert_value(:value1);
  CALL insert_value(:value2);
  RETURN 'Finished calling stored procedures';
END;
$$
;
```

Finally, call the second stored procedure:

```sqlexample
CALL insert_two_values(4, 5);
```

### Using the value returned from a stored procedure call

If you are calling a stored procedure that returns a scalar value, and you need to access that value, use the
`INTO :snowflake_scripting_variable` clause in the [CALL](../../sql-reference/sql/call.md) statement to capture the value in a
[Snowflake Scripting variable](../snowflake-scripting/variables.md).

The following example calls the `get_row_count` stored procedure that was defined in
Using an argument as an object identifier.

```sqlexample
CREATE OR REPLACE PROCEDURE count_greater_than(table_name VARCHAR, maximum_count INTEGER)
  RETURNS BOOLEAN NOT NULL
  LANGUAGE SQL
  AS
  DECLARE
    count1 NUMBER;
  BEGIN
    CALL get_row_count(:table_name) INTO :count1;
    IF (:count1 > maximum_count) THEN
      RETURN TRUE;
    ELSE
      RETURN FALSE;
    END IF;
  END;
```

Note: If you use [Snowflake CLI](../snowflake-cli/index.md), [SnowSQL](../../user-guide/snowsql.md), the Classic Console, or the
`execute_stream` or `execute_string` method in [Python Connector](../python-connector/python-connector.md)
code, use this example instead (see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](../snowflake-scripting/running-examples.md)):

```sqlexample
CREATE OR REPLACE PROCEDURE count_greater_than(table_name VARCHAR, maximum_count INTEGER)
  RETURNS BOOLEAN NOT NULL
  LANGUAGE SQL
  AS
  $$
  DECLARE
    count1 NUMBER;
  BEGIN
    CALL get_row_count(:table_name) INTO :count1;
    IF (:count1 > maximum_count) THEN
      RETURN TRUE;
    ELSE
      RETURN FALSE;
    END IF;
  END;
  $$
  ;
```

The following is an example of calling the stored procedure:

```sqlexample
CALL count_greater_than('invoices', 3);
```

If the stored procedure returns a table, you can capture the return value by setting a
[RESULTSET](../snowflake-scripting/resultsets.md) to a string containing the CALL statement. (See
[Assigning a query to a declared RESULTSET](../snowflake-scripting/resultsets.md).)

To retrieve the return value from the call, you can use a
[CURSOR for the RESULTSET](../snowflake-scripting/resultsets.md). For example:

```sqlexample
DECLARE
  res1 RESULTSET;
BEGIN
res1 := (CALL my_procedure());
LET c1 CURSOR FOR res1;
FOR row_variable IN c1 DO
  IF (row_variable.col1 > 0) THEN
    ...;
  ELSE
    ...;
  END IF;
END FOR;
...
```

### Passing output argument values from a stored procedure to a calling stored procedure

When an output argument is specified in the definition of a Snowflake Scripting stored procedure, the stored procedure
can return the current value of the output argument to a calling stored procedure. The stored procedure takes an initial value
for the output argument, saves the value to a variable in the procedure body, and optionally performs operations to change the
value of the variable. The stored procedure then returns the updated value to the calling stored procedure.

For an example, see Using an output argument to return the total sales for an employee in a quarter.

## Using nested stored procedures

A *nested stored procedure* is a stored procedure that’s defined within the scope of an anonymous block or
a block in another stored procedure (the *parent stored procedure*).

You declare a nested stored procedure in the [DECLARE](../../sql-reference/snowflake-scripting/declare.md) section
of a block, which can be part of a [CREATE PROCEDURE](../../sql-reference/sql/create-procedure.md) statement. The following example
shows a nested stored procedure declaration:

```sqlsyntax
DECLARE
  <nested_stored_procedure_name> PROCEDURE (<arguments>)
     RETURNS <data_type>
     AS
     BEGIN
       <nested_procedure_procedure_statements>
     END;
BEGIN
  <statements>
END;
```

For information about the declaration syntax of a nested stored procedure, see
[Nested stored procedure declaration syntax](../../sql-reference/snowflake-scripting/declare.md).

A nested stored procedure only exists within the scope of its [block](../snowflake-scripting/blocks.md).
It can be called from any section of its block (DECLARE, BEGIN … END, and EXCEPTION). A single block can contain
multiple nested stored procedures, and one nested stored procedure can call another nested stored procedure in the
same block. A nested procedure can’t be called or accessed from outside of its block.

A nested stored procedure operates in the same security context as the block that defines it. When a nested stored
procedure is defined in a parent stored procedure, it automatically runs with the same privileges as the parent
stored procedure.

> **Note:**
>
> Both a nested stored procedure declaration and the [CALL WITH](../../sql-reference/sql/call-with.md) command
> create a temporary stored procedure with limited scope. They differ in the following ways:
>
> * A CALL WITH statement can appear anywhere that a SQL statement can, including within a stored procedure, but a
>   nested stored procedure declaration must be in a Snowflake Scripting block.
> * A CALL WITH stored procedure only exists in the scope of its statement, but a nested stored procedure exists in
>   the scope of its Snowflake Scripting block.

### Benefits of nested stored procedures

Nested stored procedures provide the following benefits:

* They can enhance and simplify security by encapsulating logic inside an anonymous block or parent stored procedure,
  which prevents access to it from outside the block or parent.
* They keep code modular by splitting it logically into smaller chunks, which can make it easier to maintain and
  debug.
* They improve maintainability by reducing the need for global variables or additional arguments, because a nested stored
  procedure can directly access the local variables of its block.

### Usage notes for calling nested stored procedures

The following usage notes apply to calling a nested stored procedure:

* To pass arguments to a nested stored procedure, a block can use constant values,
  [Snowflake Scripting variables](../snowflake-scripting/variables.md),
  [bind variables](../../sql-reference/bind-variables.md), [SQL (session) variables](../../sql-reference/session-variables.md),
  and calls to [user-defined functions](../udf/udf-overview.md).
* When there is a mismatch between the data type of the value being passed in and the data type of an argument,
  Snowflake performs supported coercions automatically. For information about which coercions Snowflake can perform
  automatically, see [Data type conversion](../../sql-reference/data-type-conversion.md).

### Usage notes for variables in a nested stored procedure

The following usage notes apply to variables in a nested stored procedure:

* A nested stored procedure can reference variables from its block that were declared before the nested
  stored procedure declaration in the DECLARE section of its block. It can’t reference variables declared
  after it in the DECLARE section.
* A nested stored procedure can’t access variables declared in a LET statement in the BEGIN … END
  section of a block.
* The value of a referenced variable reflects its value at the time when the nested stored procedure is called.
* A nested stored procedure can modify a referenced variable value, and the modified value persists in the block
  and across multiple invocations of the same nested procedure in a single execution
  of its anonymous block or in a single call to its parent stored procedure.
* The value of a variable that was declared before a nested stored procedure call can be passed as an argument to
  the nested stored procedure. The variable value can be passed as an argument in a call even if the variable
  was declared after the nested stored procedure declaration or in a LET statement.

For example, the following stored procedure declares several variables:

```sqlexample
CREATE OR REPLACE PROCEDURE outer_sp ()
RETURNS NUMBER
LANGUAGE SQL
AS
$$
DECLARE
  var_before_nested_proc NUMBER DEFAULT 1;
  test_nested_variables PROCEDURE(arg1 NUMBER)
    -- <nested_sp_logic>
  var_after_nested_proc NUMBER DEFAULT 2;
BEGIN
  LET var_let_before_call NUMBER DEFAULT 3;
  LET result := CALL nested_proc(:<var_name>);
  LET var_let_after_call NUMBER DEFAULT 3;
  RETURN result;
END;
$$;
```

In this example, only `var_before_nested_proc` can be referenced in `nested_sp_logic`.

In the nested stored procedure call, the value of any of the following variables can be passed to the nested stored
procedure as an argument in `var_name`:

* `var_before_nested_proc`
* `var_after_nested_proc`
* `var_let_before_call`

The value of `var_let_after_call` can’t be passed to the nested stored procedure as an argument.

### Limitations for nested stored procedures

The following limitations apply to defining nested stored procedures:

* They can’t be defined inside other nested stored procedures or inside control structures, such as
  FOR or WHILE loops.
* Each nested stored procedure must have a unique name in its block. That is, nested stored procedures can’t
  be overloaded.
* They don’t support output (OUT) arguments.
* They don’t support optional arguments with default values.

The following limitations apply to calling nested stored procedures:

* They can’t be called in an [EXECUTE IMMEDIATE](../../sql-reference/sql/execute-immediate.md) statement.
* They can’t be called in [asynchronous child jobs](../snowflake-scripting/asynchronous-child-jobs.md).
* They don’t support named input arguments (`arg_name => arg`). Arguments must be
  specified by position. For more information, see [CALL](../../sql-reference/sql/call.md).

### Examples of nested stored procedures

The following examples use nested stored procedures:

* Define a nested stored procedure that returns tabular data
* Define a nested stored procedure that returns a scalar value
* Define a nested stored procedure in an anonymous block
* Define a nested stored procedure that is passed arguments
* Define a nested stored procedure that calls another nested stored procedure

#### Define a nested stored procedure that returns tabular data

The following example defines a nested stored procedure that returns a tabular data. The example creates a
parent stored procedure called `nested_procedure_example_table` with a nested stored procedure
called `nested_return_table`. The code includes the following logic:

* Declares a variable called `res` of type RESULTSET.
* Includes the following logic in the nested stored procedure:

  * Declares a variable called `res2`.
  * Inserts values into a table called `nested_table`.
  * Sets the `res2` variable to the results of a SELECT on the table.
  * Returns the tabular data in the result set.
* Creates the table `nested_table` in the parent stored procedure.
* Calls the nested stored procedure `nested_return_table` and sets the `res` variable to the results of the call
  to the nested stored procedure.
* Returns the tabular results in the `res` variable.

```sqlexample
CREATE OR REPLACE PROCEDURE nested_procedure_example_table()
RETURNS TABLE()
LANGUAGE SQL
AS
$$
DECLARE
  res RESULTSET;
  nested_return_table PROCEDURE()
    RETURNS TABLE()
    AS
    DECLARE
      res2 RESULTSET;
    BEGIN
      INSERT INTO nested_table VALUES(1);
      INSERT INTO nested_table VALUES(2);
      res2 := (SELECT * FROM nested_table);
      RETURN TABLE(res2);
    END;
BEGIN
  CREATE OR REPLACE TABLE nested_table(col1 INT);
  res := (CALL nested_return_table());
  RETURN TABLE(res);
END;
$$;
```

Call the stored procedure:

```sqlexample
CALL nested_procedure_example_table();
```

```output
+------+
| COL1 |
|------|
|    1 |
|    2 |
+------+
```

#### Define a nested stored procedure that returns a scalar value

The following example defines a nested stored procedure that returns a scalar value. The example creates a
parent stored procedure called `nested_procedure_example_scalar` with a nested stored procedure
called `simple_counter`. The code includes the following logic:

* Declares a variable called `counter` of type NUMBER, and sets the value of this variable to `0`.
* Specifies that the nested stored procedure adds `1` to the current value of the `counter` variable.
* Calls the nested stored procedure three times in the parent stored procedure. The value of the `counter`
  variable is carried over between invocations of the nested stored procedure.
* Returns the value of the `counter` variable, which is `3`.

```sqlexample
CREATE OR REPLACE PROCEDURE nested_procedure_example_scalar()
RETURNS VARCHAR
LANGUAGE SQL
AS
$$
DECLARE
  counter NUMBER := 0;
  simple_counter PROCEDURE()
    RETURNS VARCHAR
    AS
    BEGIN
      counter := counter + 1;
      RETURN counter;
    END;
BEGIN
  CALL simple_counter();
  CALL simple_counter();
  CALL simple_counter();
  RETURN counter;
END;
$$;
```

Call the stored procedure:

```sqlexample
CALL nested_procedure_example_scalar();
```

```output
+---------------------------------+
| NESTED_PROCEDURE_EXAMPLE_SCALAR |
|---------------------------------|
| 3                               |
+---------------------------------+
```

#### Define a nested stored procedure in an anonymous block

The following example is the same as the example in Define a nested stored procedure that returns a scalar value,
except that it defines a nested stored procedure in an anonymous block instead of a stored procedure:

```sqlexample
EXECUTE IMMEDIATE $$
DECLARE
  counter NUMBER := 0;
  simple_counter PROCEDURE()
    RETURNS VARCHAR
    AS
    BEGIN
      counter := counter + 1;
      RETURN counter;
    END;
BEGIN
  CALL simple_counter();
  CALL simple_counter();
  CALL simple_counter();
  RETURN counter;
END;
$$;
```

```output
+-----------------+
| anonymous block |
|-----------------|
|               3 |
+-----------------+
```

#### Define a nested stored procedure that is passed arguments

The following example defines a nested stored procedure that is passed arguments. In the example, the nested
stored procedure inserts values into the following table:

```sqlexample
CREATE OR REPLACE TABLE log_nested_values(col1 INT, col2 INT);
```

The example creates a parent stored procedure called `nested_procedure_example_arguments` with a nested stored procedure
called `log_and_multiply_numbers`. The nested stored procedure takes two arguments of type NUMBER. The code includes the
following logic:

* Declares variables `a`, `b`, and `x` of type NUMBER.
* Includes a nested stored procedure that performs the following actions:

  * Inserts the two number values passed to it by the parent stored procedure into the `log_nested_values` table
    using bind variables.
  * Sets the value of variable `x` to the result of multiplying the two argument values.
  * Returns the value of `x` to the parent stored procedure.
* Sets the value of variable `a` to `5` and variable `b` to `10`.
* Calls the nested stored procedure.
* Returns the value of the `x` variable, which was set in the nested stored procedure.

```sqlexample
CREATE OR REPLACE PROCEDURE nested_procedure_example_arguments()
RETURNS NUMBER
LANGUAGE SQL
AS
$$
DECLARE
  a NUMBER;
  b NUMBER;
  x NUMBER;
  log_and_multiply_numbers PROCEDURE(num1 NUMBER, num2 NUMBER)
    RETURNS NUMBER
    AS
    BEGIN
      INSERT INTO log_nested_values VALUES(:num1, :num2);
      x := :num1 * :num2;
      RETURN x;
    END;
BEGIN
  a := 5;
  b := 10;
  CALL log_and_multiply_numbers(:a, :b);
  RETURN x;
END;
$$;
```

Call the stored procedure:

```sqlexample
CALL nested_procedure_example_arguments();
```

```output
+------------------------------------+
| NESTED_PROCEDURE_EXAMPLE_ARGUMENTS |
|------------------------------------|
|                                 50 |
+------------------------------------+
```

Query the `log_nested_values` table to confirm that the nested stored procedure inserted the
values passed to it:

```sqlexample
SELECT * FROM log_nested_values;
```

```output
+------+------+
| COL1 | COL2 |
|------+------|
|    5 |   10 |
+------+------+
```

#### Define a nested stored procedure that calls another nested stored procedure

The following example defines a nested stored procedure that calls another nested stored procedure. The example creates a
parent stored procedure called `nested_procedure_example_call_from_nested` with two nested stored procedures
called `counter_nested_proc` and `call_counter_nested_proc`. The code includes the following logic:

* Declares a variable called `counter` of type NUMBER, and sets the value of this variable to `0`.
* Includes the nested stored procedure `counter_nested_proc` that adds `10` to the value of `counter`.
* Includes the nested stored procedure `call_counter_nested_proc` that adds `15` to the value of `counter`
  and also calls `counter_nested_proc` (which adds another `10` to the value of `counter`).
* Calls both nested stored procedures in the parent stored procedure.
* Returns the value of the `counter` variable, which is `35`.

```sqlexample
CREATE OR REPLACE PROCEDURE nested_procedure_example_call_from_nested()
RETURNS NUMBER
LANGUAGE SQL
AS
$$
DECLARE
  counter NUMBER := 0;
  counter_nested_proc PROCEDURE()
    RETURNS NUMBER
    AS
    DECLARE
      var1 NUMBER := 10;
    BEGIN
      counter := counter + var1;
    END;
  call_counter_nested_proc PROCEDURE()
    RETURNS NUMBER
    AS
    DECLARE
      var2 NUMBER := 15;
    BEGIN
      counter := counter + var2;
      CALL counter_nested_proc();
    END;
BEGIN
  counter := 0;
  CALL counter_nested_proc();
  CALL call_counter_nested_proc();
  RETURN counter;
END;
$$;
```

Call the stored procedure:

```sqlexample
CALL nested_procedure_example_call_from_nested();
```

```output
+-------------------------------------------+
| NESTED_PROCEDURE_EXAMPLE_CALL_FROM_NESTED |
|-------------------------------------------|
|                                        35 |
+-------------------------------------------+
```

## Using and setting SQL variables in a stored procedure

By default, Snowflake Scripting stored procedures run with owner’s rights. When a
stored procedure runs with owner’s rights, it can’t access
[SQL (or session) variables](../../sql-reference/session-variables.md).

However, a caller’s rights stored procedure can read the caller’s session variables and use
them in the logic of the stored procedure. For example, a caller’s rights stored procedure
can use the value in a SQL variable in a query. To create a stored procedure that runs with
caller’s rights, specify the `EXECUTE AS CALLER` parameter in the
[CREATE PROCEDURE](../../sql-reference/sql/create-procedure.md) statement.

These examples illustrate this key difference between caller’s rights and owner’s rights stored
procedures. They attempt to use SQL variables in two ways:

* Set a SQL variable before calling the stored procedure, then use the SQL variable inside the stored
  procedure.
* Set a SQL variable inside the stored procedure, then use the SQL variable after returning from the stored
  procedure.

Both using the SQL variable and setting the SQL variable work correctly in a caller’s rights stored procedure.
Both fail when using an owner’s rights stored procedure, even if the caller is the owner.

For more information about owner’s rights and caller’s rights, see [Understanding caller’s rights and owner’s rights stored procedures](stored-procedures-rights.md).

### Using a SQL variable in a stored procedure

The following example uses a SQL variable in a stored procedure.

First, set a SQL variable in a session:

```sqlexample
SET example_use_variable = 2;
```

Create a simple stored procedure that runs with caller’s rights and uses this SQL variable:

```sqlexample
CREATE OR REPLACE PROCEDURE use_sql_variable_proc()
RETURNS NUMBER
LANGUAGE SQL
EXECUTE AS CALLER
AS
DECLARE
  sess_var_x_2 NUMBER;
BEGIN
  sess_var_x_2 := 2 * $example_use_variable;
  RETURN sess_var_x_2;
END;
```

Note: If you use [Snowflake CLI](../snowflake-cli/index.md), [SnowSQL](../../user-guide/snowsql.md), the Classic Console, or the
`execute_stream` or `execute_string` method in [Python Connector](../python-connector/python-connector.md)
code, use this example instead (see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](../snowflake-scripting/running-examples.md)):

```sqlexample
CREATE OR REPLACE PROCEDURE use_sql_variable_proc()
RETURNS NUMBER
LANGUAGE SQL
EXECUTE AS CALLER
AS
$$
DECLARE
  sess_var_x_2 NUMBER;
BEGIN
  sess_var_x_2 := 2 * $example_use_variable;
  RETURN sess_var_x_2;
END;
$$
;
```

Call the stored procedure:

```sqlexample
CALL use_sql_variable_proc();
```

```output
+-----------------------+
| USE_SQL_VARIABLE_PROC |
|-----------------------|
|                     4 |
+-----------------------+
```

Set the SQL variable to a different value:

```sqlexample
SET example_use_variable = 9;
```

Call the procedure again to see that the returned value has changed:

```sqlexample
CALL use_sql_variable_proc();
```

```output
+-----------------------+
| USE_SQL_VARIABLE_PROC |
|-----------------------|
|                    18 |
+-----------------------+
```

### Setting a SQL variable in a stored procedure

You can set a SQL variable in a stored procedure that’s running with caller’s rights. For
more information, including guidelines for using SQL variables in stored procedures, see
[Caller’s rights stored procedures](stored-procedures-rights.md).

> **Note:**
>
> Although you can set a SQL variable inside a stored procedure and leave it set after the end of the procedure,
> Snowflake does not recommend doing this.

The following example sets a SQL variable in a stored procedure.

First, set a SQL variable in a session:

```sqlexample
SET example_set_variable = 55;
```

Confirm the value of the SQL variable:

```sqlexample
SHOW VARIABLES LIKE 'example_set_variable';
```

```output
+----------------+-------------------------------+-------------------------------+----------------------+-------+-------+---------+
|     session_id | created_on                    | updated_on                    | name                 | value | type  | comment |
|----------------+-------------------------------+-------------------------------+----------------------+-------+-------+---------|
| 10363782631910 | 2024-11-27 08:18:32.007 -0800 | 2024-11-27 08:20:17.255 -0800 | EXAMPLE_SET_VARIABLE | 55    | fixed |         |
+----------------+-------------------------------+-------------------------------+----------------------+-------+-------+---------+
```

For example, the following stored procedure sets the SQL variable `example_set_variable`
to a new value and returns the new value:

```sqlexample
CREATE OR REPLACE PROCEDURE set_sql_variable_proc()
RETURNS NUMBER
LANGUAGE SQL
EXECUTE AS CALLER
AS
BEGIN
  SET example_set_variable = $example_set_variable - 3;
  RETURN $example_set_variable;
END;
```

Note: If you use [Snowflake CLI](../snowflake-cli/index.md), [SnowSQL](../../user-guide/snowsql.md), the Classic Console, or the
`execute_stream` or `execute_string` method in [Python Connector](../python-connector/python-connector.md)
code, use this example instead (see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](../snowflake-scripting/running-examples.md)):

```sqlexample
CREATE OR REPLACE PROCEDURE set_sql_variable_proc()
RETURNS NUMBER
LANGUAGE SQL
EXECUTE AS CALLER
AS
$$
BEGIN
  SET example_set_variable = $example_set_variable - 3;
  RETURN $example_set_variable;
END;
$$
;
```

Call the stored procedure:

```sqlexample
CALL set_sql_variable_proc();
```

```output
+-----------------------+
| SET_SQL_VARIABLE_PROC |
|-----------------------|
|                    52 |
+-----------------------+
```

Confirm the new value of the SQL variable:

```sqlexample
SHOW VARIABLES LIKE 'example_set_variable';
```

```output
+----------------+-------------------------------+-------------------------------+----------------------+-------+-------+---------+
|     session_id | created_on                    | updated_on                    | name                 | value | type  | comment |
|----------------+-------------------------------+-------------------------------+----------------------+-------+-------+---------|
| 10363782631910 | 2024-11-27 08:18:32.007 -0800 | 2024-11-27 08:24:04.027 -0800 | EXAMPLE_SET_VARIABLE | 52    | fixed |         |
+----------------+-------------------------------+-------------------------------+----------------------+-------+-------+---------+
```
