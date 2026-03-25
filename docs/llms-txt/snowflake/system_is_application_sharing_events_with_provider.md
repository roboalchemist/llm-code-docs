# Source: https://docs.snowflake.com/en/sql-reference/functions/system_is_application_sharing_events_with_provider.md

Categories:
:   [System functions](../functions-system.md) (System Information)

# SYSTEM$IS_APPLICATION_SHARING_EVENTS_WITH_PROVIDER

Shows if event sharing is enabled.

See also:
:   [SYSTEM$IS_APPLICATION_INSTALLED_FROM_SAME_ACCOUNT](system_is_application_installed_from_same_account.md)

For more information about event sharing, see [Use logging and event tracing for an app](../../developer-guide/native-apps/event-about.md).

## Syntax

```sqlsyntax
SYSTEM$IS_APPLICATION_SHARING_EVENTS_WITH_PROVIDER()
```

## Arguments

None.

## Returns

This function returns the following status messages:

| Status Message | Description |
| --- | --- |
| TRUE | Indicates that event sharing is enabled on the app and the app has an active event table. |
| FALSE | Indicates that event sharing is not enabled on the app. |

## Access control requirements

* These system functions can only be called from within an app.

## Examples

```sqlexample
SELECT SYSTEM$IS_APPLICATION_SHARING_EVENTS_WITH_PROVIDER();
```
