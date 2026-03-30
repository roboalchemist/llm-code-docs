# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-organization-user.md

# ALTER ORGANIZATION USER

Modifies the properties of an existing [organization user](../../user-guide/organization-users.md).

See also:
:   [CREATE ORGANIZATION USER](create-organization-user.md) , [DROP ORGANIZATION USER](drop-organization-user.md) , [SHOW ORGANIZATION USERS](show-organization-users.md)

## Syntax

```sqlsyntax
ALTER ORGANIZATION USER [ IF EXISTS ] <name> SET [ objectProperties ]

ALTER ORGANIZATION USER <name> UNSET [ objectProperties ]
```

Where:

> ```sqlsyntax
> objectProperties ::=
>   EMAIL = '<string>'
>   DISPLAY_NAME = '<string>'
>   FIRST_NAME = '<string>'
>   MIDDLE_NAME = '<string>'
>   LAST_NAME = '<string>'
>   COMMENT = '<string>'
> ```

## Parameters

`name`
:   Specifies the identifier for the organization user to alter.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

`SET ...`
:   Set object properties. For a description of the object properties, see [CREATE ORGANIZATION USER](create-organization-user.md).

`UNSET ...`
:   Unset object properties. For a description of the object properties, see [CREATE ORGANIZATION USER](create-organization-user.md).

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| MANAGE ORGANIZATION USERS | Account | By default, only the GLOBALORGADMIN and USERADMIN system roles in the organization account have this privilege. |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Examples

```sqlexample
ALTER ORGANIZATION USER alice
  SET LOGIN_NAME = 'asmith';
```
