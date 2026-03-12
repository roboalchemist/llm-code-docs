# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-organization-user-group.md

# ALTER ORGANIZATION USER GROUP

Modifies the properties of an existing [organization user group](../../user-guide/organization-users.md).

See also:
:   [CREATE ORGANIZATION USER GROUP](create-organization-user-group.md) , [DROP ORGANIZATION USER GROUP](drop-organization-user-group.md) , [SHOW ORGANIZATION USER GROUPS](show-organization-user-groups.md)

## Syntax

```sqlsyntax
ALTER ORGANIZATION USER GROUP [ IF EXISTS ] <name> ADD ORGANIZATION USERS <org_user> [ , <org_user> ... ]

ALTER ORGANIZATION USER GROUP [ IF EXISTS ] <name> REMOVE ORGANIZATION USERS <org_user> [ , <org_user> ... ]

ALTER ORGANIZATION USER GROUP [ IF EXISTS ] <name> SET VISIBILITY =
  { ALL
  | ACCOUNTS <account> [ , <account> ... ]
  | REGION GROUPS '<region_group>' [ , '<region_group>' ... ]
  }

ALTER ORGANIZATION USER GROUP [ IF EXISTS ] <name> SET IS_GRANTABLE = { TRUE | FALSE }
```

## Parameters

`name`
:   Specifies the identifier for the organization user group to alter.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

`ADD ORGANIZATION USERS org_user [ , org_user ]`
:   Specifies the organization users that you want to add to the organization user group. A comma-delimited list of organization user objects.

    Adding new organization users as members of an organization user group does not remove existing members of the group.

`REMOVE ORGANIZATION USERS org_user [ , org_user ]`
:   Specifies the organization users that you want to remove from the organization user group. A comma-delimited list of organization user objects.

`SET VISIBILITY = ALL` or . `SET VISIBILITY = ACCOUNTS account [ , account ... ]` or . `SET VISIBILITY = REGION GROUPS 'region_group' [ , 'region_group' ... ]`
:   Specifies which accounts can view and add the organization user group.

    > **Note:**
    >
    > An organization administrator cannot unilaterally hide an organization user group from an
    > account that previously had visibility. An administrator in the regular account must run the ALTER ACCOUNT REMOVE ORGANIZATION USER GROUP
    > command to remove the organization user group from the account before the organization administrator can change the visibility.

    `ACCOUNTS account [ , account ... ]`
    :   Only the specified accounts can view and add the organization user group.

        Specify the account name without the name of the organization. Do not use the account locator.

    `REGION GROUPS 'region_group' [ , 'region_group' ... ]`
    :   Only accounts in the specified [region groups](../../user-guide/admin-account-identifier.md) can view and add the organization user group.

`SET IS_GRANTABLE = { TRUE | FALSE }`
:   Specifies whether the role that is imported into a regular account from the organization user group can be granted to an
    account-specific role. If `TRUE`, the role that is created when the ACCOUNTADMIN imports the organization user group can be
    granted to another role.

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| MANAGE ORGANIZATION USER GROUPS | Account | By default, only the GLOBALORGADMIN and USERADMIN system roles in the organization account have this privilege. |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Examples

Add organization users `joe` and `mary` to an organization user group `marketing`.

> ```sqlexample
> ALTER ORGANIZATION USER GROUP marketing ADD ORGANIZATION USERS joe, mary;
> ```

Remove organization user `dave` from the organization user group `data_stewards`.

> ```sqlexample
> ALTER ORGANIZATION USER GROUP data_stewards REMOVE ORGANIZATION USERS dave;
> ```

Allow all accounts in the organization to add the organization user group:

> ```sqlexample
> ALTER ORGANIZATION USER GROUP data_stewards SET VISIBILITY = ALL;
> ```

Only allow the account `qa_env` to add the organization user group:

> ```sqlexample
> ALTER ORGANIZATION USER GROUP data_stewards SET VISIBILITY = ACCOUNTS qa_env;
> ```
