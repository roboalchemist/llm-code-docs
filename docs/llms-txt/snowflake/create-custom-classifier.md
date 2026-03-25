# Source: https://docs.snowflake.com/en/sql-reference/classes/custom_classifier/commands/create-custom-classifier.md

# CREATE CUSTOM_CLASSIFIER

*Fully qualified name:* SNOWFLAKE.DATA_PRIVACY.CUSTOM_CLASSIFIER

See also:
:   [Using custom classifiers to implement custom semantic categories](../../../../user-guide/classify-custom-using.md)

Creates a new custom classification instance or replaces an existing custom classification instance in the current or specified schema.

## Syntax

```sqlsyntax
CREATE [ OR REPLACE ] SNOWFLAKE.DATA_PRIVACY.CUSTOM_CLASSIFIER
[ IF NOT EXISTS ] <custom_classifier_name>()
```

## Parameters

`custom_classifier_name()`
:   Specifies the identifier (name) for the instance; the name must be unique for the schema in which the object is created. You must add the
    parentheses at the end of the identifier when creating the object.

    In addition, the identifier must start with an alphabetic character and cannot contain spaces or special characters unless the
    entire identifier string is enclosed in double quotes (for example, `"My object"`). Identifiers enclosed in double quotes are also
    case-sensitive.

    For more information, see [Identifier requirements](../../../identifiers-syntax.md).

## Arguments

None.

## Access control requirements

A [role](../../../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../../../user-guide/security-access-control-overview.md) at a minimum:

| Database role | Object | Notes |
| --- | --- | --- |
| CLASSIFICATION_ADMIN | Database role | The account role that creates the object must be granted this database role.  This database role exists in the shared SNOWFLAKE database. |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../../../user-guide/security-access-control-overview.md).

## Methods

You can call the following methods on the custom classification instance that you create:

* [custom_classifier!ADD_REGEX](../methods/add_regex.md)
* [custom_classifier!DELETE_CATEGORY](../methods/delete_category.md)
* [custom_classifier!LIST](../methods/list.md)

## Usage notes

SNOWFLAKE.DATA_PRIVACY.CUSTOM_CLASSIFIER is a name that Snowflake defines and maintains. Use this object name every time you want to create
an instance of this class. Alternatively, update your [search path](../../../snowflake-db-classes.md) to make it easier to use the instance.

## Examples

Create a custom classifier named `medical_codes`:

```sqlexample
CREATE OR REPLACE SNOWFLAKE.DATA_PRIVACY.CUSTOM_CLASSIFIER medical_codes();
```
