# Source: https://docs.snowflake.com/en/sql-reference/functions/is_organization_user.md

Categories:
:   [Organization user and organization user group functions](../functions-organization-users.md)

# IS_ORGANIZATION_USER

Returns TRUE if the argument is a Snowflake user who is an [organization user](../../user-guide/organization-users.md).

## Syntax

```sqlsyntax
IS_ORGANIZATION_USER( <exp> )
```

## Arguments

`exp`
:   Expression that resolves to the name of a Snowflake user object.

    If passing in the literal name of a user, surround it with single quotes (for example, `'joe'`).

## Returns

Returns TRUE if the argument is an organization user.

## Usage notes

In data sharing contexts, this function returns NULL if it is called from a consumer account that exists in a *different organization* than
the provider account. Calling the function from a consumer account in the *same organization* as the provider returns TRUE or FALSE.

## Examples

Determine if the user `joe` in the current account is an organization user:

```sqlexample
SELECT IS_ORGANIZATION_USER('joe');
```

Determine if the current user in the session is an organization user:

```sqlexample
SELECT IS_ORGANIZATION_USER(CURRENT_USER());
```
