# Source: https://docs.snowflake.com/en/sql-reference/functions/application_json.md

Categories:
:   [Notification functions](../functions-notification.md) (Message Construction)

# APPLICATION_JSON

Returns a JSON object that specifies the JSON message to use for a notification. This is a helper function that you use to
construct a message object for the [SYSTEM$SEND_SNOWFLAKE_NOTIFICATION](../stored-procedures/system_send_snowflake_notification.md) stored procedure.

See also:
:   [Using SYSTEM$SEND_SNOWFLAKE_NOTIFICATION to send notifications](../../user-guide/notifications/snowflake-notifications.md) ,
    [SYSTEM$SEND_SNOWFLAKE_NOTIFICATION](../stored-procedures/system_send_snowflake_notification.md) ,
    [TEXT_HTML](text_html.md) ,
    [TEXT_PLAIN](text_plain.md)

## Syntax

```sqlsyntax
SNOWFLAKE.NOTIFICATION.APPLICATION_JSON( '<message>' )
```

## Arguments

`'message'`
:   Content of the message to send.

    You do not need to escape the double quotes around strings within the message (for example, double quotes around the keys
    and values). The function escapes these double quotes for you.

## Returns

A JSON-formatted string that specifies a message for the
[SYSTEM$SEND_SNOWFLAKE_NOTIFICATION](../stored-procedures/system_send_snowflake_notification.md) stored procedure to send.

For example, suppose that you call the function and pass in a JSON message:

```sqlexample
SELECT SNOWFLAKE.NOTIFICATION.APPLICATION_JSON('{"data": "hello world"}');
```

The function returns the following JSON-formatted string:

```json
'{"application/json":"{\"data\": \"hello world\"}"}'
```

Note how the function escapes the double quotes around the keys and values in your message.

## Examples

See [Using SYSTEM$SEND_SNOWFLAKE_NOTIFICATION to send notifications](../../user-guide/notifications/snowflake-notifications.md).
