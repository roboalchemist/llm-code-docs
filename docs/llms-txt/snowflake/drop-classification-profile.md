# Source: https://docs.snowflake.com/en/sql-reference/classes/classification_profile/commands/drop-classification-profile.md

# DROP CLASSIFICATION_PROFILE

*Fully qualified name:* SNOWFLAKE.DATA_PRIVACY.CLASSIFICATION_PROFILE

Drops a classification profile instance in the current or specified schema.

## Syntax

```sqlsyntax
DROP SNOWFLAKE.DATA_PRIVACY.CLASSIFICATION_PROFILE
  [ IF EXISTS ] <classification_profile_name>
```

## Parameters

`classification_profile_name`
:   Specifies the identifier of the instance of the CLASSIFICATION_PROFILE class.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../../../identifiers-syntax.md).

## Access control requirements

A [role](../../../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object |
| --- | --- |
| OWNERSHIP | SNOWFLAKE.DATA_PRIVACY.CLASSIFICATION_PROFILE instance |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../../../user-guide/security-access-control-overview.md).

## Usage notes

Dropped instances cannot be recovered; they must be recreated.

## Examples

Drop the classification profile instance:

```sqlexample
DROP SNOWFLAKE.DATA_PRIVACY.CLASSIFICATION_PROFILE my_classification_profile;
```
