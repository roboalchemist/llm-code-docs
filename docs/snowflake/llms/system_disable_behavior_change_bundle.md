# Source: https://docs.snowflake.com/en/sql-reference/functions/system_disable_behavior_change_bundle.md

Categories:
:   [System functions](../functions-system.md) (System Control)

# SYSTEM$DISABLE_BEHAVIOR_CHANGE_BUNDLE

Disables the behavior changes included in the specified [behavior change release bundle](../../release-notes/behavior-change-policy.md)
for the current account.

You can call this function for a particular bundle at the beginning of the
[testing period](../../release-notes/behavior-change-policy.md) for that bundle and becomes unavailable after the
[opt-out period](../../release-notes/behavior-change-policy.md) for that bundle.

An error occurs in either of the following cases:

* You call this function before the testing period for that bundle begins.
* You call this function after the opt-out period for that bundle ends.

If you call this function to disable a behavior change bundle during the testing period, the bundle remains disabled until you
enable it again or until the end of the opt-out period. Snowflake does not override this setting at the beginning of the opt-out
period, when the bundle becomes enabled by default.

See also:
:   [SYSTEM$ENABLE_BEHAVIOR_CHANGE_BUNDLE](system_enable_behavior_change_bundle.md),
    [SYSTEM$BEHAVIOR_CHANGE_BUNDLE_STATUS](system_behavior_change_bundle_status.md),
    [SYSTEM$SHOW_ACTIVE_BEHAVIOR_CHANGE_BUNDLES](system_show_active_behavior_change_bundles.md)

## Syntax

```sqlsyntax
SYSTEM$DISABLE_BEHAVIOR_CHANGE_BUNDLE( '<bundle_name>' )
```

## Arguments

`bundle_name`
:   Name of the behavior change bundle, specified as a string. To obtain the name for a bundle, see
    [Behavior change announcements](../../release-notes/behavior-changes.md).

## Returns

Returns the VARCHAR value `DISABLED` if the function successfully disables the behavior changes.

## Examples

The following example disables the `2020_08` behavior change bundle for the current account.

```sqlexample
SELECT SYSTEM$DISABLE_BEHAVIOR_CHANGE_BUNDLE('2020_08');
```

```output
+--------------------------------------------------+
| SYSTEM$DISABLE_BEHAVIOR_CHANGE_BUNDLE('2020_08') |
|--------------------------------------------------|
| DISABLED                                         |
+--------------------------------------------------+
```
