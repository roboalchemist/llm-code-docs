# Source: https://www.courier.com/docs/external-integrations/sms/messagebird.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# MessageBird

> Learn how to send SMS notifications through MessageBird by integrating with Courier and including the recipient's phone_number in the message profile.

## Setup

You will need a [MessageBird](https://messagebird.com/) account with an access key and an originating phone number. In Courier, navigate to the [MessageBird Integration](https://app.courier.com/integrations/catalog/messagebird-sms) page, enter your access key and originator number, then click "Save."

## Profile Requirements

To deliver a message to a recipient over MessageBird, Courier must be provided the recipient's SMS-compatible telephone number. This value should be included in the recipient profile as `phone_number`.

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

Overrides can be used to change the request body and config that Courier uses to send a message through MessageBird. You can override the `accessKey` via `config`, and any of the message body fields via `body`.

```json  theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {
      "phone_number": "+12345678901"
    },
    "providers": {
      "messagebird-sms": {
        "override": {
          "body": {
            "originator": "MyCompany"
          },
          "config": {
            "accessKey": "<override access key>"
          }
        }
      }
    }
  }
}
```

Everything inside of `message.providers.messagebird-sms.override` will replace what Courier sends to the [MessageBird SMS API](https://developers.messagebird.com/api/sms-messaging/).
