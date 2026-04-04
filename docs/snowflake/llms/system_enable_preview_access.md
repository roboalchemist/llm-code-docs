# Source: https://docs.snowflake.com/en/sql-reference/functions/system_enable_preview_access.md

Categories:
:   [System functions](../functions-system.md) (System Control)

# SYSTEM$ENABLE_PREVIEW_ACCESS

Enables access to [open preview](../../release-notes/preview-features.md) features.

See also:

> [SYSTEM$GET_PREVIEW_ACCESS_STATUS](system_get_preview_access_status.md), [SYSTEM$DISABLE_PREVIEW_ACCESS](system_disable_preview_access.md)

## Syntax

```sqlsyntax
SYSTEM$ENABLE_PREVIEW_ACCESS()
```

## Arguments

None.

## Returns

Returns a VARCHAR status message that open preview features have been enabled:

```output
+---------------------------------------------------------------+
| SELECT SYSTEM$ENABLE_PREVIEW_ACCESS();                        |
+---------------------------------------------------------------+
| Preview access has been successfully enabled for this account |
+---------------------------------------------------------------+
```

## Access control requirements

* Only account administrators (users with the ACCOUNTADMIN role) can execute this function.

## Usage notes

* This is an all-or-nothing setting that affects all users and all previews within an account.
* SYSTEM$ENABLE_PREVIEW_ACCESS only can enable [open preview features](../../release-notes/preview-features.md).

  [Contact Snowflake Support](../../user-guide/contacting-support.md) to enable or re-enable private preview features.
* Snowflake Marketplace products, which are managed separately through [IMPORTED PRIVILEGES](../../user-guide/data-exchange-marketplace-privileges.md),
  are not covered as part of this capability.
* Client-side libraries (such as Snowpark API) are not covered as part of this capability.
* For customers who have not agreed to the Snowflake [Preview Terms of Service](https://www.snowflake.com/legal/preview-terms-of-service/) (“Preview Terms”),
  enabling preview features may not be possible.

  To agree to Preview Terms, contact your account representative or [Snowflake Support](../../user-guide/contacting-support.md) for assistance.

## Examples

Enable preview features:

```sqlexample
USE ROLE ACCOUNTADMIN;
SELECT SYSTEM$ENABLE_PREVIEW_ACCESS();
```
