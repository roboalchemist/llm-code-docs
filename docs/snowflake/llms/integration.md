# Source: https://docs.snowflake.com/en/sql-reference/functions/integration.md

Categories:
:   [Notification functions](../functions-notification.md) (Integration Configuration)

# INTEGRATION

Returns a JSON object that specifies the notification integration to use to send a message. This is a helper function that you
use to construct an integration configuration object for the
[SYSTEM$SEND_SNOWFLAKE_NOTIFICATION](../stored-procedures/system_send_snowflake_notification.md) stored procedure.

See also:
:   [Using SYSTEM$SEND_SNOWFLAKE_NOTIFICATION to send notifications](../../user-guide/notifications/snowflake-notifications.md) ,
    [SYSTEM$SEND_SNOWFLAKE_NOTIFICATION](../stored-procedures/system_send_snowflake_notification.md) ,
    [EMAIL_INTEGRATION_CONFIG](email_integration_config.md)

## Syntax

```sqlsyntax
SNOWFLAKE.NOTIFICATION.INTEGRATION( '<integration_name>' )
```

## Arguments

`'integration_name'`
:   Name of the notification integration to use.

## Returns

A JSON-formatted string that specifies a notification integration for the
[SYSTEM$SEND_SNOWFLAKE_NOTIFICATION](../stored-procedures/system_send_snowflake_notification.md) stored procedure to send.

For example, if you pass in the notification integration name `'my_queue_int'`, the function returns:

```json
'{"my_queue_int":{}}'
```

## Examples

See [Using SYSTEM$SEND_SNOWFLAKE_NOTIFICATION to send notifications](../../user-guide/notifications/snowflake-notifications.md).
