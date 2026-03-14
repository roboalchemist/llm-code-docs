# Source: https://docs.snowflake.com/en/sql-reference/sql/show-organization-user-groups.md

# SHOW ORGANIZATION USER GROUPS

Lists [organization user groups](../../user-guide/organization-users.md).

* If the command is executed in the organization account, it lists all organization user groups in the organization.
* If the command is executed in a regular account, it lists the organization user groups that are available to the account.

See also:
:   [CREATE ORGANIZATION USER GROUP](create-organization-user-group.md) , [ALTER ORGANIZATION USER GROUP](alter-organization-user-group.md) , [DROP ORGANIZATION USER GROUP](drop-organization-user-group.md)

## Syntax

```sqlsyntax
SHOW ORGANIZATION USER GROUPS
```

## Parameters

None

## Access control requirements

The access control requirements for this command vary depending on the account where it is being executed.

Regular account:
:   Executing this command in a regular account requires the ACCOUNTADMIN role.

Organization account:
:   A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
    [privileges](../../user-guide/security-access-control-overview.md) at a minimum:

    | Privilege | Object | Notes |
    | --- | --- | --- |
    | MANAGE ORGANIZATION USER GROUPS | Account | By default, only the GLOBALORGADMIN and USERADMIN system roles in the organization account have this privilege. |

    For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

    For general information about roles and privilege grants for performing SQL actions on
    [securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Output

The output of the command includes the following columns, which describe the properties and metadata of the object:

| Column | Description |
| --- | --- |
| `name` | Name of the organization user group. |
| `is_imported` | When executed from a regular account, indicates whether the organization user group has been added to the account successfully. If TRUE, the organization user group was added and the role of the same name created. |
| `created_on` | Date and time when the organization user group was created. |
| `is_grantable` | When executed from a regular account, indicates whether the role that was imported from the organization user group can be granted to a local, account-specific role. If `TRUE`, the role imported from the organization user group can be granted to account-specific roles. |

## Examples

Show information about the organization user groups in the organization:

```sqlexample
SHOW ORGANIZATION USER GROUPS;
```
