# Source: https://ably.com/docs/platform/integrations/webhooks/generic.md

# Generic HTTP webhooks

Generic HTTP webhooks enable you to trigger HTTP endpoints and notify external services when events occur in Ably. Events include when messages are published, presence events occur, changes in channel occupancy, and when channels are created or discarded. Data can be delivered individually or in batches to any HTTP endpoint.

## Create a generic HTTP webhook integration

To create a generic HTTP webhook integration in your [dashboard](https://ably.com/dashboard/any):

1. Login and select the application you wish to integrate with an HTTP endpoint.
2. Click the **Integrations** tab.
3. Click the **New Integration Rule** button.
4. Choose **Webhook**.
5. Choose **Webhook** (again).
6. Configure the webhook [settings](#settings).
7. Click **Create**.

You can also create a generic HTTP webhook integration using the [Control API](https://ably.com/docs/platform/account/control-api.md).

## Settings

The following settings are available when creating a generic HTTP webhook integration:

| Setting | Description |
|---------|-------------|
| URL | The HTTP/HTTPS endpoint URL where webhook requests will be sent. Ably strongly recommends using HTTPS for security. |
| Headers | Optional HTTP headers to include with each request. Use the format `key:value`, for example, `X-Custom-Header:my-value`. Each header should be on a new line. |
| Request Mode | Choose between **Single request** (sends each event individually) or **Batch request** (groups multiple events into a single request). |
| Event types | Choose which event types trigger the webhook: `channel.message`, `channel.presence`, `channel.lifecycle`, or `channel.occupancy`. |
| [Channel filter](https://ably.com/docs/platform/integrations/webhooks.md#filter) | Filters the source channels based on a regular expression. |
| Encoding | Specifies the encoding format of messages. Either JSON or MsgPack. |
| Sign with key | Choose whether to sign webhook requests with your API key for security. |
| [Enveloped](https://ably.com/docs/platform/integrations/webhooks.md#enveloped) | When enabled (default), messages are wrapped in additional metadata. When disabled, only the raw message data is sent. |

## Related Topics

- [Overview](https://ably.com/docs/platform/integrations/webhooks.md): A guide on webhook payloads, including batched, enveloped, and non-enveloped event payloads, with decoding examples and sources.
- [Lambda Functions](https://ably.com/docs/platform/integrations/webhooks/lambda.md): Trigger AWS Lambda functions based on message, channel lifecycle, channel occupancy, and presence events.
- [Azure Functions](https://ably.com/docs/platform/integrations/webhooks/azure.md): Trigger Microsoft Azure functions based on message, channel lifecycle, channel occupancy, and presence events.
- [Google Functions](https://ably.com/docs/platform/integrations/webhooks/gcp-function.md): Trigger Google Functions based on message, channel lifecycle, channel occupancy, and presence events.
- [Zapier](https://ably.com/docs/platform/integrations/webhooks/zapier.md): Trigger Zapier based on message, channel lifecycle, channel occupancy, and presence events.
- [Cloudflare Workers](https://ably.com/docs/platform/integrations/webhooks/cloudflare.md): Trigger Cloudflare Workers based on message, channel lifecycle, channel occupancy, and presence events.
- [IFTTT](https://ably.com/docs/platform/integrations/webhooks/ifttt.md): Trigger IFTTT based on message, channel lifecycle, channel occupancy, and presence events.

## Documentation Index

To discover additional Ably documentation:

1. Fetch [llms.txt](https://ably.com/llms.txt) for the canonical list of available pages.
2. Identify relevant URLs from that index.
3. Fetch target pages as needed.

Avoid using assumed or outdated documentation paths.
