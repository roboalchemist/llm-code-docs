# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-organization-profile.md

# DROP ORGANIZATION PROFILE

Removes an organization profile.

See also:
:   [ALTER ORGANIZATION PROFILE](alter-organization-profile.md), [CREATE ORGANIZATION PROFILE](create-organization-profile.md), [DESCRIBE AVAILABLE ORGANIZATION PROFILE](desc-available-organization-profile.md), [DESCRIBE ORGANIZATION PROFILE](desc-organization-profile.md), [SHOW AVAILABLE ORGANIZATION PROFILES](show-available-organization-profiles.md), [SHOW ORGANIZATION PROFILES](show-organization-profiles.md), [SHOW VERSIONS IN ORGANIZATION PROFILE](show-versions-in-organization-profile.md)

## Syntax

```sqlsyntax
DROP ORGANIZATION PROFILE <name>
```

## Parameters

`name`
:   Specifies the identifier for the organization profile to drop.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case sensitive. For information about identifier syntax, see [Identifier requirements](../identifiers-syntax.md).

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | Organization profile | Executing this command with any other role returns an error. |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* Dropped organization profiles cannot be recovered; they must be recreated. An organization profile cannot be dropped if it is associated with an organizational listing.

## Examples

The following example drops the organization profile named `MYORGANIZATIONPROFILE`:

```sqlexample
DROP ORGANIZATION PROFILE myorganizationprofile;
```

```output
+---------------------------------------------+
| status                                      |
|---------------------------------------------|
| MYORGANIZATIONPROFILE successfully dropped. |
+---------------------------------------------+
```
