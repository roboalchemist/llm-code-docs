# Source: https://docs.snowflake.com/en/sql-reference/classes/classification_profile/methods/unset_custom_classifiers.md

# <classification_profile_name>!UNSET_CUSTOM_CLASSIFIERS

Remove [custom classifiers](../../../../user-guide/classify-custom.md) from the classification profile.

## Syntax

```sqlsyntax
<classification_profile_name>!UNSET_CUSTOM_CLASSIFIERS()
```

## Returns

Returns a successful status message or an error message.

## Access control requirements

A [role](../../../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../../../user-guide/security-access-control-overview.md) at a minimum:

| Instance role | Object | Notes |
| --- | --- | --- |
| `classification_profile`!PRIVACY_USER | The classification profile instance. | The account role that calls this method must be granted this instance role on the classification profile. The role used to create the instance is automatically granted this instance role. |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../../../user-guide/security-access-control-overview.md).

## Usage notes

Calling this method does not return the object. Because of this, you can’t use method chaining to call another method on the
return value of this method. Instead, call each method in a separate SQL statement.

## Examples

Remove custom classifiers from the `my_classification_profile` profile:

```sqlexample
CALL my_classification_profile!UNSET_CUSTOM_CLASSIFIERS();
```
