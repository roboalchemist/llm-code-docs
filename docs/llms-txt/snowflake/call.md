# Source: https://docs.snowflake.com/en/sql-reference/sql/call.md

# CALL

Calls a [stored procedure](../../developer-guide/stored-procedure/stored-procedures-overview.md).

See also:
:   [CREATE PROCEDURE](create-procedure.md) , [SHOW PROCEDURES](show-procedures.md)

## Syntax

```sqlsyntax
CALL <procedure_name> ( [ [ <arg_name> => ] <arg> , ... ] )
  [ INTO :<snowflake_scripting_variable> ]
```

## Required parameters

`procedure_name ( [ [ arg_name => ] arg , ... ] )`
:   Specifies the identifier (`procedure_name`) for the procedure to call and any input arguments.

    You can either specify the input arguments by name (`arg_name => arg`) or by position (`arg`).

    Note the following:

    * You must either specify all arguments by name or by position. You can’t specify some of the arguments by name and other
      arguments by position.

      When specifying an argument by name, you can’t use double quotes around the argument name.
    * If two functions or two procedures have the same name but different argument types, you can use the argument names to specify
      which function or procedure to execute, if the argument names are different. Refer to
      [Overloading procedures and functions](../../developer-guide/udf-stored-procedure-naming-conventions.md).

## Optional parameters

`INTO :snowflake_scripting_variable`
:   Sets the specified [Snowflake Scripting variable](../../developer-guide/snowflake-scripting/variables.md) to the return value of
    the stored procedure.

## Examples

For more extensive examples of creating and calling stored procedures, see [Working with stored procedures](../../developer-guide/stored-procedure/stored-procedures-usage.md).

```sqlexample
CALL stproc1(5.14::FLOAT);
```

Each argument to a stored procedure can be a general expression:

```sqlexample
CALL stproc1(2 * 5.14::FLOAT);
```

An argument can be a subquery:

```sqlexample
CALL stproc1(SELECT COUNT(*) FROM stproc_test_table1);
```

You can call only one stored procedure per CALL statement. For example, the following statement fails:

```sqlexample
CALL proc1(1), proc2(2);                          -- Not allowed
```

Also, you cannot use a stored procedure CALL as part of an expression. For example, all the following statements fail:

```sqlexample
CALL proc1(1) + proc1(2);                         -- Not allowed
CALL proc1(1) + 1;                                -- Not allowed
CALL proc1(proc2(x));                             -- Not allowed
SELECT * FROM (call proc1(1));                    -- Not allowed
```

However, inside a stored procedure, the stored procedure can call
another stored procedure, or call itself recursively.

> **Caution:**
>
> Nested calls can exceed the maximum allowed stack depth, so be careful when nesting calls,
> especially when using recursion.

The following example calls a stored procedure named `sv_proc1` and passes in a string literal and number as input arguments.
The example specifies the arguments by position:

```sqlexample
CALL sv_proc1('Manitoba', 127.4);
```

You can also specify the arguments by their names:

```sqlexample
CALL sv_proc1(province => 'Manitoba', amount => 127.4);
```

The following example demonstrates how to set and pass a [session variable](../session-variables.md) as an input
argument to a stored procedure:

```sqlexample
SET Variable1 = 49;
CALL sv_proc2($Variable1);
```

The following is an example of a Snowflake Scripting block that captures the return value of a stored procedure in a Snowflake
Scripting variable.

```sqlexample
DECLARE
  ret1 NUMBER;
BEGIN
  CALL sv_proc1('Manitoba', 127.4) into :ret1;
  RETURN ret1;
END;
```

Note: If you use [Snowflake CLI](../../developer-guide/snowflake-cli/index.md), [SnowSQL](../../user-guide/snowsql.md), the Classic Console, or the
`execute_stream` or `execute_string` method in [Python Connector](../../developer-guide/python-connector/python-connector.md)
code, use this example instead (see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](../../developer-guide/snowflake-scripting/running-examples.md)):

```sqlexample
EXECUTE IMMEDIATE $$
DECLARE
  ret1 NUMBER;
BEGIN
  CALL sv_proc1('Manitoba', 127.4) into :ret1;
  RETURN ret1;
END;
$$
;
```
