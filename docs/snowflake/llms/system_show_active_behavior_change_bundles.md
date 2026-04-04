# Source: https://docs.snowflake.com/en/sql-reference/functions/system_show_active_behavior_change_bundles.md

Categories:
:   [System functions](../functions-system.md) (System Information)

# SYSTEM$SHOW_ACTIVE_BEHAVIOR_CHANGE_BUNDLES

Returns an array of the currently available [behavior change release bundles](../../release-notes/behavior-change-policy.md), the default
state of each bundle, and the actual state of the bundle for the current account.

See also:
:   [SYSTEM$ENABLE_BEHAVIOR_CHANGE_BUNDLE](system_enable_behavior_change_bundle.md),
    [SYSTEM$DISABLE_BEHAVIOR_CHANGE_BUNDLE](system_disable_behavior_change_bundle.md),
    [SYSTEM$BEHAVIOR_CHANGE_BUNDLE_STATUS](system_behavior_change_bundle_status.md)

## Syntax

```sqlsyntax
SYSTEM$SHOW_ACTIVE_BEHAVIOR_CHANGE_BUNDLES()
```

## Arguments

None.

## Returns

Returns a VARCHAR value that contains an array of objects that represent the currently available behavior change bundles.
Each object contains the following keys, which describe the status of the bundle:

| Key | Description of value |
| --- | --- |
| `name` | Name of the behavior change bundle |
| `isDefault` | `true` if the associated bundle should be enabled by default for the current account; `false` otherwise. |
| `isEnabled` | `true` if the associated bundle is actually enabled by default for the current account; `false` otherwise. |

## Usage notes

* Calling [SYSTEM$ENABLE_BEHAVIOR_CHANGE_BUNDLE](system_enable_behavior_change_bundle.md) or [SYSTEM$DISABLE_BEHAVIOR_CHANGE_BUNDLE](system_disable_behavior_change_bundle.md) changes the value of
  `isEnabled` for the specified bundle.
* [SYSTEM$BEHAVIOR_CHANGE_BUNDLE_STATUS](system_behavior_change_bundle_status.md) returns the same information as this function for a
  specific bundle.

## Examples

The following example returns information about the current behavior change bundles.

```sqlexample
SELECT SYSTEM$SHOW_ACTIVE_BEHAVIOR_CHANGE_BUNDLES();
```

```output
+--------------------------------------------------------------------------------------------------------------+
| SYSTEM$SHOW_ACTIVE_BEHAVIOR_CHANGE_BUNDLES()                                                                 |
|--------------------------------------------------------------------------------------------------------------|
| [{"name":"2023_08","isDefault":true,"isEnabled":true},{"name":"2024_01","isDefault":false,"isEnabled":true}] |
+--------------------------------------------------------------------------------------------------------------+
```

The following example uses the [PARSE_JSON](parse_json.md) function to return the array as a VARIANT and then uses the [FLATTEN](flatten.md)
function to present the bundle information in a tabular format.

```sqlexample
SELECT
    bundles.VALUE:name::VARCHAR AS bundle_name,
    bundles.VALUE:isDefault::BOOLEAN AS is_enabled_by_default,
    bundles.VALUE:isEnabled::BOOLEAN AS is_actually_enabled_in_account
  FROM
    TABLE(FLATTEN(input => PARSE_JSON(SYSTEM$SHOW_ACTIVE_BEHAVIOR_CHANGE_BUNDLES())))
    AS bundles;
```

```output
+-------------+-----------------------+--------------------------------+
| BUNDLE_NAME | IS_ENABLED_BY_DEFAULT | IS_ACTUALLY_ENABLED_IN_ACCOUNT |
|-------------+-----------------------+--------------------------------|
| 2023_08     | True                  | True                           |
| 2024_01     | False                 | True                           |
+-------------+-----------------------+--------------------------------+
```
