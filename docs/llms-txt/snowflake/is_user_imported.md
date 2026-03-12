# Source: https://docs.snowflake.com/en/sql-reference/functions/is_user_imported.md

Categories:
:   [Context functions](../functions-context.md) (General)

# IS_USER_IMPORTED (SYS_CONTEXT function)

Returns the VARCHAR value `'TRUE'` if the specified user is an [organization user](../../user-guide/organization-users.md) that
was imported into the current account.

See also:
:   [SYS_CONTEXT (SNOWFLAKE$ORGANIZATION namespace)](sys_context_snowflake_organization.md) ,
    [IS_GROUP_ACTIVATED (SYS_CONTEXT function)](is_group_activated.md) ,
    [IS_GROUP_IMPORTED (SYS_CONTEXT function)](is_group_imported.md)

## Syntax

```sqlsyntax
SYS_CONTEXT(
  'SNOWFLAKE$ORGANIZATION' ,
  'IS_USER_IMPORTED' ,
  '<user_name>'
)
```

## Arguments

`'SNOWFLAKE$ORGANIZATION'`
:   Specifies that you want to call a function to return context information about the current organization.

`'IS_USER_IMPORTED'`
:   Calls the IS_USER_IMPORTED function.

`'user_name'`
:   Specifies the name of the user to check.

## Returns

The function returns one of the following VARCHAR values:

* `'TRUE'` if the user is an organization user that was imported into the current account.
* `'FALSE'` if the user is not an organization user, was not imported into the current account, or is not a valid user.

To compare this return value against the BOOLEAN value TRUE or FALSE, [cast](../data-type-conversion.md) the return
value to BOOLEAN. For example:

```sqlexample
SELECT SYS_CONTEXT('SNOWFLAKE$ORGANIZATION', 'IS_USER_IMPORTED', 'my_user_name')::BOOLEAN = TRUE;
```

## Usage notes

## Examples

The following example returns `'TRUE'` if the user `my_user_name` is an organization user that was imported into the current
account:

```sqlexample
SELECT SYS_CONTEXT('SNOWFLAKE$ORGANIZATION', 'IS_USER_IMPORTED', 'my_user_name');
```
