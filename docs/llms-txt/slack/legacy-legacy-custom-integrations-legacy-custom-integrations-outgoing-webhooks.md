Source: https://docs.slack.dev/legacy/legacy-custom-integrations/legacy-custom-integrations-outgoing-webhooks

# legacy custom integrations: outgoing webhooks

Outgoing webhooks are a legacy method of sending notifications to an app about two specific activities:

1. A message was posted in a particular public Slack channel.
2. A message was posted in any public Slack channel containing specific trigger words.

Because we strongly recommend you do not use legacy custom integrations anymore, you should instead use the [Events API](/apis/events-api/) with Slack apps. Our [guide to the Events API](/apis/events-api/) will walk you through the process of enabling this functionality in a Slack app.

If you were using outgoing webhooks to provide a bot-like behavior with your legacy integration, you might be interested in reading our [Handling user interaction in your Slack apps guide](/interactivity/handling-user-interaction).

* * *

## Migrating from legacy integrations {#migrating-from-legacy}

If you previously created any outgoing Webhooks using legacy integrations, you should switch to a Slack app and replicate the functionality using the [Events API](/apis/events-api/).

The [Events API](/apis/events-api/) can be used to replace this by [subscribing](/apis/events-api/#subscriptions) to the [`message.channels`](/reference/events/message.channels) event type. This will push a data payload to an app every time a message is posted to a public channel.

When an app [receives that data payload](/apis/events-api/#receiving_events), it'll be able to see both the source `channel` and the `text` of the posted message. Using `channel` will help replicate the first outgoing Webhook feature, and looking for the trigger words in the `text` string will replicate the second.

Even better, while Outgoing Webhooks only worked for public channels, the [Events API](/apis/events-api/) can be used with [private channels](/reference/events/message.groups), [direct message conversations](/reference/events/message.im), or [multi-party direct message conversations](/reference/events/message.mpim). There are also [dozens of other event types](/apis/events-api/#event_types) available for subscription, and for your app to react to. Read the [Events API overview](/apis/events-api/) for a better idea of all the things you can use it for.

* * *

## Legacy information {#legacy-info}

Though we recommend that all legacy custom integrations should [migrate to Slack apps](/legacy/legacy-custom-integrations/legacy-custom-integrations-migration), we also understand that some will still need to maintain older integrations. This section contains any information about using outgoing Webhooks that is specific to the legacy implementation.

#### Legacy management {#legacy-bot-manage}

If you need to configure your legacy integrations, you can access the [Integrations management pages here](https://www.slack.com/apps/manage/custom-integrations).

#### Channel and/or Trigger {#channel-trigger}

If an outgoing webhook is not configured to respond when a message is posted in a specific channel, then the trigger word(s) are required -- otherwise, the trigger word(s) are optional.

If both are specified, then the message must match both conditions.

#### POST Data {#post-data}

When a chat message is received that matches the conditions, a POST will be sent to all of the URLs defined like so:

```text
token=XXXXXXXXXXXXXXXXXXteam_id=T0001team_domain=examplechannel_id=C2147483705channel_name=testthread_ts=1504640714.003543timestamp=1504640775.000005user_id=U2147483697user_name=Stevetext=googlebot: What is the air-speed velocity of an unladen swallow?trigger_word=googlebot:
```text

Please note that the content of [message attachments](/messaging/formatting-message-text) will not be included in the outgoing POST data.

##### Responding {#responding}

If the handler wishes to post a response back into the channel, the following JSON should be returned as the body of the response:

```json
{    "text": "African or European?"}
```text

Empty bodies or bodies with an empty `text` property will be ignored. Non-200 responses will be retried a reasonable number of times.

Responses will be posted using the bot name and icon configured in the integration. However, if you would like to change the name on a per-response basis, include the `username` parameter in your response.

#### Rate Limits {#rate-limits}

Outgoing webhooks sent by a legacy integration are limited to no more than one message per second, with bursts allowed over short periods to accommodate periods of high activity.

If your legacy integration goes over this limit, outgoing webhooks for subsequent messages will not be sent until the rate has gone below the one webhook per second limit.

This limit exists to prevent us sending your servers more events than you or we can handle. The [Events API](/apis/events-api/#rate_limiting), which can be used with Slack apps [as above](#migrating-from-legacy) has [different rate limits](/apis/events-api/#rate_limiting) which may be more suitable for your use case.
