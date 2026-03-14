# Source: https://ably.com/docs/platform/integrations/webhooks/gcp-function.md

# Google Function integration

[Google Function](https://cloud.google.com/functions) integrations enable you to trigger event-driven serverless compute functions when an event occurs in Ably.

## Create a Google Function integration

To create a Google Function integration in your [dashboard:](https://ably.com/dashboard/any)

1. Login and select the application you wish to integrate with a Google Function.
2. Click the **Integrations** tab.
3. Click the **New Integration Rule** button.
4. Choose **Webhook**.
5. Choose **Google Functions**.
6. Configure the Google Function [settings](#settings).
7. Click **Create**.

You can also create a Google Function integration using the [Control API](https://ably.com/docs/platform/account/control-api.md).

### Settings

The following settings are available when creating a Google Function integration:

| Setting | Description |
| ------- | ----------- |
| Region | The region in which your Google Function is hosted. |
| Project ID | The ID of your Google Cloud Project. |
| Function | The name of your Google Function. |
| Headers | Allows the inclusion of additional information in key-value format. |
| Request Mode | Choose between **Single Request** or **Batch Request**. |
| [Event types](https://ably.com/docs/platform/integrations/webhooks.md#sources) | Specifies the event types being sent to your Google Function. |
| [Channel filter](https://ably.com/docs/platform/integrations/webhooks.md#filter) | Filters the source channels based on a regular expression. |
| Encoding | Specifies the encoding format of messages. Either JSON or MsgPack. |
| [Enveloped](https://ably.com/docs/platform/integrations/webhooks.md#enveloped) | Checkbox to set whether messages should be enveloped or not. Enveloped is the default. Only available when `Request Mode` is set to `Single`. |
| Sign with key | Payloads will be signed with an API key so they can be validated by your servers. Only available when `Request Mode` is set to `Batched`. |

## Related Topics

- [Overview](https://ably.com/docs/platform/integrations/webhooks.md): A guide on webhook payloads, including batched, enveloped, and non-enveloped event payloads, with decoding examples and sources.
- [Generic HTTP webhooks](https://ably.com/docs/platform/integrations/webhooks/generic.md): Configure generic HTTP webhooks to trigger HTTP endpoints and notify external services when events occur in Ably.
- [Lambda Functions](https://ably.com/docs/platform/integrations/webhooks/lambda.md): Trigger AWS Lambda functions based on message, channel lifecycle, channel occupancy, and presence events.
- [Azure Functions](https://ably.com/docs/platform/integrations/webhooks/azure.md): Trigger Microsoft Azure functions based on message, channel lifecycle, channel occupancy, and presence events.
- [Zapier](https://ably.com/docs/platform/integrations/webhooks/zapier.md): Trigger Zapier based on message, channel lifecycle, channel occupancy, and presence events.
- [Cloudflare Workers](https://ably.com/docs/platform/integrations/webhooks/cloudflare.md): Trigger Cloudflare Workers based on message, channel lifecycle, channel occupancy, and presence events.
- [IFTTT](https://ably.com/docs/platform/integrations/webhooks/ifttt.md): Trigger IFTTT based on message, channel lifecycle, channel occupancy, and presence events.

## Documentation Index

To discover additional Ably documentation:

1. Fetch [llms.txt](https://ably.com/llms.txt) for the canonical list of available pages.
2. Identify relevant URLs from that index.
3. Fetch target pages as needed.

Avoid using assumed or outdated documentation paths.
