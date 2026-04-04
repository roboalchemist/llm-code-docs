# Source: https://docs.snowflake.com/en/sql-reference/functions/system_unlink_organization_user_group.md

Categories:
:   [System functions](../functions-system.md) (System Control)

# SYSTEM$UNLINK_ORGANIZATION_USER_GROUP

Unlinks an access control role from an [organization user group](../../user-guide/organization-users.md) so it can be managed as a local role going
forward.

## Syntax

```sqlsyntax
SYSTEM$UNLINK_ORGANIZATION_USER_GROUP( '<role>' )
```

## Arguments

`'role'`
:   Name of an access control role that is linked to an organization user group.

## Usage notes

When you unlink an organization user group, user objects that were added to the regular account when the group was imported are also
unlinked.

## Examples

```sqlexample
SELECT SYSTEM$UNLINK_ORGANIZATION_USER_GROUP('marketing_team');
```
