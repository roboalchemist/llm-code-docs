# Source: https://www.apollographql.com/docs/graphos/platform/insights/notifications/schema-changes.md

# Schema Change Notifications

Configure GraphOS to notify your team whenever your graph's registered schema changes.
You can receive notifications via Slack, custom webhook, or both.

## Setup

If you want to receive notifications via both Slack and webhook, repeat these setup steps for both.

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

2. In the **Slack Webhook URL** field, paste the webhook URL you obtained in [Create an incoming Slack hook](https://www.apollographql.com/docs/graphos/platform/insights/notifications/schema-changes.md#1-create-an-incoming-slack-hook).

3. Click **Next**.

4. After you finish setup, check that your Slack channel gets a confirmation from Studio.

To configure multiple Slack channels, repeat this process. Use a different webhook URL for each channel.

### Webhook

Custom webhooks require you to set up an HTTPS endpoint accessible via
the public internet. GraphOS sends webhook notifications to this
endpoint as `POST` requests. Notification details are
provided as JSON in the request body, as described in the next section.

1. Specify a name for this notification channel in the **Channel Name** field. This name must be unique among
   all your graph's notification channels, including Slack channels.

2. In the **Webhook URL** input, provide the URL of your HTTP(S) endpoint.

3. Click **Next** and complete any remaining steps in the dialog.

#### Webhook format

Custom webhook notification details are provided as a JSON object in the request body.

The JSON object conforms to the structure of the `ResponseShape` interface:

```javascript
interface Change {
  description: string;
}

interface ResponseShape {
  eventType: 'SCHEMA_PUBLISH'
  eventID: string;
  changes: Change[];
  schemaURL: string;
  schemaURLExpiresAt: string;
  graphID: string;
  variantID: string;
  timestamp: string;
}
```

#### Field descriptions

Field
Description

##### `eventType`

The schema change event; currently, always `SCHEMA_PUBLISH`

##### `eventId`

A unique event ID

##### `changes`

The set of schema changes that occurred

##### `schemaURL`

A short-lived (24-hour) URL that enables you to fetch the published
schema without authenticating (such as with an API key). The URL expires
at the time indicated by `schemaURLExpiresAt`.

##### `schemaURLExpiresAt`

An ISO 8601 Date string indicating when the `schemaURL` expires

##### `graphID`

A unique graph ID

##### `variantID`

An unique ID in the graph ref format, for example, `graphID@variantName`

##### `timestamp`

An ISO 8601 Date string indicating when the event occurred
