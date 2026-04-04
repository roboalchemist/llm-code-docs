# Source: https://docs.snowflake.com/en/sql-reference/functions/is_group_activated.md

Categories:
:   [Context functions](../functions-context.md) (General)

# IS_GROUP_ACTIVATED (SYS_CONTEXT function)

Returns the VARCHAR value `'TRUE'` if the role representing an [organization user group](../../user-guide/organization-users.md) is
activated in a given context.

See also:
:   [SYS_CONTEXT (SNOWFLAKE$ORGANIZATION namespace)](sys_context_snowflake_organization.md) ,
    [IS_GROUP_IMPORTED (SYS_CONTEXT function)](is_group_imported.md) ,
    [IS_USER_IMPORTED (SYS_CONTEXT function)](is_user_imported.md)

## Syntax

```sqlsyntax
SYS_CONTEXT(
  'SNOWFLAKE$ORGANIZATION' ,
  'IS_GROUP_ACTIVATED' ,
  '<context>' ,
  '<group_name>'
)
```

## Arguments

`'SNOWFLAKE$ORGANIZATION'`
:   Specifies that you want to call a function to return context information about the current organization.

`'IS_GROUP_ACTIVATED'`
:   Calls the IS_GROUP_ACTIVATED function.

`'context'`
:   Specifies the execution context that you want to check. You can specify one of the following values:

    * `SESSION`: Checks if the organization group role is in the role hierarchy of the current session’s primary or secondary
      roles. The function returns `'TRUE'` if the role is in the role hierarchy.
    * `ACTIVE`: Checks if the organization group role is in the role hierarchy in the context of the current call.

      For example, in a call to an owner’s rights stored procedure, the procedure is executed by the owner’s role. The function
      returns `'TRUE'` if the organization group role is in the role hierarchy of the owner’s role.

`'group_name'`
:   Specifies the name of the organization user group to check.

## Returns

The function returns one of the following VARCHAR values:

* `'TRUE'` if the organization user group role is activated in the context specified by `context`.
* `'FALSE'` if the organization user group role is not activated in that context or if the group is not a valid organization
  user group.

To compare this return value against the BOOLEAN value TRUE or FALSE, [cast](../data-type-conversion.md) the return
value to BOOLEAN. For example:

```sqlexample
SELECT SYS_CONTEXT('SNOWFLAKE$ORGANIZATION', 'IS_GROUP_ACTIVATED', 'SESSION', 'my_group_name')::BOOLEAN = TRUE;
```

## Usage notes

## Examples

The following example returns `'TRUE'` if the role for the organization user group `my_group_name` is in the role hierarchy
of the session’s primary or secondary roles:

```sqlexample
SELECT SYS_CONTEXT('SNOWFLAKE$ORGANIZATION', 'IS_GROUP_ACTIVATED', 'SESSION', 'my_group_name');
```
