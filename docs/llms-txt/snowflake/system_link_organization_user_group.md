# Source: https://docs.snowflake.com/en/sql-reference/functions/system_link_organization_user_group.md

Categories:
:   [System functions](../functions-system.md) (System Control)

# SYSTEM$LINK_ORGANIZATION_USER_GROUP

Links an [organization user group](../../user-guide/organization-users.md) with an access control role that already exists in the regular account.

When an account administrator adds an organization user group to a regular account, a conflict arises if there is an existing role with the
same name as the group. This function resolves the conflict and allows the role to be managed as an organization user group going forward.

## Syntax

```sqlsyntax
SYSTEM$LINK_ORGANIZATION_USER_GROUP( <name> )
```

## Arguments

`name`
:   Name of an organization user group. This matches the name of an existing access control role.

## Usage notes

You can’t link an organization user group to a role that is granted to other roles.

## Examples

```sqlexample
SELECT SYSTEM$LINK_ORGANIZATION_USER_GROUP('marketing_team');
```
