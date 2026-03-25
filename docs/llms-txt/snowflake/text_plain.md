# Source: https://docs.snowflake.com/en/sql-reference/functions/text_plain.md

Categories:
:   [Notification functions](../functions-notification.md) (Message Construction)

# TEXT_PLAIN

Returns a JSON object that specifies the plain text message to use for a notification. This is a helper function that you use to
construct a message object for the [SYSTEM$SEND_SNOWFLAKE_NOTIFICATION](../stored-procedures/system_send_snowflake_notification.md) stored procedure.

See also:
:   [Using SYSTEM$SEND_SNOWFLAKE_NOTIFICATION to send notifications](../../user-guide/notifications/snowflake-notifications.md) ,
    [SYSTEM$SEND_SNOWFLAKE_NOTIFICATION](../stored-procedures/system_send_snowflake_notification.md) ,
    [TEXT_HTML](text_html.md) ,
    [APPLICATION_JSON](application_json.md)

## Syntax

```sqlsyntax
SNOWFLAKE.NOTIFICATION.TEXT_PLAIN( '<message>' )
```

## Arguments

`'message'`
:   Content of the message to send.

## Returns

A JSON-formatted string that specifies a message for the
[SYSTEM$SEND_SNOWFLAKE_NOTIFICATION](../stored-procedures/system_send_snowflake_notification.md) stored procedure to send.

For example:

```json
'{"text/plain":"A message"}'
```

## Examples

See [Using SYSTEM$SEND_SNOWFLAKE_NOTIFICATION to send notifications](../../user-guide/notifications/snowflake-notifications.md).
