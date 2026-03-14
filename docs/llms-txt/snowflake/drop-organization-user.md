# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-organization-user.md

# DROP ORGANIZATION USER

Removes an [organization user](../../user-guide/organization-users.md) from the organization.

See also:
:   [CREATE ORGANIZATION USER](create-organization-user.md) , [ALTER ORGANIZATION USER](alter-organization-user.md) , [SHOW ORGANIZATION USERS](show-organization-users.md)

## Syntax

```sqlsyntax
DROP ORGANIZATION USER [ IF EXISTS ] <name>
```

## Parameters

`name`
:   Identifier for the organization user; must be unique for your organization.

    The identifier value must start with an alphabetic character and cannot contain spaces or special characters unless the entire
    identifier string is enclosed in double quotes (for example, `"My object"`). Identifiers enclosed in double quotes are also case
    sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | Organization user |  |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* Dropped organization users cannot be recovered; they must be recreated.

* When the IF EXISTS clause is specified and the target object doesn’t exist, the command completes successfully
  without returning an error.

## Example

```sqlexample
DROP ORGANIZATION USER joe;
```
