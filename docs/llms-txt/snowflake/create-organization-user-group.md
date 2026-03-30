# Source: https://docs.snowflake.com/en/sql-reference/sql/create-organization-user-group.md

# CREATE ORGANIZATION USER GROUP

Creates a new [organization user group](../../user-guide/organization-users.md).

See also:
:   [ALTER ORGANIZATION USER GROUP](alter-organization-user-group.md) , [DROP ORGANIZATION USER GROUP](drop-organization-user-group.md) , [SHOW ORGANIZATION USER GROUPS](show-organization-user-groups.md)

## Syntax

```sqlsyntax
CREATE ORGANIZATION USER GROUP [ IF NOT EXISTS ] <name>
  [ IS_GRANTABLE = { TRUE | FALSE } ]
```

## Required parameters

`name`
:   Identifier for the organization user group; must be unique for your organization.

    The identifier must start with an alphabetic character and cannot contain spaces or special characters unless the entire identifier
    string is enclosed in double quotes (for example, `"My object"`). Identifiers enclosed in double quotes are also case sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

## Optional parameters

`IS_GRANTABLE = { TRUE | FALSE }`
:   Specifies whether the role that is imported into a regular account from the organization user group can be granted to an account-specific role. If `TRUE`, the role that is created when the ACCOUNTADMIN imports the organization user group can be granted to another role.

    Default: `FALSE`

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| CREATE ORGANIZATION USER GROUP | Account | By default, only the GLOBALORGADMIN and USERADMIN system roles in the organization account have this privilege. |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Examples

Create an organization user group named `data_stewards`:

```sqlexample
CREATE ORGANIZATION USER GROUP data_stewards;
```
