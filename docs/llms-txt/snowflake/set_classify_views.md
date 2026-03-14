# Source: https://docs.snowflake.com/en/sql-reference/classes/classification_profile/methods/set_classify_views.md

# <classification_profile_name>!SET_CLASSIFY_VIEWS

Specifies whether to classify views during sensitive data classification.

## Syntax

```sqlsyntax
<classification_profile_name>!SET_CLASSIFY_VIEWS( <boolean_value> )
```

## Arguments

`boolean_value`
:   Specifies whether to enable classification of views for the instance of the CLASSIFICATION_PROFILE class.

    TRUE enables the classification of views.

    FALSE disables the classification of views. Only tables will be classified by sensitive data classification.

    Default: FALSE

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

Configure the classification profile so that views are classified along with tables:

```sqlexample
CALL my_classification_profile!SET_CLASSIFY_VIEWS(true);
```

Disable view classification for the classification profile:

```sqlexample
CALL my_classification_profile!SET_CLASSIFY_VIEWS(false);
```
