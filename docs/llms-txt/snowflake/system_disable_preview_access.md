# Source: https://docs.snowflake.com/en/sql-reference/functions/system_disable_preview_access.md

Categories:
:   [System functions](../functions-system.md) (System Control)

# SYSTEM$DISABLE_PREVIEW_ACCESS

Disables access to [open preview](../../release-notes/preview-features.md) and private preview features.

See also:

> [SYSTEM$GET_PREVIEW_ACCESS_STATUS](system_get_preview_access_status.md), [SYSTEM$ENABLE_PREVIEW_ACCESS](system_enable_preview_access.md)

## Syntax

```sqlsyntax
SYSTEM$DISABLE_PREVIEW_ACCESS()
```

## Arguments

None.

## Returns

Returns a VARCHAR status message that preview features have been disabled:

```output
+----------------------------------------------------------------+
| SYSTEM$DISABLE_PREVIEW_ACCESS()                                |
+----------------------------------------------------------------+
| Preview access has been successfully disabled for this account |
+----------------------------------------------------------------+
```

## Access control requirements

* Only account administrators (users with the ACCOUNTADMIN role) can execute this function.

## Usage notes

* Applies to both private and open preview features.
* This is an all-or-nothing setting that affects all users and all previews within an account.
* Any user in the account who is using a preview feature will lose access to that feature immediately after SYSTEM$DISABLE_PREVIEW_ACCESS is executed.
* Snowflake Marketplace products, which are managed separately through [IMPORTED PRIVILEGES](../../user-guide/data-exchange-marketplace-privileges.md), are not covered as part of this capability.
* Client-side libraries (such as Snowpark API) are not covered as part of this capability.

## Examples

Disable preview features:

```sqlexample
USE ROLE ACCOUNTADMIN;
SELECT SYSTEM$DISABLE_PREVIEW_ACCESS();
```
