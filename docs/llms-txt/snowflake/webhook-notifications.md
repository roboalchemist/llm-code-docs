# Source: https://docs.snowflake.com/en/user-guide/notifications/webhook-notifications.md

# Sending webhook notifications

You can integrate Snowflake notifications with the following external systems by using the webhooks that these systems provide:

* [Slack](https://api.slack.com/messaging/webhooks)
* [Microsoft Teams](https://support.microsoft.com/en-us/office/create-incoming-webhooks-with-workflows-for-microsoft-teams-8ae491c7-0394-4861-ba59-055e33f75498)
* [PagerDuty](https://developer.pagerduty.com/docs/ZG9jOjExMDI5NTgw-events-api-v2-overview)

> **Note:**
>
> Snowflake does not send webhook notifications to external systems other than the ones listed above.

To send a notification to one of these systems:

1. Create the secret for the webhook URL for the external system.
2. Create the webhook notification integration for the external system.
3. Send the notification to the external system, using the webhook notification integration.

The next sections provide more details about how to set up and send notifications to these external systems.

## Creating a secret for a webhook URL

Most webhooks require a secret or integration key in the incoming HTTP request. For example:

* When you [create an incoming webhook in Slack](https://api.slack.com/messaging/webhooks#create_a_webhook), the URL for the webhook includes a secret:

  ```none
  https://hooks.slack.com/services/<secret>
  ```

* When you [create an incoming webhook with Workflows for Microsoft Teams](https://support.microsoft.com/en-us/office/create-incoming-webhooks-with-workflows-for-microsoft-teams-8ae491c7-0394-4861-ba59-055e33f75498), the URL for the webhook includes a secret.

  Up until November 30, 2025, Microsoft Teams supports URLs in the following format:

  ```none
  https://<hostname>.<region>.logic.azure.com:443/workflows/<secret>
  ```

  [From November 30, 2025 onward](https://learn.microsoft.com/en-us/troubleshoot/power-platform/power-automate/flow-run-issues/triggers-troubleshoot?tabs=new-designer#changes-to-http-or-teams-webhook-trigger-flows),
  Microsoft Teams supports URLs in the following format:

  ```none
  https://default<hostname>.environment.api.powerplatform.com/powerautomate/automations/direct/workflows/<secret>/triggers/manual/paths/invoke
  ```

* When you [set up an integration for your PagerDuty service](https://support.pagerduty.com/docs/services-and-integrations), the integration provides an integration key that you must
  include in webhook requests:

  ```json
  {
     "routing_key" : "<integration_key>",
     /* ... */
  ```

For this secret or integration key, we recommend creating a secret object of the generic string type. This secret object is used
in the following ways:

* When you create a webhook notification integration, you specify this secret object in the
  [CREATE NOTIFICATION INTEGRATION](../../sql-reference/sql/create-notification-integration-webhooks.md) statement.
* When you send a notification, the secret object is used to construct the HTTP request for the webhook.

Note the following:

* When you create the webhook notification integration, you must use a role that has the USAGE privilege on this secret.
* When you send a notification to this webhook, you must use a role that has the READ privilege on this secret as well as the
  USAGE privileges on the database and schema containing the secret.

To create this object, use the [CREATE SECRET](../../sql-reference/sql/create-secret.md) command, and specify TYPE=GENERIC_STRING. You must use a
role that has the CREATE SECRET privilege on the schema where you plan to create that object.

The next sections provide examples of creating the secret object.

* Example 1: Creating a secret for a Slack webhook
* Example 2: Creating a secret for a Workflows for Microsoft Teams webhook
* Example 3: Creating a secret for a PagerDuty webhook

### Example 1: Creating a secret for a Slack webhook

Suppose that you want to send notifications to a [Slack webhook](https://api.slack.com/messaging/webhooks#create_a_webhook) with the URL:

```none
https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX
```

In this example, the webhook URL contains the secret `T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX`.

Execute the following statement to create a secret object for this secret:

```sqlexample
CREATE OR REPLACE SECRET my_slack_webhook_secret
  TYPE = GENERIC_STRING
  SECRET_STRING = 'T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX';
```

### Example 2: Creating a secret for a Workflows for Microsoft Teams webhook

Suppose that you want to send notifications to a [Workflows for Microsoft Teams webhook](https://support.microsoft.com/en-us/office/create-incoming-webhooks-with-workflows-for-microsoft-teams-8ae491c7-0394-4861-ba59-055e33f75498) with one of the following URLs:

* Up until November 30, 2025:

  ```none
  https://prod-114.westeurope.logic.azure.com:443/workflows/xxxxxxxx
  ```

* [From November 30, 2025 onward](https://learn.microsoft.com/en-us/troubleshoot/power-platform/power-automate/flow-run-issues/triggers-troubleshoot?tabs=new-designer#changes-to-http-or-teams-webhook-trigger-flows):

  ```none
  https://defaultcac999b557e445acf1fefefe4ae5ff4.34.environment.api.powerplatform.com/powerautomate/automations/direct/workflows/xxxxxxxx/triggers/manual/paths/invoke
  ```

For information about the Microsoft API data format, see <https://adaptivecards.io/> .

In this example, the webhook URL contains the secret `xxxxxxxx`.

Execute the following statement to create a secret object for this secret:

```sqlexample
CREATE OR REPLACE SECRET my_teams_webhook_secret
  TYPE = GENERIC_STRING
  SECRET_STRING = 'xxxxxxxx';
```

### Example 3: Creating a secret for a PagerDuty webhook

Suppose that you want to send notifications to a [PagerDuty webhook](https://support.pagerduty.com/docs/services-and-integrations) and that your integration key (the value that you must
include in the `routing_key` field in requests) is:

```none
xxxxxxxx
```

Execute the following statement to create a secret object for this secret:

```sqlexample
CREATE OR REPLACE SECRET my_pagerduty_webhook_secret
  TYPE = GENERIC_STRING
  SECRET_STRING = 'xxxxxxxx';
```

## Creating a webhook notification integration

To create a notification integration of the webhook type, use the
[CREATE NOTIFICATION INTEGRATION](../../sql-reference/sql/create-notification-integration-webhooks.md) command.

When executing this command, set the following properties to set up the HTTP request that should be sent for the notification.

* Set TYPE to WEBHOOK.
* If you created a secret object for a secret to be included in the URL, HTTP request
  body, or header, set WEBHOOK_SECRET to the name of that secret object.
* Set WEBHOOK_URL to the URL for the webhook.

  If the webhook URL includes a secret and you created a secret object for this secret, replace the secret in the URL with
  SNOWFLAKE_WEBHOOK_SECRET.
* If the body of the message for the webhook needs to be in a specific format for this external system (for example, if all
  messages sent to this system need to use the same format), set WEBHOOK_BODY_TEMPLATE to a template for the message. In this
  template:

  * Use the SNOWFLAKE_WEBHOOK_SECRET placeholder where the secret should appear in the body of the message.
  * Use the SNOWFLAKE_WEBHOOK_MESSAGE placeholder where the notification message should appear.

  When you call [SYSTEM$SEND_SNOWFLAKE_NOTIFICATION](../../sql-reference/stored-procedures/system_send_snowflake_notification.md) and pass in a message, the stored
  procedure uses the template to construct the body of the webhook request. The stored procedure replaces the
  SNOWFLAKE_WEBHOOK_MESSAGE placeholder with the message that you pass in.
* If the HTTP request to the webhook must include specific HTTP headers, set WEBHOOK_HEADERS to the list of the header names and
  values.

  Use the SNOWFLAKE_WEBHOOK_SECRET placeholder where the secret should appear in the value of a header.

The next sections provide examples of creating webhook notification integrations for different types of external systems.

* Example 1: Creating a notification integration for a Slack webhook
* Example 2: Creating a notification integration for a Workflows for Microsoft Teams webhook
* Example 3: Creating a notification integration for a PagerDuty webhook

### Example 1: Creating a notification integration for a Slack webhook

Suppose that you want to send notifications to a Slack webhook with the URL:

```none
https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX
```

Suppose that you created a secret object named `my_slack_webhook_secret`
for the secret `T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX` that appears in the URL.

Execute the following statement to create a notification integration for this webhook:

```sqlexample
CREATE OR REPLACE NOTIFICATION INTEGRATION my_slack_webhook_int
  TYPE=WEBHOOK
  ENABLED=TRUE
  WEBHOOK_URL='https://hooks.slack.com/services/SNOWFLAKE_WEBHOOK_SECRET'
  WEBHOOK_SECRET=my_secrets_db.my_secrets_schema.my_slack_webhook_secret
  WEBHOOK_BODY_TEMPLATE='{"text": "SNOWFLAKE_WEBHOOK_MESSAGE"}'
  WEBHOOK_HEADERS=('Content-Type'='application/json');
```

### Example 2: Creating a notification integration for a Workflows for Microsoft Teams webhook

Suppose that you want to send notifications to a Workflows for Microsoft Teams webhook with one of the following URLs:

* Up until November 30, 2025:

  ```none
  https://prod-114.westeurope.logic.azure.com:443/workflows/xxxxxxxx
  ```

* [From November 30, 2025 onward](https://learn.microsoft.com/en-us/troubleshoot/power-platform/power-automate/flow-run-issues/triggers-troubleshoot?tabs=new-designer#changes-to-http-or-teams-webhook-trigger-flows):

  ```none
  https://defaultcac999b557e445acf1fefefe4ae5ff4.34.environment.api.powerplatform.com/powerautomate/automations/direct/workflows/xxxxxxxx/triggers/manual/paths/invoke
  ```

Suppose that you created a secret object named `my_teams_webhook_secret`
for the secret `xxxxxxxx` that appears in the URL.
(For information about the Microsoft API data format, see <https://adaptivecards.io/> .)

Execute one of the following statements to create a notification integration for this webhook:

* For the `logic.azure.com` URL:

  ```sqlexample
  CREATE OR REPLACE NOTIFICATION INTEGRATION my_teams_webhook_int
    TYPE=WEBHOOK
    ENABLED=TRUE
    WEBHOOK_URL='https://prod-114.westeurope.logic.azure.com/workflows/SNOWFLAKE_WEBHOOK_SECRET'
    WEBHOOK_SECRET=my_secrets_db.my_secrets_schema.my_teams_webhook_secret
    WEBHOOK_BODY_TEMPLATE='{"text": "SNOWFLAKE_WEBHOOK_MESSAGE"}'
    WEBHOOK_HEADERS=('Content-Type'='application/json');
  ```

* For the `environment.api.powerplatform.com` URL:

  ```sqlexample
  CREATE OR REPLACE NOTIFICATION INTEGRATION my_teams_webhook_int
    TYPE=WEBHOOK
    ENABLED=TRUE
    WEBHOOK_URL='https://defaultcac999b557e445acf1fefefe4ae5ff4.34.environment.api.powerplatform.com/powerautomate/automations/direct/workflows/xxxxxxxx/triggers/manual/paths/invoke'
    WEBHOOK_SECRET=my_secrets_db.my_secrets_schema.my_teams_webhook_secret
    WEBHOOK_BODY_TEMPLATE='{"text": "SNOWFLAKE_WEBHOOK_MESSAGE"}'
    WEBHOOK_HEADERS=('Content-Type'='application/json');
  ```

> **Note:**
>
> You must omit the port number (`:443`) from the URL in the WEBHOOK_URL parameter.

### Example 3: Creating a notification integration for a PagerDuty webhook

Suppose that you want to send notifications to a PagerDuty webhook with the URL:

```none
https://events.pagerduty.com/v2/enqueue
```

Suppose that you created a secret object named `my_pagerduty_webhook_secret`
for the integration key `xxxxxx` that should be included in the `routing_key` field in the body of the message.

Execute the following statement to create a notification integration for this webhook:

```sqlexample
CREATE OR REPLACE NOTIFICATION INTEGRATION my_pagerduty_webhook_int
  TYPE=WEBHOOK
  ENABLED=TRUE
  WEBHOOK_URL='https://events.pagerduty.com/v2/enqueue'
  WEBHOOK_SECRET=my_secrets_db.my_secrets_schema.my_pagerduty_webhook_secret
  WEBHOOK_BODY_TEMPLATE='{
    "routing_key": "SNOWFLAKE_WEBHOOK_SECRET",
    "event_action": "trigger",
    "payload": {
      "summary": "SNOWFLAKE_WEBHOOK_MESSAGE",
      "source": "Snowflake monitoring",
      "severity": "INFO"
    }
  }'
  WEBHOOK_HEADERS=('Content-Type'='application/json');
```

## Sending a notification to a webhook

To send a notification to a webhook:

1. Pass the [SANITIZE_WEBHOOK_CONTENT](../../sql-reference/functions/sanitize_webhook_content.md) function to remove any placeholders (like
   SNOWFLAKE_WEBHOOK_SECRET) from the message.
2. Call the [SYSTEM$SEND_SNOWFLAKE_NOTIFICATION](../../sql-reference/stored-procedures/system_send_snowflake_notification.md) stored
   procedure, passing in the sanitized message and specifying the name of the webhook notification integration to use.

For example, the following statement sends a JSON message to a Slack webhook, using the notification integration that you
created earlier:

```sqlexample
CALL SYSTEM$SEND_SNOWFLAKE_NOTIFICATION(
  SNOWFLAKE.NOTIFICATION.TEXT_PLAIN(
    SNOWFLAKE.NOTIFICATION.SANITIZE_WEBHOOK_CONTENT('my message')
  ),
  SNOWFLAKE.NOTIFICATION.INTEGRATION('my_slack_webhook_int')
);
```

In this example, the statement passes in a message in plain text (`my message`). When constructing the body of the webhook
request from the template specified by the WEBHOOK_BODY_TEMPLATE property of the notification integration,
SYSTEM$SEND_SNOWFLAKE_NOTIFICATION replaces the SNOWFLAKE_WEBHOOK_MESSAGE placeholder with the message that you pass in.

For example, suppose that you specified the following template for the body of the request:

```sqlexample
CREATE OR REPLACE NOTIFICATION INTEGRATION my_slack_webhook_int
  ...
  WEBHOOK_BODY_TEMPLATE='{"text": "SNOWFLAKE_WEBHOOK_MESSAGE"}'
  ...
```

SYSTEM$SEND_SNOWFLAKE_NOTIFICATION constructs a request with the following body:

```json
{"text": "my message"}
```
