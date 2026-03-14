# Source: https://docs.snowflake.com/en/sql-reference/functions/system_get_preview_access_status.md

Categories:
:   [System functions](../functions-system.md) (System Information)

# SYSTEM$GET_PREVIEW_ACCESS_STATUS

Determine if access to all preview features is enabled or disabled.

See also:

> [SYSTEM$DISABLE_PREVIEW_ACCESS](system_disable_preview_access.md), [SYSTEM$ENABLE_PREVIEW_ACCESS](system_enable_preview_access.md)

## Syntax

```sqlsyntax
SYSTEM$GET_PREVIEW_ACCESS_STATUS()
```

## Arguments

None.

## Returns

Returns a VARCHAR status message representing whether preview features are enabled or disabled as shown below:

* Enabled:

  ```output
  +--------------------------------------------+
  | SYSTEM$GET_PREVIEW_ACCESS_STATUS()         |
  +--------------------------------------------+
  | Preview access is ENABLED for this account |
  +--------------------------------------------+
  ```

* Disabled:

  ```output
  +---------------------------------------------+
  | SYSTEM$GET_PREVIEW_ACCESS_STATUS()          |
  |---------------------------------------------|
  | Preview access is DISABLED for this account |
  +---------------------------------------------+
  ```

## Access control requirements

The SYSTEM$GET_PREVIEW_ACCESS_STATUS function can be executed by any user in the account and does not require special privileges.

## Examples

Display the current state of preview features.

```sqlexample
SELECT SYSTEM$GET_PREVIEW_ACCESS_STATUS();
```
