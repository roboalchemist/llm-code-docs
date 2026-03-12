# Source: https://docs.snowflake.com/en/sql-reference/functions/system_is_application_all_mandatory_telemetry_event_definitions_enabled.md

Categories:
:   [System functions](../functions-system.md) (System Information)

# SYSTEM$IS_APPLICATION_ALL_MANDATORY_TELEMETRY_EVENT_DEFINITIONS_ENABLED

Indicates that the AUTHORIZE_TELEMETRY_EVENT_SHARING property has been set on the app.

## Syntax

```sqlsyntax
SYSTEM$IS_APPLICATION_ALL_MANDATORY_TELEMETRY_EVENT_DEFINITIONS_ENABLED
```

## Returns

* Returns `TRUE` if the AUTHORIZE_TELEMETRY_EVENT_SHARING property is set
  on the app. This indicates that event sharing is allowed in the consumer account.
  Otherwise, returns `FALSE`.

  For more information, see [Determine information about event sharing in the consumer account](../../developer-guide/native-apps/event-develop.md).
