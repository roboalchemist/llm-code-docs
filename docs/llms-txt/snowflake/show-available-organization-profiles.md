# Source: https://docs.snowflake.com/en/sql-reference/sql/show-available-organization-profiles.md

# SHOW AVAILABLE ORGANIZATION PROFILES

Lists the organization profiles available in the user’s organization.

See also:
:   [ALTER ORGANIZATION PROFILE](alter-organization-profile.md), [CREATE ORGANIZATION PROFILE](create-organization-profile.md), [DESCRIBE AVAILABLE ORGANIZATION PROFILE](desc-available-organization-profile.md), [DESCRIBE ORGANIZATION PROFILE](desc-organization-profile.md), [DROP ORGANIZATION PROFILE](drop-organization-profile.md), [SHOW ORGANIZATION PROFILES](show-organization-profiles.md), [SHOW VERSIONS IN ORGANIZATION PROFILE](show-versions-in-organization-profile.md)

## Syntax

```sqlsyntax
SHOW AVAILABLE ORGANIZATION PROFILES
```

## Output

The output of the command includes the following columns, which describe the properties and metadata of the object:

| Column | Description |
| --- | --- |
| `created_on` | The date and time when the organization profile was created. |
| `name` | The name of the organization profile. |
| `system_generated` | Indicates the organization profile is system generated. |
| `state` | The organization profile state. One of ACTIVE or DRAFT. |
| `organization_name` | The name of the organization associated with the organization profile. |
| `title` | The title of the organization profile. |
| `description` | The description of the organization profile. |
| `owner_contact` | The contact email of the owner of the organization profile. |
| `approver_contact` | The contact email of the access approver of the organization profile. |
| `can_publish_listings_with_profile` | Whether the current user can publish organizational listings using this organization profile. One of `TRUE` or `FALSE`. |

## Examples

The following example lists the organization profiles that you have the privileges to access:

```sqlexample
SHOW AVAILABLE ORGANIZATION PROFILES;
```

```output
+-------------------------+-------------+---------------------+---------------------+---------------------+------------------------+---------------------------------+---------------------+---------------------+-----------------------------------+
|created_on               |name         |system_generated     |state                |organization_name    |title                   |description                      |owner_contact        |approver_contact     |can_publish_listings_with_profile  |
+-------------------------+-------------+---------------------+---------------------+---------------------+------------------------+---------------------------------+---------------------+---------------------+-----------------------------------+
|2025-01-01 01:01:01.000  |ORGPROFILE   |FALSE                |ACTIVE               |TESTORG              |My Organization Profile |Organization profile description |test@test.com        |test@test.com        |TRUE                               |
+-------------------------+-------------+---------------------+---------------------+---------------------+------------------------+---------------------------------+---------------------+---------------------+-----------------------------------+
```
