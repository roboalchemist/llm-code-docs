# Source: https://www.courier.com/docs/external-integrations/sms/sinch.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Sinch

> Learn how to send SMS notifications using Sinch by configuring Courier with the recipient's phone number and integrating Sinch's API for reliable and efficient message delivery.

## Setup

You will need a [Sinch](https://www.sinch.com/) account with a Service Plan ID, API token, and a from number. In Courier, navigate to the [Sinch Integration](https://app.courier.com/integrations/catalog/sinch) page, enter your Service Plan ID, API token, and from number, then click "Save."

## Profile Requirements

To deliver an SMS message through Sinch, Courier must be provided the recipient's SMS-compatible phone number. This value should be included in the recipient profile as `phone_number`.

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

Overrides can be used to change the request body and config that Courier uses to send a message through Sinch. You can override the `apiToken`, `servicePlanId`, and `url` via `config`, and any of the message body fields via `body`.

```json  theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {
      "phone_number": "+12345678901"
    },
    "providers": {
      "sinch": {
        "override": {
          "body": {
            "from": "+15555555555"
          },
          "config": {
            "apiToken": "<override API token>",
            "servicePlanId": "<override Service Plan ID>",
            "url": "<alternate API url>"
          }
        }
      }
    }
  }
}
```

Everything inside of `message.providers.sinch.override` will replace what Courier sends to the [Sinch SMS API](https://developers.sinch.com/docs/sms/).
