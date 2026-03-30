# Source: https://docs.snowflake.com/en/sql-reference/functions/system_unlink_organization_user.md

Categories:
:   [System functions](../functions-system.md) (System Control)

# SYSTEM$UNLINK_ORGANIZATION_USER

Unlinks a user object from an [organization user](../../user-guide/organization-users.md) so it can be managed as a local user going forward.

## Syntax

```sqlsyntax
SYSTEM$UNLINK_ORGANIZATION_USER( '<user_name>' )
```

## Arguments

`'user_name'`
:   Name of a user object that was imported from an organization user.

## Examples

```sqlexample
SELECT SYSTEM$UNLINK_ORGANIZATION_USER('jloeb');
```
