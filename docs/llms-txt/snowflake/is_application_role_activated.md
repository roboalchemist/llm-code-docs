# Source: https://docs.snowflake.com/en/sql-reference/functions/is_application_role_activated.md

Categories:
:   [Context functions](../functions-context.md) (General)

# IS_APPLICATION_ROLE_ACTIVATED (SYS_CONTEXT function)

Returns the VARCHAR value `'TRUE'` if an application role is activated in the specified context.

See also:
:   [SYS_CONTEXT (SNOWFLAKE$APPLICATION namespace)](sys_context_snowflake_application.md)

## Syntax

```sqlsyntax
SYS_CONTEXT(
  'SNOWFLAKE$APPLICATION' ,
  'IS_APPLICATION_ROLE_ACTIVATED' ,
  '<context>' ,
  '<app_role>'
)
```

## Arguments

`'SNOWFLAKE$APPLICATION'`
:   Specifies that you want to call a function to return context information about the application in which the function is called.

`'IS_APPLICATION_ROLE_ACTIVATED'`
:   Calls the IS_APPLICATION_ROLE_ACTIVATED function.

`'context'`
:   Specifies the execution context that you want to check. You can specify one of the following values:

    * `SESSION`: Checks if the application role is in the role hierarchy of the current session’s primary or secondary roles.
      The function returns `'TRUE'` if the role is in the role hierarchy.
    * `ACTIVE`: Checks if the application role is in the role hierarchy in the context of the current call.

      For example, in a call to an owner’s rights stored procedure, the procedure is executed by the owner’s role. The function
      returns `'TRUE'` if the application role is in the role hierarchy of the owner’s role.

`'app_role'`
:   Specifies the application role to check.

    Do not qualify the role name with the name of the application. The function automatically determines the application name from
    the context in which the function is called.

## Returns

The function returns one of the following VARCHAR values:

* `'TRUE'` if the application role is activated in the context specified by `context`.
* `'FALSE'` if the application role is not activated in that context or if the application role is not valid.

To compare this return value against the BOOLEAN value TRUE or FALSE, [cast](../data-type-conversion.md) the return
value to BOOLEAN. For example:

```sqlexample
SELECT SYS_CONTEXT('SNOWFLAKE$APPLICATION', 'IS_APPLICATION_ROLE_ACTIVATED', 'SESSION', 'my_app_role')::BOOLEAN = TRUE;
```

## Usage notes

## Examples

The following example returns `TRUE` if the application role `my_app_role` is in the role hierarchy of the session’s primary
or secondary roles:

```sqlexample
SELECT SYS_CONTEXT('SNOWFLAKE$APPLICATION', 'IS_APPLICATION_ROLE_ACTIVATED', 'SESSION', 'my_app_role');
```
