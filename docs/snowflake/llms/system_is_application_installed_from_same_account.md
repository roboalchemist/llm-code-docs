# Source: https://docs.snowflake.com/en/sql-reference/functions/system_is_application_installed_from_same_account.md

Categories:
:   [System functions](../functions-system.md) (System Information)

# SYSTEM$IS_APPLICATION_INSTALLED_FROM_SAME_ACCOUNT

Shows if an app is installed on the same account as the application package it is based on.

See also:
:   [SYSTEM$IS_APPLICATION_SHARING_EVENTS_WITH_PROVIDER](system_is_application_sharing_events_with_provider.md)

For more information about event sharing, see [Use logging and event tracing for an app](../../developer-guide/native-apps/event-about.md).

## Syntax

```sqlsyntax
SYSTEM$IS_APPLICATION_INSTALLED_FROM_SAME_ACCOUNT()
```

## Arguments

None.

## Returns

This function returns the following status messages:

| Status Message | Description |
| --- | --- |
| TRUE | Indicates if an app is installed on the same account as the application package it is based on. |
| FALSE | Indicates if an app is not installed on the same account as the application package it is based on. |

## Access control requirements

* These system functions can only be called from within an app.

## Examples

```sqlexample
SELECT SYSTEM$IS_APPLICATION_INSTALLED_FROM_SAME_ACCOUNT();
```
