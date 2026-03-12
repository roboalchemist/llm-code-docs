# Source: https://docs.snowflake.com/en/sql-reference/functions-notification.md

# Notification functions

Notification functions are helper functions that you can call when using the
[SYSTEM$SEND_SNOWFLAKE_NOTIFICATION](stored-procedures/system_send_snowflake_notification.md) stored procedure to
[send a notification](../user-guide/notifications/snowflake-notifications.md).

The integration configuration and message construction functions return JSON-formatted strings that you pass to the
SYSTEM$SEND_SNOWFLAKE_NOTIFICATION stored procedure.

| Sub-category | Function | Notes |
| --- | --- | --- |
| Integration Configuration | [EMAIL_INTEGRATION_CONFIG](functions/email_integration_config.md) |  |
|  | [INTEGRATION](functions/integration.md) |  |
| Message Construction | [APPLICATION_JSON](functions/application_json.md) |  |
|  | [TEXT_HTML](functions/text_html.md) |  |
|  | [TEXT_PLAIN](functions/text_plain.md) |  |
| Message Sanitization | [SANITIZE_WEBHOOK_CONTENT](functions/sanitize_webhook_content.md) |  |
