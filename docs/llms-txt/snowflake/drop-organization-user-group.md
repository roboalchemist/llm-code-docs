# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-organization-user-group.md

# DROP ORGANIZATION USER GROUP

Removes an [organization user group](../../user-guide/organization-users.md) from the organization.

See also:
:   [CREATE ORGANIZATION USER GROUP](create-organization-user-group.md) , [ALTER ORGANIZATION USER GROUP](alter-organization-user-group.md) , [SHOW ORGANIZATION USER GROUPS](show-organization-user-groups.md)

## Syntax

```sqlsyntax
DROP ORGANIZATION USER GROUP [ IF EXISTS ] <name>
```

## Parameters

`name`
:   Identifier for the organization user group; must be unique for your organization.

    The identifier value must start with an alphabetic character and cannot contain spaces or special characters unless the entire
    identifier string is enclosed in double quotes (for example, `"My object"`). Identifiers enclosed in double quotes are also case
    sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | Organization user group |  |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* If an organization user group is dropped, the local users that were created in a regular account when the group was imported are also
  deleted. These users can’t be recovered. You’d have to recreate the local users by creating a new organization user group with the
  organization users, and then importing the group into the regular account.

* When the IF EXISTS clause is specified and the target object doesn’t exist, the command completes successfully
  without returning an error.

## Example

```sqlexample
DROP ORGANIZATION USER GROUP data_stewards;
```
