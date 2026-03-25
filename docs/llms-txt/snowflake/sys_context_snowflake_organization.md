# Source: https://docs.snowflake.com/en/sql-reference/functions/sys_context_snowflake_organization.md

Categories:
:   [Context functions](../functions-context.md) (General)

# SYS_CONTEXT (SNOWFLAKE$ORGANIZATION namespace)

Returns information about the current organization.

You can call this function in any account in the organization. In any other context, the function returns NULL.

See also:
:   [SYS_CONTEXT](sys_context.md) ,
    [SYS_CONTEXT (SNOWFLAKE$APPLICATION namespace)](sys_context_snowflake_application.md) ,
    [SYS_CONTEXT (SNOWFLAKE$ENVIRONMENT namespace)](sys_context_snowflake_environment.md) ,
    [SYS_CONTEXT (SNOWFLAKE$ORGANIZATION_SESSION namespace)](sys_context_snowflake_organization_session.md) ,
    [SYS_CONTEXT (SNOWFLAKE$SESSION namespace)](sys_context_snowflake_session.md) ,
    [IS_GROUP_ACTIVATED (SYS_CONTEXT function)](is_group_activated.md) ,
    [IS_GROUP_IMPORTED (SYS_CONTEXT function)](is_group_imported.md) ,
    [IS_USER_IMPORTED (SYS_CONTEXT function)](is_user_imported.md)

## Syntax

**Syntax for calling functions:**

```sqlsyntax
SYS_CONTEXT(
  'SNOWFLAKE$ORGANIZATION' ,
  '<function>' , '<argument>' [ , ... ]
)
```

## Arguments

`'SNOWFLAKE$ORGANIZATION'`
:   Specifies that you want to retrieve a property or call a function to return context information about the current organization.

`'function'`
:   Name of the function that you want to call. You can call the following functions:

    * [IS_GROUP_ACTIVATED (SYS_CONTEXT function)](is_group_activated.md)
    * [IS_GROUP_IMPORTED (SYS_CONTEXT function)](is_group_imported.md)
    * [IS_USER_IMPORTED (SYS_CONTEXT function)](is_user_imported.md)

`'argument' [ , ... ]`
:   Arguments to pass to the function that you want to call.

## Returns

The function returns a VARCHAR value or NULL:

* The return value depends on
  the function that you are calling.
* If you call SYS_CONTEXT with the SNOWFLAKE$ORGANIZATION namespace outside of
  any of the supported contexts, the function returns NULL.

## Usage notes

* If you are specifying the function call in a double-quoted string in a shell, escape the `$` character with a backslash
  (`\`) so that `$ORGANIZATION` is not interpreted as a shell variable.

  For example, if you are using Snowflake CLI and you are
  [specifying the SQL statement as a command-line argument](../../developer-guide/snowflake-cli/sql/execute-sql.md) in double
  quotes:

  ```bash
  snow sql --query "SELECT SYS_CONTEXT('SNOWFLAKE\$ORGANIZATION', 'IS_USER_IMPORTED', 'my_user_name');"
  ```

## Examples

See the following topics:

* [IS_GROUP_ACTIVATED (SYS_CONTEXT function)](is_group_activated.md)
* [IS_GROUP_IMPORTED (SYS_CONTEXT function)](is_group_imported.md)
* [IS_USER_IMPORTED (SYS_CONTEXT function)](is_user_imported.md)
