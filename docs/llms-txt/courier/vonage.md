# Source: https://www.courier.com/docs/external-integrations/sms/vonage.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Vonage

> Step-by-step tutorial for integrating Vonage (formerly Nexmo) with Courier to send SMS notifications, including required phone number formatting for recipient profiles.

## Setup

You will need a [Vonage](https://www.vonage.com/) (formerly Nexmo) account with an API key, API secret, and a from number. In Courier, navigate to the [Vonage Integration](https://app.courier.com/integrations/catalog/vonage) page, enter your API key, API secret, and from number, then click "Save."

## Profile Requirements

To deliver a message to a recipient over Vonage, Courier must be provided the recipient's SMS-compatible telephone number. Be sure that all phone numbers include country code, area code, and phone number without spaces or dashes. This value should be included in the recipient profile as `phone_number`.

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

Overrides can be used to change the request body and config that Courier uses to send a message through Vonage. You can override the `apiKey`, `apiSecret`, `fromNumber`, and `url` via `config`, and any of the message body fields via `body`.

```json  theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {
      "phone_number": "+12345678901"
    },
    "providers": {
      "vonage": {
        "override": {
          "body": {
            "text": "Override message text"
          },
          "config": {
            "apiKey": "<override API key>",
            "apiSecret": "<override API secret>",
            "fromNumber": "<override from number>",
            "url": "<alternate API url>"
          }
        }
      }
    }
  }
}
```

Everything inside of `message.providers.vonage.override` will replace what Courier sends to the [Vonage SMS API](https://developer.vonage.com/en/messaging/sms/overview).
