# Source: https://docs.snowflake.com/en/sql-reference/functions/is_role_activated.md

Categories:
:   [Context functions](../functions-context.md) (General)

# IS_ROLE_ACTIVATED (SYS_CONTEXT function)

Returns the VARCHAR value `'TRUE'` if an account role is activated in the current session.

See also:
:   [IS_DATABASE_ROLE_ACTIVATED (SYS_CONTEXT function)](is_database_role_activated.md)
    [SYS_CONTEXT (SNOWFLAKE$SESSION namespace)](sys_context_snowflake_session.md)

## Syntax

```sqlsyntax
SYS_CONTEXT(
  'SNOWFLAKE$SESSION' ,
  'IS_ROLE_ACTIVATED' ,
  '<role>'
)
```

## Arguments

`'SNOWFLAKE$SESSION'`
:   Specifies that you want to call a function to return context information about the current session.

`'IS_ROLE_ACTIVATED'`
:   Calls the IS_ROLE_ACTIVATED function.

`'role'`
:   Specifies the account role to check.

## Returns

The function returns one of the following VARCHAR values:

* `'TRUE'` if the account role is activated in the current session.
* `'FALSE'` if the account role is not activated or if the account role is not valid.

To compare this return value against the BOOLEAN value TRUE or FALSE, [cast](../data-type-conversion.md) the return
value to BOOLEAN. For example:

```sqlexample
SELECT SYS_CONTEXT('SNOWFLAKE$SESSION', 'IS_ROLE_ACTIVATED', 'my_role')::BOOLEAN = TRUE;
```

## Usage notes

## Examples

The following example returns `'TRUE'` if the role `my_role` is in the role hierarchy of the session’s primary or secondary
roles:

```sqlexample
SELECT SYS_CONTEXT('SNOWFLAKE$SESSION', 'IS_ROLE_ACTIVATED', 'my_role');
```
