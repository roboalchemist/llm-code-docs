# Source: https://www.courier.com/docs/external-integrations/push/pusher.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Pusher

> Send real-time push notifications via Pusher by targeting a recipient's Pusher channel and customizing payloads through Courier templates or jsonnet editor.

## Setup

You will need a [Pusher](https://pusher.com/) account with a Channels app configured. In Courier, navigate to the [Pusher Integration](https://app.courier.com/integrations/catalog/pusher) page, enter your app ID, key, secret, and cluster, then click "Save."

## Profile Requirements

To deliver a message to a recipient via Pusher, Courier must be provided a target object that contains the recipient's Pusher channel. This value should be included in the recipient profile as `pusher`.

```json  theme={null}
{
  "message": {
    "to": {
      "pusher": {
        "channel": "my-channel"
      }
    }
  }
}
```

## Template Requirements

Pusher can be used in Courier in two ways. One is via the "Push" channel; the other is via a direct Pusher channel. When in the direct Pusher channel, a jsonnet editor will be provided for you to customize your payload. When Pusher is integrated via the push channel, a rich editor will be shown.

## Example Event

```json  theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {
      "pusher": {
        "channel": "my-channel"
      }
    },
    "data": {
      "name": "Katherine Pryde"
    }
  }
}
```

<Note>
  Pusher uses the Pusher SDK directly and does not support the standard `providers.<key>.override` pattern used by other push providers.
</Note>

## Tracking Events

Courier will include tracking URL information in the `data` attribute on the incoming message payload.

See [Courier push notification tracking](/external-integrations/push/intro-to-push#tracking).
