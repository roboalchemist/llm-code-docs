# Source: https://www.courier.com/docs/external-integrations/sms/textus.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# TextUs

> Send SMS messages using TextUs by integrating with Courier. Learn how to configure recipient profiles, override authentication and message content, and send customized text notifications with optional parameters.

## Setup

You will need a [TextUs](https://textus.com/) account with an API auth token. In Courier, navigate to the [TextUs Integration](https://app.courier.com/integrations/catalog/textus) page, enter your auth token, from number or email, then click "Save."

## Profile Requirements

To deliver an SMS message through TextUs, Courier must be provided the recipient's SMS-compatible phone number. This value should be included in the recipient profile as `phone_number`.

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

Overrides can be used to change the request that Courier makes to TextUs. You can override the `authToken`, `from`, and `email` via `config`, as well as the `body` of the SMS content.

```json  theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {
      "phone_number": "+12345678901"
    },
    "providers": {
      "textus": {
        "override": {
          "body": {
            "to": "+10987654321",
            "body": "Override message content"
          },
          "config": {
            "from": "<override from number>",
            "authToken": "<override auth token>",
            "email": "<override email>"
          }
        }
      }
    }
  }
}
```
