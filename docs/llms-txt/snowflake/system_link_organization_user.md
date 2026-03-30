# Source: https://docs.snowflake.com/en/sql-reference/functions/system_link_organization_user.md

Categories:
:   [System functions](../functions-system.md) (System Control)

# SYSTEM$LINK_ORGANIZATION_USER

Links an [organization user](../../user-guide/organization-users.md) with a user that already exists in the regular account.

When an account administrator adds an organization user group to a regular account, a conflict arises when an organization user in the
group corresponds to a person who already has a user object in the account. This function resolves the conflict and allows the user to be
managed as an organization user going forward.

## Syntax

```sqlsyntax
SYSTEM$LINK_ORGANIZATION_USER( '<local_user>', '<org_user>' )
```

## Arguments

`'local_user'`
:   Name of a user object that exists in the regular account.

`'org_user'`
:   Name of the organization user that corresponds to the same person as `local_user`.

## Usage notes

Linking an organization user to a local user object replaces the EMAIL property of the local user with the EMAIL property of the
organization user.

## Example

```sqlexample
SELECT SYSTEM$LINK_ORGANIZATION_USER('jloeb', 'jloeb');
```
