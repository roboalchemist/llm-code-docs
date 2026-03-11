# Source: https://www.courier.com/docs/external-integrations/direct-message/chat.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Chat API

> Send notifications via the Chat API service using Courier, with support for phone number or chat ID targeting, and provider overrides for credentials and message body.

<Warning>
  The Chat API service (`chat-api.com`) may no longer be actively maintained. Verify the service status before integrating.
</Warning>

## Setup

You will need a [Chat API](https://chat-api.com/) account with an instance configured. In Courier, navigate to the [Chat API Integration](https://app.courier.com/integrations/catalog/chat-api) page, enter your instance ID and token, then click "Save."

## Profile Requirements

To deliver a message to a recipient over Chat API, Courier must be provided a phone number or chat ID. This value should be included in the recipient profile as `chat_api`.

```json  theme={null}
{
  "message": {
    "to": {
      "chat_api": {
        "phone_number": "12345678"
      }
    }
  }
}
```

```json  theme={null}
{
  "message": {
    "to": {
      "chat_id": "recipient-chat-id"
    }
  }
}
```

## Template

In the notification's integration settings, you can provide a quoted message ID and mentioned phone numbers.

## Overrides

You can use a provider override to change the request body or swap credentials at send time.

### Body Overrides

Override any of the fields supported by Chat API's `/sendMessage` endpoint.

### Config Overrides

You can swap the instance ID, token, or API URL at send time:

```json  theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {
      "chat_api": {
        "phone_number": "12345678"
      }
    },
    "data": {
      "name": "Katherine Pryde"
    },
    "providers": {
      "chat-api": {
        "override": {
          "config": {
            "instanceId": "RUNTIME_INSTANCE_ID",
            "token": "RUNTIME_TOKEN"
          }
        }
      }
    }
  }
}
```
