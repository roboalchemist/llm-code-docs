# Source: https://www.courier.com/docs/external-integrations/direct-message/stream-chat.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Stream Chat

> Send notifications via Stream Chat using Courier by specifying channelType and channelId or a messageId in the recipient profile, and optionally overriding message body, API credentials, or endpoint settings.

## Setup

You will need a [Stream Chat](https://getstream.io/chat/) account with a project configured. In Courier, navigate to the [Stream Chat Integration](https://app.courier.com/integrations/catalog/stream-chat) page, enter your API key, API secret, and sender ID, then click "Save."

## Profile Requirements

To deliver a message to a recipient over Stream Chat, Courier must be provided a `channelType` and `channelId`, or a `messageId` (for updating an existing message). Include these in the recipient profile as `streamChat`.

```json  theme={null}
{
  "message": {
    "to": {
      "streamChat": {
        "channelType": "messaging",
        "channelId": "my-channel-id"
      }
    }
  }
}
```

```json  theme={null}
{
  "message": {
    "to": {
      "streamChat": {
        "messageId": "my-message-id"
      }
    }
  }
}
```

## Overrides

You can override the request body, API credentials, and endpoint URL that Courier sends to Stream Chat.

* Override any of the fields supported by Stream Chat's `POST /channels/{type}/{id}/message` API endpoint.
  [See all send request body fields here.](https://getstream.io/chat/docs/rest/#/product%3Achat/SendMessage)
* Override `apiKey`, `apiSecret`, and `senderId` via the config object.
* Override `baseUrl` (defaults to `https://chat-us-east-1.stream-io-api.com`).

```json  theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {
      "streamChat": {
        "channelType": "messaging",
        "channelId": "my-channel-id"
      }
    },
    "data": {
      "name": "Foo Bar"
    },
    "providers": {
      "stream-chat": {
        "override": {
          "body": {
            "skip_push": true
          },
          "config": {
            "baseUrl": "https://custom-stream-endpoint.example.com",
            "apiKey": "RUNTIME_API_KEY",
            "apiSecret": "RUNTIME_API_SECRET",
            "senderId": "RUNTIME_SENDER_ID"
          }
        }
      }
    }
  }
}
```
