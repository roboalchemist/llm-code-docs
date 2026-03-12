# Source: https://docs.snowflake.com/en/sql-reference/classes/classification_profile/methods/set_minimum_object_age_for_classification_days.md

# <classification_profile_name>!SET_MINIMUM_OBJECT_AGE_FOR_CLASSIFICATION_DAYS

Specifies the minimum number of days an object must exist before it is eligible to be automatically classified by an instance of the
CLASSIFICATION_PROFILE class.

## Syntax

```sqlsyntax
<classification_profile_name>!SET_MINIMUM_OBJECT_AGE_FOR_CLASSIFICATION_DAYS( <days> )
```

## Arguments

`days`
:   Specifies the INTEGER number of days to wait before a table is eligible to be classified.

    The value must be equal to or greater than `0`.

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

Set the minimum number of days to be `1` before a table can be automatically classified:

```sqlexample
CALL my_classification_profile!SET_MINIMUM_OBJECT_AGE_FOR_CLASSIFICATION_DAYS(1);
```
