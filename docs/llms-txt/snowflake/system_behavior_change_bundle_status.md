# Source: https://docs.snowflake.com/en/sql-reference/functions/system_behavior_change_bundle_status.md

Categories:
:   [System functions](../functions-system.md) (System Control)

# SYSTEM$BEHAVIOR_CHANGE_BUNDLE_STATUS

Returns the status of the specified [behavior change release bundle](../../release-notes/behavior-change-policy.md) for the current account.

See also:
:   [SYSTEM$ENABLE_BEHAVIOR_CHANGE_BUNDLE](system_enable_behavior_change_bundle.md),
    [SYSTEM$DISABLE_BEHAVIOR_CHANGE_BUNDLE](system_disable_behavior_change_bundle.md),
    [SYSTEM$SHOW_ACTIVE_BEHAVIOR_CHANGE_BUNDLES](system_show_active_behavior_change_bundles.md)

## Syntax

```sqlsyntax
SYSTEM$BEHAVIOR_CHANGE_BUNDLE_STATUS( '<bundle_name>' )
```

## Arguments

`bundle_name`
:   Name of the behavior change bundle, specified as a string. To obtain the name for a bundle, see
    [Behavior change announcements](../../release-notes/behavior-changes.md).

## Returns

Returns one of the following VARCHAR values:

* `ENABLED` (if the specified bundle is enabled for the current account)
* `DISABLED` (if the specified bundle is disabled for the current account)
* `RELEASED` (if the specified bundle is
  [generally enabled](../../release-notes/behavior-change-policy.md) for the current account and thus permanently enabled)

## Examples

The following example returns the status of the `2020_08` behavior change bundle for the current account.

```sqlexample
SELECT SYSTEM$BEHAVIOR_CHANGE_BUNDLE_STATUS('2020_08');
```

```output
+-------------------------------------------------+
| SYSTEM$BEHAVIOR_CHANGE_BUNDLE_STATUS('2020_08') |
|-------------------------------------------------|
| DISABLED                                        |
+-------------------------------------------------+
```
