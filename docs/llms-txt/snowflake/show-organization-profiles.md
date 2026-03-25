# Source: https://docs.snowflake.com/en/sql-reference/sql/show-organization-profiles.md

# SHOW ORGANIZATION PROFILES

Lists the organization profiles for which you have access privileges.

See also:
:   [ALTER ORGANIZATION PROFILE](alter-organization-profile.md), [CREATE ORGANIZATION PROFILE](create-organization-profile.md), [DESCRIBE AVAILABLE ORGANIZATION PROFILE](desc-available-organization-profile.md), [DESCRIBE ORGANIZATION PROFILE](desc-organization-profile.md), [DROP ORGANIZATION PROFILE](drop-organization-profile.md), [SHOW AVAILABLE ORGANIZATION PROFILES](show-available-organization-profiles.md), [SHOW VERSIONS IN ORGANIZATION PROFILE](show-versions-in-organization-profile.md)

## Syntax

```sqlsyntax
SHOW ORGANIZATION PROFILES
```

## Output

The output of the command includes the following columns, which describe the properties and metadata of the object:

| Column | Description |
| --- | --- |
| `created_on` | The date and time when the organization profile was created. |
| `name` | The organization profile name. |
| `system_generated` | Indicates the organization profile is system generated and can’t be dropped. One of `TRUE` or `FALSE`. |
| `state` | The organization profile state. One of ACTIVE or DRAFT. |
| `organization_name` | The name of the organization associated with the organization profile. |
| `title` | The title of the organization profile. |
| `description` | The description of the organization profile. |
| `owner_contact` | The contact email of the owner of the organization profile. |
| `approver_contact` | The contact email of the access approver of the organization profile. |
| `owner` | The owner role of the organization profile. |

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP or MODIFY or a privileged role, such as ACCOUNTADMIN or SECURITYADMIN | Organization profile |  |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Examples

The following example lists the organization profiles that you have privileges to access:

```sqlexample
SHOW ORGANIZATION PROFILES;
```

```output
+-------------------------+-----------------+---------------------+---------------------+---------------------+---------------------------+----------------------------------+---------------------+---------------------+---------------------+
|created_on               |name             |system_generated     |state                |organization_name    |title                      |description                       |owner_contact        |approver_contact     |owner                |
+-------------------------+-----------------+---------------------+---------------------+---------------------+---------------------------+----------------------------------+---------------------+---------------------+---------------------+
| 2025-01-01 01:01:01.000 |ORGPROFILE       |FALSE                |ACTIVE               |TESTORG              |My Organization Profile    |Organization profile description  |test@test.com        |test@test.com        |ACCOUNTADMIN         |
+-------------------------+-----------------+---------------------+---------------------+---------------------+---------------------------+----------------------------------+---------------------+---------------------+---------------------+
```
