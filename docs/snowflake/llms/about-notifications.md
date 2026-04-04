# Source: https://docs.snowflake.com/en/user-guide/notifications/about-notifications.md

# Notifications in Snowflake

You can configure Snowflake to send notifications to a queue provided by a Cloud service (Amazon SNS, Google Cloud PubSub, or
Azure Event Grid), an email address, or a webhook. For details, see the following sections:

* [Sending notifications to cloud provider queues (Amazon SNS, Google Cloud PubSub, and Azure Event Grid)](queue-notifications.md)
* [Sending email notifications](email-notifications.md)
* [Sending webhook notifications](webhook-notifications.md)

## Viewing the history of notifications

To view the history of notifications, call the Information Schema [NOTIFICATION_HISTORY](../../sql-reference/functions/notification_history.md) table
function.
