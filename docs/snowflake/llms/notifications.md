# Source: https://docs.snowflake.com/en/user-guide/budgets/notifications.md

# Notifications for budgets

To receive notifications when your credit usage is expected to exceed your spending limits, you must set up the budget so that
notifications can be sent to the destination of your choice. You can receive notifications through the following means:

* Email.
* Messages pushed to a queue provided by a cloud service (Amazon SNS, Azure Event Grid, or Google Cloud PubSub).
* Calls to a webhook for Slack, Microsoft Teams, or PagerDuty.

> **Note:**
>
> Email notifications are processed through Snowflake’s Amazon Web Services (AWS) deployments, using AWS Simple Email Service
> (SES). The content of an email message sent using AWS may be retained by Snowflake for up to thirty days to manage the delivery
> of the message. After this period, the message content is deleted.

## Controlling when notifications are sent

By default, notifications begin when the projected spending is more than 10% above the spending limit of the budget.

You can override this default by defining a notification threshold, which is a percentage of the budget’s spending limit. Notifications are
sent when Snowflake predicts that spending will exceed the threshold.

For example, suppose you want notifications sent when projected spending exceeds 50% of the budget’s spending limit. To set this
notification threshold for the account budget, run the following command:

```sqlexample
CALL SNOWFLAKE.LOCAL.ACCOUNT_ROOT_BUDGET!SET_NOTIFICATION_THRESHOLD(50);
```

You can also set a notification threshold for custom budgets.

If you want to reset the notification threshold to the default, call the
[<budget_name>!SET_NOTIFICATION_THRESHOLD](../../sql-reference/classes/budget/methods/set_notification_threshold.md) method with `110` as the argument.

## Setting up email notification

To set up email notification:

1. (Optional) If you want to use your own notification integration, create a notification integration or choose an existing
   notification integration that you want to use. A notification integration enables Snowflake to send notifications to a
   third-party system.

   1. Create a notification integration with TYPE = EMAIL and ALLOWED_RECIPIENTS set to the list of verified email addresses of
      the recipients. For information, see [Create an email notification integration](../notifications/email-notifications.md) and
      [Restrict the list of email addresses that can receive notifications](../notifications/email-notifications.md).

      > **Note:**
      >
      > Each email address added for budget notifications must be [verified](../notifications/email-notifications.md). The
      > email notification setup fails if any email address in the list is *not* verified.

      For example:

      ```sqlexample
      CREATE NOTIFICATION INTEGRATION budgets_notification_integration
        TYPE = EMAIL
        ENABLED = TRUE
        ALLOWED_RECIPIENTS = ('costadmin@example.com','budgetadmin@example.com');
      ```

   2. Verify that the notification integration works as expected by calling the
      [SYSTEM$SEND_SNOWFLAKE_NOTIFICATION](../../sql-reference/stored-procedures/system_send_snowflake_notification.md) stored procedure to send a test message.

      For example, you can send a test message in JSON format:

      ```sqlexample
      CALL SYSTEM$SEND_SNOWFLAKE_NOTIFICATION(
        SNOWFLAKE.NOTIFICATION.APPLICATION_JSON('{"name": "value"}'),
        SNOWFLAKE.NOTIFICATION.INTEGRATION('budgets_notification_integration')
      );
      ```

   3. Grant the USAGE privilege on the notification integration to the SNOWFLAKE application. The USAGE privilege enables the
      budget to use the notification integration to send the notification. For example:

      ```sqlexample
      GRANT USAGE ON INTEGRATION budgets_notification_integration
        TO APPLICATION snowflake;
      ```

2. Specify the email addresses that should receive the notification. If you created or selected a notification integration to use,
   associate the notification integration with the budget.

   To do this, call the [<budget_name>!SET_EMAIL_NOTIFICATIONS](../../sql-reference/classes/budget/methods/set_email_notifications.md) method, and specify the following:

   * If you do not have a notification integration that you want to use, pass in a comma-delimited list of verified email
     addresses. For example, if you are configuring notifications for the account budget:

     ```sqlexample
     CALL SNOWFLAKE.LOCAL.ACCOUNT_ROOT_BUDGET!SET_EMAIL_NOTIFICATIONS(
       'costadmin@example.com, budgetadmin@example.com'
     );
     ```

     If you are configuring notifications for a custom budget, call the method on the object for the custom budget. For example,
     if you created a custom budget named `my_budget`:

     ```sqlexample
     CALL my_budget!SET_EMAIL_NOTIFICATIONS(
       'costadmin@example.com, budgetadmin@example.com'
     );
     ```

   * If you have a notification integration that you want to use, pass in the name of that integration and a comma-delimited list
     of verified email addresses. For example, if you are configuring notifications for the account budget:

     ```sqlexample
     CALL SNOWFLAKE.LOCAL.ACCOUNT_ROOT_BUDGET!SET_EMAIL_NOTIFICATIONS(
       'budgets_notification_integration',
       'costadmin@example.com, budgetadmin@example.com'
     );
     ```

     If you are configuring notifications for a custom budget, call the method on the object for the custom budget. For example,
     if you created a custom budget named `my_budget`:

     ```sqlexample
     CALL my_budget!SET_EMAIL_NOTIFICATIONS(
       'budgets_notification_integration',
       'costadmin@example.com, budgetadmin@example.com'
     );
     ```

3. If you associated a notification integration with the budget, you can verify that the budget is associated with your
   notification integration by calling the
   [<budget_name>!GET_NOTIFICATION_INTEGRATION_NAME](../../sql-reference/classes/budget/methods/get_notification_integration_name.md) method. This method returns the name of the
   email notification integration associated with the budget.

   For example, if you are configuring notifications for the account budget:

   ```sqlexample
   CALL SNOWFLAKE.LOCAL.ACCOUNT_ROOT_BUDGET!GET_NOTIFICATION_INTEGRATION_NAME();
   ```

   If you are configuring notifications for a custom budget, call the method on the object for the custom budget. For example,
   if you created a custom budget named `my_budget`:

   ```sqlexample
   CALL my_budget!GET_NOTIFICATION_INTEGRATION_NAME();
   ```

## Setting up queue notification

To set up queue notification:

1. Create a notification integration or choose an existing notification integration that you want to use. A notification
   integration enables Snowflake to send notifications to a third-party system.

   Create a notification integration with TYPE=QUEUE, DIRECTION=OUTBOUND, and the additional properties required for the cloud
   provider. For information, see:

   * [Creating a notification integration to send notifications to an Amazon SNS topic](../notifications/creating-notification-integration-amazon-sns.md)
   * [Creating a notification integration to send notifications to a Microsoft Azure Event Grid topic](../notifications/creating-notification-integration-azure-event-grid.md)
   * [Creating a notification integration to send notifications to a Google Cloud Pub/Sub topic](../notifications/creating-notification-integration-google-pubsub.md)
   > **Note:**
   >
   > Your account must be on the same [cloud platform](../intro-cloud-platforms.md) as the cloud provider queue.

   For example:

   ```sqlexample
   CREATE OR REPLACE NOTIFICATION INTEGRATION budgets_notification_integration
     ENABLED = TRUE
     TYPE = QUEUE
     DIRECTION = OUTBOUND
     NOTIFICATION_PROVIDER = AWS_SNS
     AWS_SNS_TOPIC_ARN = '<ARN_for_my_SNS_topic>'
     AWS_SNS_ROLE_ARN = '<ARN_for_my_IAM_role>';
   ```

   > **Note:**
   >
   > For queue and webhook notifications, you can associate up to 10 notification integrations with a budget.
2. Verify that the notification integration works as expected by calling the
   [SYSTEM$SEND_SNOWFLAKE_NOTIFICATION](../../sql-reference/stored-procedures/system_send_snowflake_notification.md) stored procedure to send a test message.

   For example, you can send a test message in JSON format:

   ```sqlexample
   CALL SYSTEM$SEND_SNOWFLAKE_NOTIFICATION(
     SNOWFLAKE.NOTIFICATION.APPLICATION_JSON('{"name": "value"}'),
     SNOWFLAKE.NOTIFICATION.INTEGRATION('budgets_notification_integration')
   );
   ```

3. Grant the USAGE privilege on the notification integration to the SNOWFLAKE application. The USAGE privilege enables the budget
   to use the notification integration to send the notification. For example:

   ```sqlexample
   GRANT USAGE ON INTEGRATION budgets_notification_integration
     TO APPLICATION snowflake;
   ```

4. Associate the notification integration with the budget. Call the
   [<budget_name>!ADD_NOTIFICATION_INTEGRATION](../../sql-reference/classes/budget/methods/add_notification_integration.md) method, passing in the name of the integration.

   For example, if you are configuring notifications for the account budget:

   ```sqlexample
   CALL SNOWFLAKE.LOCAL.ACCOUNT_ROOT_BUDGET!ADD_NOTIFICATION_INTEGRATION(
     'budgets_notification_integration',
   );
   ```

   If you are configuring notifications for a custom budget, call the method on the object for the custom budget. For example,
   if you created a custom budget named `my_budget`:

   ```sqlexample
   CALL my_budget!ADD_NOTIFICATION_INTEGRATION(
     'budgets_notification_integration',
   );
   ```

5. Verify that the notification integration is associated with the budget.

   Call the [<budget_name>!GET_NOTIFICATION_INTEGRATIONS](../../sql-reference/classes/budget/methods/get_notification_integrations.md) method to print out the list of
   notification integrations associated with the budget.

   For example, if you are configuring notifications for the account budget:

   ```sqlexample
   CALL SNOWFLAKE.LOCAL.ACCOUNT_ROOT_BUDGET!GET_NOTIFICATION_INTEGRATIONS();
   ```

   If you are configuring notifications for a custom budget, call the method on the object for the custom budget. For example,
   if you created a custom budget named `my_budget`:

   ```sqlexample
   CALL my_budget!GET_NOTIFICATION_INTEGRATIONS();
   ```

   The method prints out a table that lists the names of the integrations, the times that they were last used to send
   notifications, and the dates when they were added.

   ```output
   +----------------------------------+------------------------+------------+
   |  INTEGRATION_NAME                | LAST_NOTIFICATION_TIME | ADDED_DATE |
   +----------------------------------+------------------------+------------+
   | budgets_notification_integration | -1                     | 2024-09-23 |
   +----------------------------------+------------------------+------------+
   ```

## Setting up webhook notification

To set up webhook notification:

1. Create a notification integration or choose an existing notification integration that you want to use. A notification
   integration enables Snowflake to send notifications to a third-party system.

   Create a notification integration with TYPE=WEBHOOK and the additional properties required for the webhook. For information,
   see [Sending webhook notifications](../notifications/webhook-notifications.md).

   The notification message is in JSON format, so you should configure the notification integration to handle this. For example,
   the following statements create a secret and a notification integration for a Slack webhook:

   ```sqlexample
   CREATE OR REPLACE SECRET my_database.my_schema.slack_secret
     TYPE = GENERIC_STRING
     SECRET_STRING = '... secret in my Slack webhook URL ...';

   CREATE OR REPLACE NOTIFICATION INTEGRATION budgets_notification_integration
     ENABLED = TRUE
     TYPE = WEBHOOK
     WEBHOOK_URL = 'https://hooks.slack.com/services/SNOWFLAKE_WEBHOOK_SECRET'
     WEBHOOK_BODY_TEMPLATE='{"text": "SNOWFLAKE_WEBHOOK_MESSAGE"}'
     WEBHOOK_HEADERS=('Content-Type'='application/json')
     WEBHOOK_SECRET = slack_secret;
   ```

   > **Note:**
   >
   > For queue and webhook notifications, you can associate up to 10 notification integrations with a budget.
2. Verify that the notification integration works as expected by calling the
   [SYSTEM$SEND_SNOWFLAKE_NOTIFICATION](../../sql-reference/stored-procedures/system_send_snowflake_notification.md) stored procedure to send a test message.

   For example, you can send a test message in JSON format. Make sure to escape the double quotes in the JSON string and the
   backslashes:

   ```sqlexample
   CALL SYSTEM$SEND_SNOWFLAKE_NOTIFICATION(
     SNOWFLAKE.NOTIFICATION.APPLICATION_JSON('{\\\"name\\\": \\\"value\\\"}'),
     SNOWFLAKE.NOTIFICATION.INTEGRATION('budgets_notification_integration')
   );
   ```

3. Grant the USAGE privilege on the notification integration to the SNOWFLAKE application. The USAGE privilege enables the budget
   to use the notification integration to send the notification. For example:

   ```sqlexample
   GRANT USAGE ON INTEGRATION budgets_notification_integration
     TO APPLICATION snowflake;
   ```

4. If you are using a webhook notification integration that relies on a secret, grant the following privileges to the
   SNOWFLAKE application.

   * The READ privilege on that secret.
   * The USAGE privilege on the schema containing that secret.
   * The USAGE privilege on the database containing that schema.

   For example:

   ```sqlexample
   GRANT READ ON SECRET slack_secret TO APPLICATION snowflake;
   GRANT USAGE ON SCHEMA my_schema TO APPLICATION snowflake;
   GRANT USAGE ON DATABASE my_database TO APPLICATION snowflake;
   ```

5. Associate the notification integration with the budget.

   Call the [<budget_name>!ADD_NOTIFICATION_INTEGRATION](../../sql-reference/classes/budget/methods/add_notification_integration.md) method, and pass in the name of the
   integration.

   For example, if you are configuring notifications for the account budget:

   ```sqlexample
   CALL SNOWFLAKE.LOCAL.ACCOUNT_ROOT_BUDGET!ADD_NOTIFICATION_INTEGRATION(
     'budgets_notification_integration',
   );
   ```

   If you are configuring notifications for a custom budget, call the method on the object for the custom budget. For example,
   if you created a custom budget named `my_budget`:

   ```sqlexample
   CALL my_budget!ADD_NOTIFICATION_INTEGRATION(
     'budgets_notification_integration',
   );
   ```

6. Verify that the notification integration is associated with the budget.

   Call the [<budget_name>!GET_NOTIFICATION_INTEGRATIONS](../../sql-reference/classes/budget/methods/get_notification_integrations.md) method, which prints out the list of
   notification integrations associated with the budget.

   For example, if you are configuring notifications for the account budget:

   ```sqlexample
   CALL SNOWFLAKE.LOCAL.ACCOUNT_ROOT_BUDGET!GET_NOTIFICATION_INTEGRATIONS();
   ```

   If you are configuring notifications for a custom budget, call the method on the object for the custom budget. For example,
   if you created a custom budget named `my_budget`:

   ```sqlexample
   CALL my_budget!GET_NOTIFICATION_INTEGRATIONS();
   ```

   The method prints out a table that lists the names of the integrations, the times that they were last used to send
   notifications, and the dates when they were added.

   ```output
   +----------------------------------+------------------------+------------+
   |  INTEGRATION_NAME                | LAST_NOTIFICATION_TIME | ADDED_DATE |
   +----------------------------------+------------------------+------------+
   | budgets_notification_integration | -1                     | 2024-09-23 |
   +----------------------------------+------------------------+------------+
   ```

## Interpreting the JSON notification message

When you configure a budget to send a notification to a cloud provider queue or a webhook, the notification message contains a
JSON object similar to the following:

```json
{
  "account_name": "MY_ACCOUNT",
  "budget_name": "MY_BUDGET_NAME",
  "type": "BUDGET_LIMIT_WARNING",
  "limit": "100",
  "spending": "67.42",
  "spending_percent": "67.42",
  "spending_trend_percent": "130.63",
  "time_percent":"51.61"
}
```

The JSON object contains the following key-value pairs:

| Key | Description |
| --- | --- |
| `account_name` | Name of your account. |
| `budget_name` | Name of your budget. For the account budget, the name is `ACCOUNT_ROOT_BUDGET`. |
| `type` | The type of the notification (for example, `BUDGET_LIMIT_WARNING`). |
| `limit` | The spending limit that you set for the budget. |
| `spending` | The amount of credit usage for this month. |
| `spending_percent` | The percentage of the spending limit that has already been spent (`spending / limit`). |
| `spending_trend_percent` | Expected percentage of the spending limit to be spent by the end of the month (`spending_percent / time_percent * 100`). |
| `time_percent` | Percentage of time that has passed for the month (for example, `50.00` if the month is half over). |

## Checking the history of notifications for a budget

To view the history of notifications for a budget, call the [NOTIFICATION_HISTORY](../../sql-reference/functions/notification_history.md) function and
filter on the integration name. For example:

```sqlexample
SELECT * FROM TABLE(
  INFORMATION_SCHEMA.NOTIFICATION_HISTORY(
    INTEGRATION_NAME=>'budgets_notification_integration'
  )
);
```

The `message_source` column contains `BUDGET` for rows representing budget notifications.

## Disabling notifications for a budget

To disable notifications for a budget, call the
[SET_NOTIFICATION_MUTE_FLAG](../../sql-reference/classes/budget/methods/set_notification_mute_flag.md) method, and pass in TRUE as
an argument. For example:

```sqlexample
CALL SNOWFLAKE.LOCAL.ACCOUNT_ROOT_BUDGET!SET_NOTIFICATION_MUTE_FLAG(TRUE);
```

## Removing a notification integration from a budget

To remove a notification integration from a budget, call the
[<budget_name>!REMOVE_NOTIFICATION_INTEGRATION](../../sql-reference/classes/budget/methods/remove_notification_integration.md) method, passing in the name of the integration.
For example:

```sqlexample
CALL my_budget!REMOVE_NOTIFICATION_INTEGRATION(
  'budgets_notification_integration',
);
```
