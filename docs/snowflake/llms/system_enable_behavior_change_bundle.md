# Source: https://docs.snowflake.com/en/sql-reference/functions/system_enable_behavior_change_bundle.md

Categories:
:   [System functions](../functions-system.md) (System Control)

# SYSTEM$ENABLE_BEHAVIOR_CHANGE_BUNDLE

Enables behavior changes included in the specified [behavior change release bundle](../../release-notes/behavior-change-policy.md) for the
current account.

By default, behavior change bundles are not enabled during the pre-announcement period. Use this function to test behavior changes before they are enabled for your account.

See also:
:   [SYSTEM$DISABLE_BEHAVIOR_CHANGE_BUNDLE](system_disable_behavior_change_bundle.md),
    [SYSTEM$BEHAVIOR_CHANGE_BUNDLE_STATUS](system_behavior_change_bundle_status.md)
    [SYSTEM$SHOW_ACTIVE_BEHAVIOR_CHANGE_BUNDLES](system_show_active_behavior_change_bundles.md)

## Syntax

```sqlsyntax
SYSTEM$ENABLE_BEHAVIOR_CHANGE_BUNDLE( '<bundle_name>' )
```

## Arguments

`bundle_name`
:   Name of the behavior change bundle, specified as a string. To obtain the name for a bundle, see
    [Behavior change announcements](../../release-notes/behavior-changes.md).

## Returns

Returns the VARCHAR value `ENABLED` if the function successfully enables the behavior changes.

## Usage notes

* You cannot call this function from within a stored procedure or user-defined function (UDF).

## Examples

The following example enables the `2020_08` behavior change bundle for the current account.

```sqlexample
SELECT SYSTEM$ENABLE_BEHAVIOR_CHANGE_BUNDLE('2020_08');
```

```output
+-------------------------------------------------+
| SYSTEM$ENABLE_BEHAVIOR_CHANGE_BUNDLE('2020_08') |
|-------------------------------------------------|
| ENABLED                                         |
+-------------------------------------------------+
```
