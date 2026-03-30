# Source: https://docs.snowflake.com/en/sql-reference/sql/desc-available-organization-profile.md

# DESCRIBE AVAILABLE ORGANIZATION PROFILE

Describes the active organization profile that can be associated with organizational listings.

DESCRIBE can be abbreviated to DESC.

See also:
:   [ALTER ORGANIZATION PROFILE](alter-organization-profile.md), [CREATE ORGANIZATION PROFILE](create-organization-profile.md), [DESCRIBE ORGANIZATION PROFILE](desc-organization-profile.md), [DROP ORGANIZATION PROFILE](drop-organization-profile.md), [SHOW AVAILABLE ORGANIZATION PROFILES](show-available-organization-profiles.md), [SHOW ORGANIZATION PROFILES](show-organization-profiles.md), [SHOW VERSIONS IN ORGANIZATION PROFILE](show-versions-in-organization-profile.md)

## Syntax

```sqlsyntax
{ DESC | DESCRIBE } AVAILABLE ORGANIZATION PROFILE <name>
```

## Parameters

`name`
:   Specifies the identifier for the organization profile to describe. Must contain only uppercase characters or numbers.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case sensitive. See [Identifier requirements](../identifiers-syntax.md).

## Output

The output of the command includes the following columns, which describe the properties and metadata of the object:

| Column | Description |
| --- | --- |
| `created_on` | The date and time when the organization profile was created. |
| `name` | The name of the organization profile. |
| `title` | The title of the organization profile. |
| `system_generated` | Indicates the organization profile is system generated. |
| `state` | The organization profile state. One of ACTIVE or DRAFT. |
| `description` | The description of the organization profile. |
| `owner_contact` | The contact email of the owner of the organization profile. |
| `approver_contact` | The contact email of the access approver of the organization profile. |
| `logo` | The organization profile logo URL. |
| `can_publish_listings_with_profile` | Whether the current user can publish organizational listings using this organization profile. One of `TRUE` or `FALSE`. |

## Examples

The following example describes the ORGPROFILE organization profile:

```sqlexample
DESCRIBE AVAILABLE ORGANIZATION PROFILE orgprofile;
```

```output
+-------------------------+-------------+--------------------------+---------------------+---------------------+----------------------------------+---------------------+---------------------+--------------------+-----------------------------------+
|created_on               |name         |title                     |system_generated     |state                |description                       |owner_contact        |approver_contact     |logo                |can_publish_listings_with_profile  |
+-------------------------+-------------+--------------------------+---------------------+---------------------+----------------------------------+---------------------+---------------------+--------------------+-----------------------------------+
|2025-01-01 01:01:01.000  |ORGPROFILE   |My Organization Profile   |FALSE                |ACTIVE               |Organization profile description  |test@test.com        |test@test.com        |urn:icon:shield     |TRUE                               |
+-------------------------+-------------+--------------------------+---------------------+---------------------+----------------------------------+---------------------+---------------------+--------------------+-----------------------------------+
```
