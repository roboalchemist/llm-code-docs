# Source: https://docs.snowflake.com/en/sql-reference/functions/getvariable.md

Categories:
:   [Context functions](../functions-context.md) (Session)

# GETVARIABLE

Returns the value associated with a SQL variable name.

See also:
:   [Session variable functions](../session-variables.md)

## Syntax

```sqlsyntax
GETVARIABLE( '<name>' )
```

## Arguments

`name`
:   The name of the SQL variable.

    You must specify the name in uppercase letters, even if you used lowercase letters when defining the variable.

## Returns

The data type of the return value is VARCHAR.

## Usage notes

This function uses the result cache for the current session if you call the function more than once in the same session. The result cache
applies wherever you call this function, including the body of policy objects, such as a row access policy.

## Examples

This example shows how to use this function and other ways of getting the value of the variable:

> ```sqlexample
> SET MY_LOCAL_VARIABLE= 'my_local_variable_value';
> +----------------------------------+
> | status                           |
> |----------------------------------|
> | Statement executed successfully. |
> +----------------------------------+
> SELECT
>     GETVARIABLE('MY_LOCAL_VARIABLE'),
>     SESSION_CONTEXT('MY_LOCAL_VARIABLE'),
>     $MY_LOCAL_VARIABLE;
> +----------------------------------+--------------------------------------+-------------------------+
> | GETVARIABLE('MY_LOCAL_VARIABLE') | SESSION_CONTEXT('MY_LOCAL_VARIABLE') | $MY_LOCAL_VARIABLE      |
> |----------------------------------+--------------------------------------+-------------------------|
> | my_local_variable_value          | my_local_variable_value              | my_local_variable_value |
> +----------------------------------+--------------------------------------+-------------------------+
> ```

When variables are created with the SET command, the variable names are forced to all upper case. The functions
GETVARIABLE and SESSION_CONTEXT must pass the uppercase version of the function name. The “$” notation
works with either uppercase or lowercase variable names.

> ```sqlexample
> SET var_2 = 'value_2';
> +----------------------------------+
> | status                           |
> |----------------------------------|
> | Statement executed successfully. |
> +----------------------------------+
> SELECT
>     GETVARIABLE('var_2'),
>     GETVARIABLE('VAR_2'),
>     SESSION_CONTEXT('var_2'),
>     SESSION_CONTEXT('VAR_2'),
>     $var_2,
>     $VAR_2;
> +----------------------+----------------------+--------------------------+--------------------------+---------+---------+
> | GETVARIABLE('VAR_2') | GETVARIABLE('VAR_2') | SESSION_CONTEXT('VAR_2') | SESSION_CONTEXT('VAR_2') | $VAR_2  | $VAR_2  |
> |----------------------+----------------------+--------------------------+--------------------------+---------+---------|
> | NULL                 | value_2              | NULL                     | value_2                  | value_2 | value_2 |
> +----------------------+----------------------+--------------------------+--------------------------+---------+---------+
> ```
