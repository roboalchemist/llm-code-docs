# Source: https://www.apollographql.com/docs/graphos/platform/insights/notifications/performance-alerts.md

# Performance Alerts from GraphOS

GraphOS can alert your team's Slack workspace or PagerDuty when a metric, like error rate, for a GraphQL operation goes over a set threshold.
These alerts are useful for detecting anomalies, especially following a release.

## Supported metrics

You can configure performance alerts for any of the following metrics:

* **Request rate:** requests per minute
* **Request duration:** p50/p95/p99 service time
* **Error rate:** errors per minute
* **Error percentage:** the number of requests with errors divided by the total requests

Each performance alert you define can apply to either a specific operation or any operation.
If you define an alert that applies to a specific operation, the "any operation" alerts for the same metric no longer apply to that operation.
That is, the more specific alert takes precedence.

## Setup

If you want to receive notifications via both Slack and PagerDuty, repeat these setup steps for both.

1. Go to your graph's Settings page in [GraphOS Studio](https://studio.apollographql.com/?referrer=docs-content).
2. Select the **Reporting** tab.
3. Find the **Performance Alerts** card and click **Add a new alert**.
4. Configure the alert's **Operation Name**, **Trigger**, and **Trigger Value** to suit your needs.
5. Select a **Channel** to send alerts to. You can select **New Channel** from the dropdown if you haven't yet configured the Slack channel or PagerDuty instance you want to use.
6. Click **Create**.

## Configure a new channel

### Slack

To set up Slack notifications, you must:

1. Create an incoming webhook in Slack.
2. Provide that webhook's URL to GraphOS Studio.

#### 1. Create an incoming Slack hook

To create an incoming Slack hook:

1. From the [Incoming Hooks](https://slack.com/apps/A0F7XDUAZ-incoming-webhooks) page of the Slack App Directory, sign in and click **Add to Slack**.
2. Select the Slack channel that should receive notifications. Then, click **Add Incoming WebHooks integration**.
3. Copy the **Webhook URL** to use in the next step. It should have a format like `https://hooks.slack.com/services/...`.

You can repeat this process to create webhook URLs for different Slack channels.

#### 2. Provide the Slack hook to Studio

1. In [GraphOS Studio](https://studio.apollographql.com/?referrer=docs-content), specify a name for this notification channel in the **Channel Name** field.

   * This name must be unique among your graph's notification channels.
   * This name doesn't have to match the name of the Slack channel, but it's recommended for simplicity.

2. In the **Slack Webhook URL** field, paste the webhook URL you obtained in [Create an incoming Slack hook](https://www.apollographql.com/docs/graphos/platform/insights/notifications/performance-alerts.md#1-create-an-incoming-slack-hook).

3. Click **Next**.

4. After you finish setup, check that your Slack channel gets a confirmation from Studio.

To configure multiple Slack channels, repeat this process. Use a different webhook URL for each channel.

### PagerDuty

To set up PagerDuty alerts, you must:

1. Create a PagerDuty integration key.
2. Provide that integration key to GraphOS Studio.

#### 1. Create a PagerDuty integration key

Generate an [integration key](https://support.pagerduty.com/docs/generating-api-keys#events-api-keys) for the service that should receive alerts in PagerDuty.
You can select an [existing service](https://www.apollographql.com/docs/graphos/platform/insights/notifications/performance-alerts.md#existing-services) that corresponds to your GraphQL API or [**Add New Service**](https://www.apollographql.com/docs/graphos/platform/insights/notifications/performance-alerts.md#adding-a-service).

##### Existing services

1. In PagerDuty, go to your existing service's **Integrations** tab and click **new integration**.
2. Enter an **Integration Name**, for example, `GraphOS Alerts`.
3. Under **Integration type**, choose **Use our API directly** and **Events API v2**.
4. Click **Add Integration**.
5. From the Integrations tab, copy the generated integration key from the table for use in the [next step](https://www.apollographql.com/docs/graphos/platform/insights/notifications/performance-alerts.md#2-provide-the-integration-key-to-studio).

##### Adding a service

1. In PagerDuty, under **Integration Settings**, choose **Use our API directly** and use **Events API v2**.
2. Enter an **Integration Name**, for example, `GraphOS Alerts`, and complete the add service flow.
3. From the **Integrations** tab, copy the generated integration key from the table for use in the [next step](https://www.apollographql.com/docs/graphos/platform/insights/notifications/performance-alerts.md#2-provide-the-integration-key-to-studio).

#### 2. Provide the integration key to Studio

1. In [GraphOS Studio](https://studio.apollographql.com/?referrer=docs-content), specify a name for this notification channel in the **Channel Name** field.

   * This name must be unique among your graph's notification channels.
   * This name does not have to match the name of the PagerDuty service, but it's recommended for simplicity.

2. In the **PagerDuty Integration Key** field, paste the integration key you obtained in [Create a PagerDuty integration key](https://www.apollographql.com/docs/graphos/platform/insights/notifications/performance-alerts.md#1-create-a-pagerduty-integration-key).

3. Click **Done**.

## Threshold window

Thresholds are measured against a rolling five-minute window.
For example, let's say you configure an alert to trigger when an operation's error rate exceeds 5%.
If 6 out of 100 executions of that operation result in an error during a five-minute period, the alert will trigger with an error rate of 6%.
When the error rate falls back below 5%, your alert will resolve.
