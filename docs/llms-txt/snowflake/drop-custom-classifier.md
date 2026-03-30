# Source: https://docs.snowflake.com/en/sql-reference/classes/custom_classifier/commands/drop-custom-classifier.md

# DROP CUSTOM_CLASSIFIER

*Fully qualified name:* SNOWFLAKE.DATA_PRIVACY.CUSTOM_CLASSIFIER

Drops a custom classification instance in the current or specified schema.

See also:
:   [Using custom classifiers to implement custom semantic categories](../../../../user-guide/classify-custom-using.md)

## Syntax

```sqlsyntax
DROP SNOWFLAKE.DATA_PRIVACY.CUSTOM_CLASSIFIER
[ IF EXISTS ] <custom_classifier_name>
```

## Parameters

`custom_classifier_name`
:   Specifies the identifier (name) for the instance.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../../../identifiers-syntax.md).

## Arguments

None.

## Access control requirements

A [role](../../../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object |
| --- | --- |
| OWNERSHIP | SNOWFLAKE.DATA_PRIVACY.CUSTOM_CLASSIFIER instance |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../../../user-guide/security-access-control-overview.md).

## Usage notes

Dropped instances cannot be recovered; they must be recreated.

## Examples

```sqlexample
DROP SNOWFLAKE.DATA_PRIVACY.CUSTOM_CLASSIFIER data.classifiers.medical_codes;
```
