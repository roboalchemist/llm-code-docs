# Source: https://docs.snowflake.com/en/sql-reference/sql/desc-function.md

# DESCRIBE FUNCTION

Describes the specified user-defined function (UDF) or external function, including the signature (i.e. arguments),
return value, language, and body (i.e. definition).

DESCRIBE can be abbreviated to DESC.

See also:
:   [DROP FUNCTION](drop-function.md) , [ALTER FUNCTION](alter-function.md) , [CREATE FUNCTION](create-function.md) , [SHOW USER FUNCTIONS](show-user-functions.md) , [SHOW EXTERNAL FUNCTIONS](show-external-functions.md)

## Syntax

```sqlsyntax
DESC[RIBE] FUNCTION <name> ( [ <arg_data_type> ] [ , ... ] )
```

## Parameters

`name`
:   Specifies the identifier for the function to describe. If the identifier contains spaces or special characters, the entire string must
    be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive.

`arg_data_type [ , ... ]`
:   Specifies the data type of the argument(s), if any, for the function. The argument data types are necessary because functions support
    name overloading (i.e. two functions in the same schema can have the same name) and the argument data types are used to identify the
    function.

## Usage notes

* To post-process the output of this command, you can use the [pipe operator](../operators-flow.md)
  (`->>`) or the [RESULT_SCAN](../functions/result_scan.md) function. Both constructs treat the output as a
  result set that you can query.

  For example, you can use the pipe operator or RESULT_SCAN function to select specific columns from the SHOW
  command output or filter the rows.

  When you refer to the output columns, use [double-quoted identifiers](../identifiers-syntax.md) for
  the column names. For example, to select the output column `type`, specify `SELECT "type"`.

  You must use double-quoted identifiers because the output column names for SHOW commands are in lowercase.
  The double quotes ensure that the column names in the SELECT list or WHERE clause match the column names
  in the SHOW command output that was scanned.

## Examples

This demonstrates the DESCRIBE FUNCTION command:

> ```sqlexample
> DESC FUNCTION multiply(number, number);
>
> -----------+----------------------------------+
>  property  |              value               |
> -----------+----------------------------------+
>  signature | (a NUMBER(38,0), b NUMBER(38,0)) |
>  returns   | NUMBER(38,0)                     |
>  language  | SQL                              |
>  body      | a * b                            |
> -----------+----------------------------------+
> ```
