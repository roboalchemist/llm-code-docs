# Source: https://docs.snowflake.com/en/user-guide/notifications/queue-notifications.md

# Sending notifications to cloud provider queues (Amazon SNS, Google Cloud PubSub, and Azure Event Grid)

You can configure Snowflake to send notifications to a queue provided by a cloud service (Amazon SNS, Google Cloud PubSub, or
Azure Event Grid).

* To configure [Snowpipe](../data-load-snowpipe-intro.md) or specific [tasks](../tasks-intro.md) to send
  notifications about errors to a queue, see the following topics:

  * [Snowpipe error notifications](../data-load-snowpipe-errors.md)
  * [Set up error notifications for tasks](../tasks-errors.md)
* To call a stored procedure to send a notification to a queue:

  1. Create a notification integration for the cloud provider queue. For details, see the following topics:

     * [Creating a notification integration to send notifications to an Amazon SNS topic](creating-notification-integration-amazon-sns.md)
     * [Creating a notification integration to send notifications to a Microsoft Azure Event Grid topic](creating-notification-integration-azure-event-grid.md)
     * [Creating a notification integration to send notifications to a Google Cloud Pub/Sub topic](creating-notification-integration-google-pubsub.md)
     > **Note:**
     >
     > Your account must be on the same [cloud platform](../intro-cloud-platforms.md) as the cloud provider queue.
  2. Call the [SYSTEM$SEND_SNOWFLAKE_NOTIFICATION](../../sql-reference/stored-procedures/system_send_snowflake_notification.md) stored procedure to send the notification
     message to the queue. For details, see [Using SYSTEM$SEND_SNOWFLAKE_NOTIFICATION to send notifications](snowflake-notifications.md).
