# Source: https://docs.snowflake.com/en/sql-reference/snowflake-scripting/declare.md

# DECLARE (Snowflake Scripting)

Declares one or more Snowflake Scripting variables, cursors, RESULTSETs, nested stored procedures, or exceptions.

For more information, see the following topics:

* [Working with variables](../../developer-guide/snowflake-scripting/variables.md)
* [Working with cursors](../../developer-guide/snowflake-scripting/cursors.md)
* [Working with RESULTSETs](../../developer-guide/snowflake-scripting/resultsets.md)
* [Using nested stored procedures](../../developer-guide/stored-procedure/stored-procedures-snowflake-scripting.md)
* [Handling exceptions](../../developer-guide/snowflake-scripting/exceptions.md)

See also:
:   [LET](let.md)

## Syntax

```sqlsyntax
DECLARE
  {   <variable_declaration>
    | <cursor_declaration>
    | <resultset_declaration>
    | <nested_stored_procedure_declaration>
    | <exception_declaration> };
  [
    {   <variable_declaration>
      | <cursor_declaration>
      | <resultset_declaration>
      | <nested_stored_procedure_declaration>
      | <exception_declaration> };
    ...
  ]
```

The following sections describe the syntax for each type of declaration in more detail:

* Variable declaration syntax
* Cursor declaration syntax
* RESULTSET declaration syntax
* Nested stored procedure declaration syntax
* Exception declaration syntax

### Variable declaration syntax

Use the following syntax to declare a [variable](../../developer-guide/snowflake-scripting/variables.md):

```sqlsyntax
<variable_declaration> ::=
  <variable_name> [<type>] [ { DEFAULT | := } <expression>]
```

Where:

> `variable_name`
> :   The name of the variable. The name must follow the naming rules for [Object identifiers](../identifiers.md).
>
> `type`
> :   A [SQL data type](../../sql-reference-data-types.md).
>
> `DEFAULT expression` or . `:= expression`
> :   Assigns the value of `expression` to the variable. If both `type` and `expression` are specified, the
> expression must evaluate to a data type that matches, or can be implicitly [cast](../functions/cast.md) to, the
> specified `type`.

For example:

> ```sqlexample
> profit NUMBER(38, 2) := 0;
> ```

For a complete example, see Examples.

For more information about variables, see [Working with variables](../../developer-guide/snowflake-scripting/variables.md).

### Cursor declaration syntax

Use the following syntax to declare a [cursor](../../developer-guide/snowflake-scripting/cursors.md):

```sqlsyntax
<cursor_declaration> ::=
  <cursor_name> CURSOR FOR <query>
```

Where:

> `cursor_name`
> :   The name to give the cursor. This can be any valid Snowflake [identifier](../identifiers.md)
> that is not already in use in this block. The identifier is used by other cursor-related commands, such as
> `FETCH`.
>
> `query`
> :   The query that defines the result set that the cursor iterates over.
>
>     This can be almost any valid SELECT statement. To specify bind parameters in the SELECT statement, use
>     question marks (`?`). You can bind the parameters to bind variables in the USING clause when you
>     open the cursor.

For example:

> ```sqlexample
> c1 CURSOR FOR SELECT id, price FROM invoices;
> ```

For more information about cursors (including complete examples), see [Working with cursors](../../developer-guide/snowflake-scripting/cursors.md).

### RESULTSET declaration syntax

Use the following syntax to declare a [RESULTSET](../../developer-guide/snowflake-scripting/resultsets.md):

```sqlsyntax
<resultset_name> RESULTSET [ { DEFAULT | := } [ ASYNC ] ( <query> ) ] ;
```

Where:

> `resultset_name`
> :   The name to give the RESULTSET.
>
>     The name should be unique within the current scope.
>
>     The name must follow the naming rules for [Object identifiers](../identifiers.md).
>
> `ASYNC`
> :   Runs the query as an [asynchronous child job](../../developer-guide/snowflake-scripting/asynchronous-child-jobs.md).
>
>     The query can be any valid SQL statement, including SELECT statements and DML statements, such as INSERT
>     or UPDATE.
>
>     When this keyword is omitted, the stored procedure runs child jobs sequentially, and each child job waits for
>     the running child job to finish before it starts.
>
>     You can use this keyword to run multiple child jobs concurrently, which can improve efficiency and reduce overall
>     run time.
>
>     You can use [AWAIT](await.md) and [CANCEL](cancel.md)
>     statements to manage asynchronous child jobs for a RESULTSET.
>
> `DEFAULT query` or . `:= query`
> :   Assigns the value of `query` to the RESULTSET.

For example:

```sqlexample
res RESULTSET DEFAULT (SELECT col1 FROM mytable ORDER BY col1);
```

For more information about RESULTSETs (including complete examples), see [Working with RESULTSETs](../../developer-guide/snowflake-scripting/resultsets.md).

### Nested stored procedure declaration syntax

Use the following syntax to declare a [nested stored procedure](../../developer-guide/stored-procedure/stored-procedures-snowflake-scripting.md):

```sqlsyntax
<nested_procedure_name> PROCEDURE (
    [ <arg_name> <arg_data_type> ] [ , ... ] )
  RETURNS { <result_data_type> | TABLE ( [ <col_name> <col_data_type> [ , ... ] ] ) }
  AS <nested_procedure_definition>
```

Where:

`nested_procedure_name`
:   The name of the nested stored procedure. The name must follow the naming rules for [Object identifiers](../identifiers.md).

`( [ arg_name arg_data_type ] [ , ... ] )`
:   Specifies the input arguments for the nested stored procedure.

    * For `arg_name`, specify the name of the input argument.
    * For `arg_data_type`, specify [a SQL data type](../../sql-reference-data-types.md).

`RETURNS { result_data_type | TABLE ( [ col_name col_data_type [ , ... ] ] ) }`
:   Specifies the type of the result returned by the stored procedure. Currently, NOT NULL isn’t supported in the
    RETURNS parameter for nested stored procedures.

    * For `RETURNS result_data_type`, specify [a SQL data type](../../sql-reference-data-types.md).
    * For `RETURNS TABLE ( [ col_name col_data_type [ , ... ] ] )`, if you know the
      [Snowflake data types](../../sql-reference-data-types.md) of the columns in the returned table, specify the column names and
      types:

      ```sqlexample
      RETURNS TABLE (sales_date DATE, quantity NUMBER)
      ```

      Otherwise (for example, if you are determining the column types during run time), you can omit the column names and types:

      ```sqlexample
      RETURNS TABLE ()
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

`AS nested_procedure_definition`
:   Defines the code executed by the nested stored procedure. The definition can consist of any valid code.

### Exception declaration syntax

Use the following syntax to declare an [exception](../../developer-guide/snowflake-scripting/exceptions.md):

```sqlsyntax
<exception_name> EXCEPTION [ ( <exception_number> , '<exception_message>' ) ] ;
```

Where:

> `exception_name`
> :   The name to give to the exception.
>
> `exception_number`
> :   A number to uniquely identify the exception. The number must be an integer between -20000 and -20999. The
> number should not be used for any other exception that exists at the same time.
>
>     Default: -20000
>
> `exception_message`
> :   A message to describe the exception.
> The message must not contain any double quote characters.
>
>     Default: Empty string.

For example:

> ```sqlexample
> exception_could_not_create_table EXCEPTION (-20003, 'ERROR: Could not create table.');
> ```

For more information about exceptions (including complete examples), see [Handling exceptions](../../developer-guide/snowflake-scripting/exceptions.md).

## Examples

This example declares a variable named `profit` for use in a Snowflake Scripting anonymous block:

```sqlexample
DECLARE
  profit number(38, 2) DEFAULT 0.0;
BEGIN
  LET cost number(38, 2) := 100.0;
  LET revenue number(38, 2) DEFAULT 110.0;

  profit := revenue - cost;
  RETURN profit;
END;
```

Note: If you use [Snowflake CLI](../../developer-guide/snowflake-cli/index.md), [SnowSQL](../../user-guide/snowsql.md), the Classic Console, or the
`execute_stream` or `execute_string` method in [Python Connector](../../developer-guide/python-connector/python-connector.md)
code, use this example instead (see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](../../developer-guide/snowflake-scripting/running-examples.md)):

```sqlexample
EXECUTE IMMEDIATE
$$
DECLARE
  profit number(38, 2) DEFAULT 0.0;
BEGIN
  LET cost number(38, 2) := 100.0;
  LET revenue number(38, 2) DEFAULT 110.0;

  profit := revenue - cost;
  RETURN profit;
END;
$$
;
```

For more examples that declare variables, cursors, RESULTSETs, and exceptions, see the following topics:

* [Examples of using variables](../../developer-guide/snowflake-scripting/variables.md)
* [Example of using a cursor](../../developer-guide/snowflake-scripting/cursors.md)
* [Examples of using a RESULTSET](../../developer-guide/snowflake-scripting/resultsets.md)
* [Handling exceptions](../../developer-guide/snowflake-scripting/exceptions.md)
