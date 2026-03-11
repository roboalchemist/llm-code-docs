# Source: https://www.courier.com/docs/external-integrations/sms/telnyx.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Telnyx

> Learn how to send SMS notifications via Telnyx using Courier, including how to structure recipient profiles, apply provider-specific overrides for message content and configuration, and customize Telnyx API requests.

## Setup

You will need a [Telnyx](https://telnyx.com/) account with an SMS-capable phone number and an API key. In Courier, navigate to the [Telnyx Integration](https://app.courier.com/integrations/catalog/telnyx) page, enter your API key and originating phone number, then click "Save."

## Profile Requirements

To deliver a message to a recipient over Telnyx, Courier must be provided the recipient's SMS-compatible telephone number. This value should be included in the recipient profile as `phone_number`.

```json  theme={null}
{
  "message": {
    "to": {
      "phone_number": "+12025550156"
    }
  }
}
```

## Overrides

Overrides can be used to change the request body that Courier uses to send a message. You can override any of the fields supported on the outgoing call to Telnyx:

```json  theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {
      "phone_number": "+15551734686"
    },
    "data": {
      "name": "Katherine Pryde"
    },
    "providers": {
      "telnyx": {
        "override": {
          "body": {
            "text": "Override message text",
            "to": "+17777777777"
          },
          "config": {
            "apiKey": "<your API Key>",
            "from": "+15555555555",
            "url": "<alternate url>"
          }
        }
      }
    }
  }
}
```

Everything inside of `message.providers.telnyx.override` will replace what Courier sends to the [Telnyx Messaging API](https://developers.telnyx.com/api/messaging/send-message).
